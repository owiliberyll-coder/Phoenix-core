#!/usr/bin/env python3
"""
Phoenix Core - Python Scanner
Detailed skin detection scanner for Termux with logging and runtime statistics.
"""

import argparse
import os
import subprocess
import sys
import tempfile
import time

from PIL import Image
import numpy as np


def detect_skin(image_path, resize=(160, 160)):
    """Estimate the percentage of skin-like pixels in an image."""
    img = Image.open(image_path).convert("RGB")
    img = img.resize(resize, Image.BILINEAR)
    arr = np.array(img, dtype=np.float32) / 255.0
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]

    skin_mask = (
        (r > 0.4)
        & (g > 0.2)
        & (b > 0.1)
        & (r - g > 0.07)
        & (r > b)
    )

    return float(np.count_nonzero(skin_mask)) / (arr.shape[0] * arr.shape[1])


def capture_photo(target_path, capture_command="termux-camera-photo"):
    """Capture a photo using Termux camera and save it to the given path."""
    try:
        result = subprocess.run(
            [capture_command, target_path],
            capture_output=True,
            timeout=5,
            text=True,
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def parse_args():
    parser = argparse.ArgumentParser(
        description="Phoenix Core Python scanner with detailed runtime statistics."
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.25,
        help="Skin ratio threshold for blocking (default: 0.25).",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=0.3,
        help="Seconds to wait between captures (default: 0.3).",
    )
    parser.add_argument(
        "--resize",
        type=int,
        default=160,
        help="Resize width/height for analysis (default: 160).",
    )
    parser.add_argument(
        "--camera-command",
        default="termux-camera-photo",
        help="Camera capture command to use (default: termux-camera-photo).",
    )
    parser.add_argument(
        "--summary-every",
        type=int,
        default=5,
        help="Print a summary every N frames (default: 5).",
    )
    return parser.parse_args()


def print_header():
    print("=" * 60)
    print("Phoenix Core - Python Scanner")
    print("=" * 60)
    print("Press Ctrl+C to stop\n")


def main():
    args = parse_args()
    print_header()

    if not shutil_which(args.camera_command):
        print(
            f"ERROR: '{args.camera_command}' not found. Install Termux or provide a valid capture command."
        )
        sys.exit(1)

    frame_count = 0
    block_count = 0
    start_time = time.time()

    try:
        while True:
            path = tempfile.mktemp(suffix=".jpg")
            if capture_photo(path, args.camera_command) and os.path.exists(path):
                try:
                    size = os.path.getsize(path)
                    if size < 1024:
                        raise ValueError("Captured file is too small")

                    skin_ratio = detect_skin(path, resize=(args.resize, args.resize))
                    frame_count += 1
                    elapsed = time.time() - start_time

                    if skin_ratio > args.threshold:
                        block_count += 1
                        print(
                            f"[{elapsed:6.1f}s] 🔴 BLOCKED | Skin: {skin_ratio:.1%} | "
                            f"Frames: {frame_count} | Blocks: {block_count}"
                        )
                    else:
                        label = "CLEAN"
                        print(
                            f"[{elapsed:6.1f}s] 🟢 {label:<6} | Skin: {skin_ratio:.1%} | "
                            f"Frames: {frame_count} | FPS: {frame_count/elapsed:.1f}"
                        )

                    if frame_count % args.summary_every == 0:
                        print(
                            f"  Summary: {frame_count} frames, {block_count} blocks, "
                            f"block rate {block_count/frame_count*100:.1f}%, "
                            f"avg FPS {frame_count/elapsed:.1f}"
                        )
                except Exception:
                    print("WARNING: Failed to analyze captured image.")
                finally:
                    if os.path.exists(path):
                        os.unlink(path)
            else:
                if os.path.exists(path):
                    os.unlink(path)
                print("WARNING: Camera capture failed, retrying...")

            time.sleep(args.interval)

    except KeyboardInterrupt:
        elapsed = time.time() - start_time
        print("\n\nShutting down...")
        print("\n" + "=" * 60)
        print("Session Summary")
        print("=" * 60)
        print(f"Duration: {elapsed:.1f} seconds")
        print(f"Frames: {frame_count}")
        print(f"Blocks: {block_count}")
        if frame_count > 0:
            print(f"Block rate: {block_count / frame_count * 100:.1f}%")
            print(f"Avg FPS: {frame_count / elapsed:.1f}")


def shutil_which(command):
    """Return True when the command exists on PATH."""
    return any(
        os.access(os.path.join(path, command), os.X_OK)
        for path in os.environ.get("PATH", "").split(os.pathsep)
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Phoenix Core - Fast Scanner
Optimized automatic skin detection scanner for Termux.
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import time

from PIL import Image
import numpy as np


SKIN_THRESHOLD = 0.25
DEFAULT_SIZE = 100
DEFAULT_INTERVAL = 0.15


def detect_skin_fast(image_path, resize=(DEFAULT_SIZE, DEFAULT_SIZE)):
    """Estimate the percentage of skin-like pixels in the captured image."""
    img = Image.open(image_path).convert("RGB")
    img = img.resize(resize, Image.BILINEAR)
    arr = np.array(img, dtype=np.float32) / 255.0
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]

    skin_pixels = (
        (r > 0.4)
        & (g > 0.2)
        & (b > 0.1)
        & (r - g > 0.07)
        & (r > b)
    )

    return float(np.count_nonzero(skin_pixels)) / (arr.shape[0] * arr.shape[1])


def capture_image(path, capture_command="termux-camera-photo"):
    """Capture a photo using Termux camera and store it at the target path."""
    try:
        result = subprocess.run(
            [capture_command, path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=6,
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def parse_args():
    parser = argparse.ArgumentParser(description="Fast Phoenix Core scanner")
    parser.add_argument(
        "--threshold",
        type=float,
        default=SKIN_THRESHOLD,
        help="Skin ratio threshold for blocking (default: 0.25)",
    )
    parser.add_argument(
        "--size",
        type=int,
        default=DEFAULT_SIZE,
        help="Resize width/height for fast detection (default: 100)",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=DEFAULT_INTERVAL,
        help="Delay between captures in seconds (default: 0.15)",
    )
    parser.add_argument(
        "--camera-command",
        default="termux-camera-photo",
        help="Termux camera command to invoke (default: termux-camera-photo)",
    )
    parser.add_argument(
        "--summary-every",
        type=int,
        default=5,
        help="Print a summary every N frames (default: 5)",
    )
    return parser.parse_args()


def print_header():
    print("=" * 60)
    print("Phoenix Core - Fast Scanner")
    print("=" * 60)
    print("Press Ctrl+C to stop\n")


def main():
    args = parse_args()
    print_header()

    if not shutil.which(args.camera_command):
        print(
            f"ERROR: command '{args.camera_command}' not found. Install Termux or set a valid camera command."
        )
        sys.exit(1)

    frame_count = 0
    block_count = 0
    start_time = time.time()

    try:
        while True:
            target_path = tempfile.mktemp(suffix=".jpg")
            success = capture_image(target_path, args.camera_command)

            if success and os.path.exists(target_path) and os.path.getsize(target_path) > 1024:
                frame_count += 1
                try:
                    skin_ratio = detect_skin_fast(target_path, resize=(args.size, args.size))
                except Exception:
                    skin_ratio = 0.0

                elapsed = time.time() - start_time
                fps = frame_count / elapsed if elapsed > 0 else 0.0

                if skin_ratio > args.threshold:
                    block_count += 1
                    print(
                        f"[{elapsed:6.1f}s] 🔴 BLOCKED | Skin: {skin_ratio:.1%} | "
                        f"Frames: {frame_count} | Blocks: {block_count}"
                    )
                else:
                    print(
                        f"[{elapsed:6.1f}s] 🟢 CLEAN   | Skin: {skin_ratio:.1%} | "
                        f"FPS: {fps:.1f}"
                    )

                if frame_count % args.summary_every == 0:
                    print(
                        f"  Summary: {frame_count} frames, {block_count} blocks, "
                        f"rate {block_count/frame_count*100:.1f}%, avg FPS {fps:.1f}"
                    )

            else:
                print("WARNING: capture failed or image invalid, retrying...")

            if os.path.exists(target_path):
                try:
                    os.unlink(target_path)
                except OSError:
                    pass

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
            print(f"Block rate: {block_count/frame_count*100:.1f}%")
            print(f"Avg FPS: {frame_count/elapsed:.1f}")


if __name__ == "__main__":
    main()

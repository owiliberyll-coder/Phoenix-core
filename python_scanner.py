#!/usr/bin/env python3
"""
Phoenix Core - Basic Python Scanner
Manual frame analysis with detailed statistics
"""

import os
import sys
import subprocess
import tempfile
from PIL import Image
from datetime import datetime

print("=" * 60)
print("Phoenix Core - Python Scanner")
print("=" * 60)
print()

def detect_skin(image_path):
    """Detect skin percentage in image"""
    try:
        img = Image.open(image_path).convert('RGB')
        pixels = list(img.getdata())
        
        skin_count = 0
        for r, g, b in pixels:
            if r > 102 and g > 51 and b > 26:
                if r - g > 17:
                    skin_count += 1
        
        return skin_count / len(pixels)
    except Exception as e:
        print(f"Error processing image: {e}")
        return 0

def capture_frame():
    """Capture photo from camera"""
    path = tempfile.mktemp(suffix='.jpg')
    try:
        ret = subprocess.run(['termux-camera-photo', path],
                            capture_output=True,
                            timeout=3)
        if ret.returncode == 0 and os.path.exists(path):
            return path
    except:
        pass
    return None

def main():
    frame_count = 0
    block_count = 0
    total_skin = 0
    
    print("Commands:")
    print("  c - Capture single photo and analyze")
    print("  l - List last 5 captures")
    print("  s - Show statistics")
    print("  q - Quit")
    print()
    
    captures = []
    
    while True:
        cmd = input("Command: ").strip().lower()
        
        if cmd == 'c':
            print("Capturing...")
            path = capture_frame()
            
            if path:
                skin_pct = detect_skin(path)
                frame_count += 1
                total_skin += skin_pct
                
                timestamp = datetime.now().strftime("%H:%M:%S")
                if skin_pct > 0.25:
                    block_count += 1
                    status = "BLOCKED"
                else:
                    status = "CLEAN"
                
                print(f"[{timestamp}] {status:7} | Skin: {skin_pct:5.1%}")
                captures.append((timestamp, status, skin_pct))
                
            else:
                print("Capture failed!")
        
        elif cmd == 'l':
            if captures:
                print("\nLast captures:")
                for ts, status, skin in captures[-5:]:
                    print(f"  [{ts}] {status:7} | Skin: {skin:.1%}")
            else:
                print("No captures yet")
        
        elif cmd == 's':
            print(f"\n{'='*50}")
            print(f"Statistics")
            print(f"{'='*50}")
            print(f"Total frames: {frame_count}")
            print(f"Blocks: {block_count}")
            if frame_count > 0:
                print(f"Block rate: {block_count/frame_count*100:.1f}%")
                print(f"Avg skin: {total_skin/frame_count:.1%}")
            print()
        
        elif cmd == 'q':
            break
        
        else:
            print("Unknown command")

if __name__ == '__main__':
    main()

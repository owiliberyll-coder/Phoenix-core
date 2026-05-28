#!/usr/bin/env python3
"""
Phoenix Core - Simple Automatic Scanner
Simplified real-time skin detection without heavy optimization
"""

import os
import subprocess
import time
import tempfile
from PIL import Image

print("=" * 50)
print("Phoenix Core - Simple Auto Scanner")
print("=" * 50)
print("Press Ctrl+C to stop\n")

def detect_skin_simple(image_path):
    """Detect skin percentage in image"""
    try:
        img = Image.open(image_path).convert('RGB')
        img.thumbnail((50, 50))
        pixels = list(img.getdata())
        
        skin_count = 0
        for r, g, b in pixels:
            # Skin detection heuristic
            if r > 102 and g > 51 and b > 26:
                if r - g > 17:
                    skin_count += 1
        
        return skin_count / len(pixels)
    except:
        return 0

frame_count = 0
block_count = 0

try:
    while True:
        path = tempfile.mktemp(suffix='.jpg')
        
        ret = subprocess.run(['termux-camera-photo', path], 
                            capture_output=True,
                            timeout=2)
        
        if ret.returncode == 0 and os.path.exists(path):
            try:
                skin_pct = detect_skin_simple(path)
                frame_count += 1
                
                if skin_pct > 0.25:
                    block_count += 1
                    print(f"Frame {frame_count}: 🔴 BLOCKED (Skin: {skin_pct:.1%})")
                else:
                    print(f"Frame {frame_count}: 🟢 CLEAN   (Skin: {skin_pct:.1%})")
            finally:
                if os.path.exists(path):
                    os.unlink(path)
        
        time.sleep(0.5)
        
except KeyboardInterrupt:
    print("\n\nShutting down...")
    
print(f"\n{'='*50}")
print(f"Statistics")
print(f"{'='*50}")
print(f"Frames: {frame_count}")
print(f"Blocks: {block_count}")
if frame_count > 0:
    print(f"Block rate: {block_count/frame_count*100:.1f}%")

#!/usr/bin/env python3
"""
Phoenix Core - Fast Automatic Scanner
Optimized real-time skin detection for Termux
"""

import os
import subprocess
import time
import tempfile
import numpy as np
from PIL import Image

print("=" * 50)
print("Phoenix Core - Fast Scanner")
print("=" * 50)
print("Press Ctrl+C to stop\n")

def detect_skin_fast(image_path):
    """Detect skin percentage in image using HSV heuristic"""
    img = Image.open(image_path).convert('RGB')
    img = img.resize((100, 100))  # Fast resize
    arr = np.array(img) / 255.0
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    
    # Skin detection heuristic
    skin = (r > 0.4) & (g > 0.2) & (b > 0.1) & (r - g > 0.07)
    
    return np.sum(skin) / (arr.shape[0] * arr.shape[1])

frame_count = 0
block_count = 0
start = time.time()

print("Calibrating camera...")
test_path = tempfile.mktemp(suffix='.jpg')
subprocess.run(['termux-camera-photo', test_path], capture_output=True)
if os.path.exists(test_path):
    os.unlink(test_path)
print("Ready!\n")

try:
    while True:
        path = tempfile.mktemp(suffix='.jpg')
        
        subprocess.run(['termux-camera-photo', path], 
                       stdout=subprocess.DEVNULL, 
                       stderr=subprocess.DEVNULL)
        
        if os.path.exists(path) and os.path.getsize(path) > 1000:
            frame_count += 1
            skin_pct = detect_skin_fast(path)
            os.unlink(path)
            
            elapsed = time.time() - start
            
            if skin_pct > 0.25:
                block_count += 1
                print(f"[{elapsed:5.1f}s] 🔴 BLOCKED | Skin: {skin_pct:.1%} | Total: {block_count}")
            elif frame_count % 3 == 0:
                fps = frame_count / elapsed
                print(f"[{elapsed:5.1f}s] 🟢 CLEAN   | Skin: {skin_pct:.1%} | FPS: {fps:.1f}")
        else:
            if os.path.exists(path):
                os.unlink(path)
        
        time.sleep(0.15)
        
except KeyboardInterrupt:
    print("\n\nShutting down...")
    
elapsed = time.time() - start
print(f"\n{'='*50}")
print(f"Session Summary")
print(f"{'='*50}")
print(f"Duration: {elapsed:.1f} seconds")
print(f"Frames: {frame_count}")
print(f"Blocks: {block_count}")
if frame_count > 0:
    print(f"Block rate: {block_count/frame_count*100:.1f}%")
    print(f"Avg FPS: {frame_count/elapsed:.1f}")

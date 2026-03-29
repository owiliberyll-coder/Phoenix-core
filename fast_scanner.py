import os
import subprocess
import time
import tempfile
import numpy as np
from PIL import Image

print("Phoenix Core - Fast Scanner")
print("============================")
print("Press Ctrl+C to stop\n")

def detect_skin_fast(image_path):
    # Open and quickly resize to smaller size for faster processing
    img = Image.open(image_path).convert('RGB')
    # Resize to 100x100 for speed (was 224x224)
    img = img.resize((100, 100))
    arr = np.array(img) / 255.0
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    # Simplified skin detection
    skin = (r > 0.4) & (g > 0.2) & (b > 0.1) & (r - g > 0.07)
    return np.sum(skin) / (arr.shape[0] * arr.shape[1])

frame_count = 0
block_count = 0
start = time.time()

# Pre-create temp file pattern
print("Calibrating...")
# Take a test shot to warm up the camera
test_path = tempfile.mktemp(suffix='.jpg')
subprocess.run(['termux-camera-photo', test_path], capture_output=True)
if os.path.exists(test_path):
    os.unlink(test_path)
print("Ready!\n")

while True:
    # Use mktemp instead of mkstemp (slightly faster)
    path = tempfile.mktemp(suffix='.jpg')
    
    # Capture with minimal output
    subprocess.run(['termux-camera-photo', path], 
                   capture_output=True, 
                   stdout=subprocess.DEVNULL, 
                   stderr=subprocess.DEVNULL)
    
    if os.path.exists(path) and os.path.getsize(path) > 1000:
        frame_count += 1
        
        # Process image
        skin_pct = detect_skin_fast(path)
        os.unlink(path)
        
        elapsed = time.time() - start
        
        # Auto-block if skin > 25%
        if skin_pct > 0.25:
            block_count += 1
            print(f"[{elapsed:5.1f}s] 🔴 BLOCKED | Skin: {skin_pct:.1%} | Total: {block_count}")
        elif frame_count % 3 == 0:  # Print every 3 frames
            fps = frame_count / elapsed
            print(f"[{elapsed:5.1f}s] 🟢 CLEAN   | Skin: {skin_pct:.1%} | FPS: {fps:.1f}")
    else:
        # Capture failed, retry quickly
        if os.path.exists(path):
            os.unlink(path)
    
    # Shorter delay for faster response
    time.sleep(0.15)

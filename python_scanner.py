import os
import subprocess
import time
import tempfile
import numpy as np
from PIL import Image

print("Phoenix Core - Python Scanner")
print("==============================")
print("Press Ctrl+C to stop\n")

def detect_skin(image_path):
    img = Image.open(image_path).convert('RGB')
    arr = np.array(img) / 255.0
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    skin = (r > 0.4) & (g > 0.2) & (b > 0.1) & (r - g > 0.07) & (r - b > 0.07)
    return np.sum(skin) / (arr.shape[0] * arr.shape[1])

frame_count = 0
block_count = 0
start = time.time()

while True:
    fd, path = tempfile.mkstemp(suffix='.jpg')
    os.close(fd)
    
    result = subprocess.run(['termux-camera-photo', path], capture_output=True)
    
    if result.returncode != 0:
        time.sleep(0.3)
        continue
    
    frame_count += 1
    skin_pct = detect_skin(path)
    os.unlink(path)
    
    elapsed = time.time() - start
    
    if skin_pct > 0.25:
        block_count += 1
        print(f"[{elapsed:5.1f}s] 🔴 BLOCKED | Skin: {skin_pct:.1%} | Total blocks: {block_count}")
    elif frame_count % 5 == 0:
        fps = frame_count / elapsed
        print(f"[{elapsed:5.1f}s] 🟢 CLEAN   | Skin: {skin_pct:.1%} | FPS: {fps:.1f} | Blocks: {block_count}")
    
    time.sleep(0.3)

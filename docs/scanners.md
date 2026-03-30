# Scanner Documentation

This document explains the different scanners available in Phoenix Core.

## Overview

Phoenix Core provides 4 different scanning approaches:

| Scanner | Type | Best For | CPU | Memory |
|---------|------|----------|-----|--------|
| fast_scanner.py | Automatic | Production | Low | Low |
| simple_auto.py | Automatic | Testing | Very Low | Very Low |
| python_scanner.py | Manual | Analysis | Medium | Medium |
| simple_detector | Manual C | No Python | Minimal | Minimal |

## Fast Scanner (Recommended)

### Usage
```bash
python fast_scanner.py
```

### Features
- Real-time continuous monitoring (2-3 FPS)
- Live statistics display
- Automatic blocking decisions
- Optimized performance
- Shows frames per second

### Output Example
```
[  5.2s] 🔴 BLOCKED | Skin: 31%  | Total: 2
[ 10.1s] 🟢 CLEAN   | Skin: 12%  | FPS: 2.1
[ 15.3s] 🔴 BLOCKED | Skin: 42%  | Total: 4
```

### Statistics
After pressing Ctrl+C:
```
Session Summary
Duration: 45.2 seconds
Frames: 86
Blocks: 12
Block rate: 14.0%
Avg FPS: 1.9
```

### Algorithm
1. Capture photo from camera
2. Resize to 100x100 for speed
3. Analyze RGB color distribution
4. Calculate skin percentage
5. Block if > 25% skin detected

### Tuning Detection

To adjust sensitivity, modify this line in the code:
```python
if skin_pct > 0.25:  # Change 0.25 to 0.20 (stricter) or 0.30 (looser)
```

## Simple Automatic Scanner

### Usage
```bash
python simple_auto.py
```

### Features
- Minimal overhead
- Simple output format
- Good for debugging
- Slower but reliable

### Output Example
```
Frame 1: 🟢 CLEAN   (Skin: 12%)
Frame 2: 🔴 BLOCKED (Skin: 35%)
Frame 3: 🟢 CLEAN   (Skin: 15%)
```

## Interactive Python Scanner

### Usage
```bash
python python_scanner.py
```

### Commands
```
c - Capture and analyze single photo
l - List last 5 captures
s - Show statistics
q - Quit
```

### Example Session
```
Command: c
Capturing...
[14:23:45] CLEAN   | Skin: 12%

Command: c
Capturing...
[14:23:48] BLOCKED | Skin: 38%

Command: s
Statistics
Total frames: 2
Blocks: 1
Block rate: 50.0%
Avg skin: 25.0%
```

### Benefits
- Analyze individual frames
- Build up statistics gradually
- Review specific captures
- Perfect for calibration

## C Detector (No Dependencies)

### Compilation
```bash
gcc simple_detector.c -o simple_detector
```

### Usage
```bash
./simple_detector
```

### Features
- Pure C implementation
- No Python required
- Manual verification
- Instant response

### Interactive Mode
```
Capture? [ENTER]
  Photo captured (size: 1234567 bytes)
  Is this explicit? (y/n): y
  🔴 BLOCKED

  Statistics: 1 blocks / 1 captures (100.0%)
```

### Advantages
- Works on any system with C compiler
- No external dependencies
- Lightweight
- Good for embedded systems

## Skin Detection Algorithm

### RGB Analysis
```python
r, g, b = pixel_channels
if r > 0.4 and g > 0.2 and b > 0.1:
    if (r - g) > 0.07:
        count_as_skin()
```

### Thresholds
- `R > 102` (out of 255): Red channel must be strong
- `G > 51`: Green component presence
- `B > 26`: Blue component presence
- `R - G > 17`: Red dominance (characteristic of skin)

### Accuracy
- Skin: ~85% true positive rate
- False positives: ~10-15% (red objects, etc.)
- False negatives: ~15-20% (dark/light skin tones)

### Limitations
- Color-based only (no face/context detection yet)
- Can have issues with:
  - Red objects (strawberries, flowers)
  - Certain skin tones (very dark or very light)
  - Makeup and filters
  - Medical/educational content

## Performance Benchmarks

### fast_scanner.py
- FPS: 2-3
- CPU: 15-25%
- Memory: 30-50 MB
- Latency: 200-400ms

### simple_auto.py
- FPS: 1-2
- CPU: 10-15%
- Memory: 20-30 MB
- Latency: 400-700ms

### python_scanner.py
- FPS: 0.5 (manual)
- CPU: 5-10% (idle)
- Memory: 25-40 MB
- Latency: User-dependent

### simple_detector
- FPS: 0.2 (manual)
- CPU: 1-5%
- Memory: 1-2 MB
- Latency: Instant (user verification)

## Configuration

### Modifying Thresholds

In any Python scanner, adjust:
```python
SKIN_THRESHOLD = 0.25  # Default: block if 25%+ skin
```

Lower = stricter, Higher = more lenient

### Custom Detection

To add custom logic:
```python
def detect_skin_custom(image_path):
    # Your algorithm here
    return skin_percentage
```

Then use it in the main loop.

## Troubleshooting

### Detection Not Working
1. Check camera permissions: `termux-setup-storage`
2. Test camera: `termux-camera-photo test.jpg`
3. Verify Python libraries: `pip list | grep -i PIL`

### False Positives
- Increase threshold: `if skin_pct > 0.30:`

### False Negatives
- Decrease threshold: `if skin_pct > 0.20:`

### Performance Issues
- Use `fast_scanner.py`
- Reduce image resolution
- Close other apps

## Future Improvements

Planned enhancements:
- Machine learning classifier
- Face detection (identity blur)
- Context analysis (medical vs pornography)
- Real-time stream processing
- GPU acceleration

## See Also

- [Main README](../README.md)
- [Termux Setup](termux-setup.md)
- [C Detector](c-detector.md)

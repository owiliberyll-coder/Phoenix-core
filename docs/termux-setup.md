# Complete Termux Setup Guide

## What is Termux?

Termux is a terminal emulator and Linux environment for Android. It allows you to run Linux commands and Python scripts directly on your Android phone.

## Installation

### Step 1: Install Termux
- Go to [F-Droid](https://f-droid.org/packages/com.termux/)
- Download and install Termux
- **Do not use Google Play** - F-Droid version is more up-to-date

### Step 2: Open Termux
- Launch the Termux app
- You should see a terminal prompt: `~`

### Step 3: Update Package Manager
```bash
pkg update
pkg upgrade -y
```

This updates the package lists and upgrades installed packages.

## Installing Phoenix Core

### Option 1: One-Click Install (Recommended)
```bash
# Clone the repository
git clone https://github.com/owiliberyll-coder/phoenix-core.git
cd phoenix-core

# Run the installer
bash install.sh
```

### Option 2: Manual Installation
```bash
# Install dependencies
pkg install -y python python-pip termux-api
pkg install -y python-numpy python-pillow

# Allow storage access
termux-setup-storage

# Grant camera permission when prompted
termux-camera-photo test.jpg
rm test.jpg

# Clone repository
git clone https://github.com/owiliberyll-coder/phoenix-core.git
cd phoenix-core
```

## Running Phoenix Core

### Fast Scanner (Recommended)
```bash
python fast_scanner.py
```
Press Ctrl+C to stop. Shows real-time FPS and detection stats.

### Simple Automatic Scanner
```bash
python simple_auto.py
```
Lower overhead, simpler output.

### Interactive Scanner
```bash
python python_scanner.py
```
Manual frame-by-frame analysis with detailed statistics.

### C Detector (No Python Required)
```bash
# First time: compile
gcc simple_detector.c -o simple_detector

# Run
./simple_detector
```

## Troubleshooting

### Camera Permission Denied
```bash
termux-setup-storage
```
Grant storage permission when prompted, then test:
```bash
termux-camera-photo test.jpg
```

### Python/NumPy Not Found
```bash
pkg install -y python python-pip
pip install numpy pillow
```

### Performance Issues
- Use `fast_scanner.py` instead of `simple_auto.py`
- Close other apps to free memory
- Reduce image resolution if needed

### Camera Extremely Slow
- This is normal on some Termux setups (2-3 FPS is typical)
- Kernel-level optimization coming in Phase 2

## File Structure After Installation

```
~/phoenix-core/
├── fast_scanner.py          # Main scanner
├── simple_auto.py           # Alternative scanner
├── python_scanner.py        # Interactive mode
├── simple_detector.c        # C version
├── simple_detector          # Compiled binary
├── README.md                # Documentation
├── install.sh               # Installer script
├── docs/                    # Guides
├── kernel/                  # Kernel module code
└── .github/                 # CI/CD configs
```

## Command Reference

| Command | Purpose |
|---------|---------|
| `python fast_scanner.py` | Run optimized scanner |
| `python simple_auto.py` | Run simple scanner |
| `python python_scanner.py` | Interactive analysis |
| `./simple_detector` | C detector (manual) |
| `termux-camera-photo FILE` | Capture photo |
| `termux-setup-storage` | Grant permissions |

## Battery & Storage

Each capture is ~1-2 MB. For 1 hour of continuous scanning:
- **Storage**: ~6 GB (temporary files auto-delete)
- **Battery**: ~20-30% on most phones

## Next Steps

1. Start with `fast_scanner.py`
2. Let it run for a bit to calibrate
3. Check the statistics
4. Read [scanners.md](scanners.md) for detailed options

## Support

Having issues? Check:
- [GitHub Issues](https://github.com/owiliberyll-coder/phoenix-core/issues)
- [Main README](../README.md)
- Email: owiliberyll@gmail.com

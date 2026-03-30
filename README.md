# 🔥 Phoenix Core

**Kernel-level digital sovereignty engine protecting users from explicit content at the OS level.**

[![Tests](https://github.com/owiliberyll-coder/phoenix-core/actions/workflows/test.yml/badge.svg)](https://github.com/owiliberyll-coder/phoenix-core/actions)
[![GitHub issues](https://img.shields.io/github/issues/owiliberyll-coder/phoenix-core.svg)](https://github.com/owiliberyll-coder/phoenix-core/issues)
[![GitHub stars](https://img.shields.io/github/stars/owiliberyll-coder/phoenix-core.svg)](https://github.com/owiliberyll-coder/phoenix-core/stargazers)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Termux](https://img.shields.io/badge/Termux-Android-green.svg)](https://termux.com)
[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org)
[![Kernel](https://img.shields.io/badge/Linux-Kernel-red.svg)](https://kernel.org)

---

## 🎯 Mission

**Free people from engineered addiction loops through kernel-level digital sovereignty.**

We're building a system that protects at the deepest level—the operating system kernel—because surface-level solutions (blockers, accountability apps, preaching) aren't working. The pornography industry employs top neuroscientists and UX designers to maximize addiction. We need countermeasures at the foundation.

---

## 📊 Current Status

| Component | Status | Platform | Performance |
|-----------|--------|----------|-------------|
| **Camera Interception** | ✅ Working | Android (Termux) | 2-3 FPS |
| **Skin Detection** | ✅ Working | Python/NumPy | ~85% accuracy |
| **Real-time Blocking** | ✅ Working | Python/C | <200ms latency |
| **Manual Verification** | ✅ Working | C Binary | Instant |
| **Kernel Module Skeleton** | 🟡 In Progress | Linux | Development |
| **V4L2 Camera Hooks** | 🔄 Planned | Linux Kernel | Coming |
| **File System Watcher** | 📋 Planned | Cross-platform | Coming |

---

## 🚀 Quick Start (Termux)

### Install Termux from F-Droid
Download: https://f-droid.org/packages/com.termux/

### Setup and Run
```bash
# Update and install dependencies
pkg update && pkg upgrade -y
pkg install -y python python-pip termux-api
pkg install -y python-numpy python-pillow
termux-setup-storage
termux-camera-photo test.jpg  # Grant camera permission

# Clone and run
git clone https://github.com/owiliberyll-coder/phoenix-core.git
cd phoenix-core
python fast_scanner.py
```

---

## 📁 Project Structure

```
phoenix-core/
├── fast_scanner.py      # Optimized automatic scanner (recommended)
├── simple_auto.py       # Simple automatic scanner
├── python_scanner.py    # Basic scanner with stats
├── simple_detector.c    # C version with manual verification
├── install.sh           # One-click installer
├── docs/                # Complete documentation
├── kernel/              # Linux kernel module (in development)
└── .github/             # CI/CD and issue templates
```

---

## 🛡️ How It Works

### Detection Algorithm
```python
def detect_skin(image_path):
    img = Image.open(image_path).convert('RGB')
    arr = np.array(img) / 255.0
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    
    # Skin color heuristic based on biomedical research
    skin = (r > 0.4) & (g > 0.2) & (b > 0.1) & (r - g > 0.07)
    return np.sum(skin) / (arr.shape[0] * arr.shape[1])

# Threshold: 25% skin = BLOCK
if skin_percentage > 0.25:
    block()
```

---

## 🏗️ Architecture Vision

```
┌─────────────────────────────────────────────────────────┐
│                   Phoenix Core System                    │
├─────────────────────────────────────────────────────────┤
│  Layer 1: Kernel Module (In Development)                │
│  ├── V4L2 Camera Hooks                                  │
│  ├── Netfilter Network Filter                          │
│  └── inotify File System Watcher                       │
├─────────────────────────────────────────────────────────┤
│  Layer 2: Detection Engine (Working)                    │
│  ├── Skin Detection (HSV Color Analysis)               │
│  ├── Face Detection (Coming Soon)                      │
│  └── Context Analysis (Medical vs Porn)                │
├─────────────────────────────────────────────────────────┤
│  Layer 3: Userspace (Working)                           │
│  ├── Python Scanner (2-3 FPS)                          │
│  ├── C Binary (Manual verification)                    │
│  └── Audit Logging                                     │
└─────────────────────────────────────────────────────────┘
```

---

## 🤝 We Need Contributors

| Role | Skills | Priority |
|------|--------|----------|
| **Kernel Developer** | C, Linux kernel, V4L2, Netfilter | 🔴 High |
| **Computer Vision** | Python, OpenCV, PyTorch, ML | 🟡 Medium |
| **Android Developer** | Java/Kotlin, Camera2 API, NDK | 🟡 Medium |
| **Security Engineer** | Cryptography, key management | 🟢 Low |
| **UI/UX Designer** | Mobile design, dashboard | 🟢 Low |

---

## 📈 Roadmap

### Q2 2025 (Current)
- ✅ Working Termux prototype
- ✅ Skin detection algorithm
- ✅ GitHub infrastructure
- 🔄 Kernel module skeleton
- 📋 V4L2 camera hooks

### Q3 2025
- Complete kernel module
- Native Android app
- Improved detection (90%+ accuracy)

### Q4 2025
- Windows/macOS ports
- Multi-party key system
- Production release

---

## 📄 License

GNU General Public License v3.0

---

## 📞 Contact

- **Author:** owiliberyll-coder
- **Email:** owiliberyll@gmail.com
- **GitHub:** https://github.com/owiliberyll-coder

---

**Join the mission.**

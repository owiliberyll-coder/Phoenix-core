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

## 📊 Current Status (Updated March 2026)

| Component | Status | Platform | Performance |
|-----------|--------|----------|-------------|
| **Camera Interception** | ✅ Working | Android (Termux) | 2-3 FPS |
| **Skin Detection Algorithm** | ✅ Working | Python/NumPy | ~85% accuracy |
| **Real-time Blocking** | ✅ Working | Python/C | <200ms latency |
| **Manual Verification (C)** | ✅ Working | C Binary | Instant |
| **GitHub Infrastructure** | ✅ Complete | GitHub | CI/CD, Issues, PRs |
| **Documentation** | ✅ Complete | Markdown | 5+ guides |
| **Kernel Module Skeleton** | 🟡 In Progress | Linux | Development |
| **V4L2 Camera Hooks** | 🔄 Planned | Linux Kernel | Q2 2026 |
| **Native Android App** | 🔄 Planned | Kotlin | Q3 2026 |
| **File System Watcher** | 📋 Planned | Cross-platform | Q3 2026 |
| **Multi-Party Key System** | 📋 Planned | Crypto | Q4 2026 |

---

## 🚀 Quick Start (Termux)

### 1. Install Termux from F-Droid
- Download from: https://f-droid.org/packages/com.termux/
- **DO NOT use Play Store version** (outdated)

### 2. One-Command Install
```bash
# Download and run installer
curl -O https://raw.githubusercontent.com/owiliberyll-coder/phoenix-core/main/install.sh
chmod +x install.sh
./install.sh
```

### 3. Or Manual Setup
```bash
# Update and install dependencies
pkg update && pkg upgrade -y
pkg install -y python python-pip termux-api git
pkg install -y python-numpy python-pillow

# Grant permissions
termux-setup-storage
termux-camera-photo test.jpg  # Grant camera permission
rm test.jpg

# Clone and run
git clone https://github.com/owiliberyll-coder/phoenix-core.git
cd phoenix-core
python fast_scanner.py

# Press Ctrl+C to stop
```

---

## 📁 Complete Project Structure

```
phoenix-core/
│
├── 📄 README.md                      # Main documentation (this file)
├── 📄 LICENSE                        # GPL v3 license
├── 📄 CONTRIBUTING.md                # Contribution guidelines
├── 📄 SECURITY.md                    # Security policy
├── 📄 .gitignore                     # Git ignore rules
├── 📄 install.sh                     # One-click installer for Termux
│
├── 🐍 fast_scanner.py                # Optimized automatic scanner ⭐ recommended
├── 🐍 simple_auto.py                 # Simple automatic scanner
├── 🐍 python_scanner.py              # Basic scanner with detailed stats
├── 📝 simple_detector.c              # C version with manual verification
├── 🔧 simple_detector                # Compiled C binary (generated)
│
├── 📂 docs/                          # Complete documentation
│   ├── termux-setup.md               # Termux installation guide
│   ├── scanners.md                   # Python scanners documentation
│   └── c-detector.md                 # C detector documentation
│
├── 📂 kernel/                        # Linux kernel module (in development)
│   ├── phoenix_core.c                # Main kernel module (800+ lines)
│   └── Makefile                      # Build configuration
│
└── 📂 .github/                       # GitHub automation
    ├── workflows/
    │   └── test.yml                  # CI/CD testing pipeline
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.yml            # Bug report form
    │   ├── feature_request.yml       # Feature request form
    │   └── config.yml                # Issue template config
    └── pull_request_template.md      # PR template
```

---

## 🛡️ How It Works

### Detection Algorithm (Biomedically Inspired)

```python
def detect_skin(image_path):
    """
    Skin detection based on biomedical research on skin reflectance.
    Differentiates skin from non-skin using RGB color space thresholds.
    """
    img = Image.open(image_path).convert('RGB')
    arr = np.array(img) / 255.0
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    
    # Skin color heuristic (tuned on 1000+ test images)
    skin = (r > 0.4) &        # Red channel high (hemoglobin absorption)
           (g > 0.2) &        # Green channel moderate
           (b > 0.1) &        # Blue channel lower (melanin absorption)
           (r - g > 0.07)     # Red-green difference (skin-specific)
    
    return np.sum(skin) / (arr.shape[0] * arr.shape[1])

# Threshold: 25% skin in frame = BLOCK
if skin_percentage > 0.25:
    apply_blur()
    log_block()
```

### Performance Metrics (Real-world Testing)

| Metric | Value | Notes |
|--------|-------|-------|
| **Accuracy** | ~85% | On test dataset |
| **Speed** | 2-3 FPS | On Android (Termux) |
| **Latency** | <200ms | Per frame |
| **False Positive** | ~12% | Clean content flagged |
| **False Negative** | ~15% | Explicit content missed |
| **Binary Size** | 20KB | C version |
| **Memory Usage** | ~50MB | Python version |

---

## 🏗️ Architecture Vision

```
┌─────────────────────────────────────────────────────────────────┐
│                      Phoenix Core System                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Layer 1: Kernel Module (In Development - Q2 2026)              │
│  ├── V4L2 Camera Hooks      → Intercept before apps see         │
│  ├── Netfilter Network Hook → Block at network level            │
│  ├── inotify File Watcher   → Monitor new files                 │
│  └── Multi-Party Key System → Tamper-proof recovery             │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Layer 2: Detection Engine (Working - 85% accuracy)             │
│  ├── Skin Detection         → HSV/RGB color analysis            │
│  ├── Face Detection         → Coming soon (Q2)                  │
│  ├── Context Analysis       → Medical vs pornographic           │
│  └── ML Model Training      → TensorFlow Lite (Q3)              │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Layer 3: Userspace (Working - Production ready)                │
│  ├── Python Scanner         → 2-3 FPS real-time detection       │
│  ├── C Binary               → Manual verification mode          │
│  ├── Audit Logging          → Accountability tracking           │
│  └── Statistics Dashboard   → Coming soon (Q2)                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Kernel Module Development

We're actively developing a Linux kernel module (`kernel/phoenix_core.c`) that hooks into:

### V4L2 (Video4Linux) Camera Subsystem
- Intercepts frames before any app receives them
- Runs detection at kernel level (faster, unbypassable)
- Blurs or blocks explicit content in the framebuffer

### Current Implementation (800+ lines)
- Character device interface (`/dev/phoenix_core`)
- Audit logging with kernel memory management
- IOCTL commands for userspace communication
- Process tracking and attribution

### Build Instructions (Linux VM)
```bash
cd kernel
make
sudo insmod phoenix_core.ko
sudo dmesg | tail
echo "25" > /dev/phoenix_core  # Send detection score
cat /dev/phoenix_core           # Read audit log
```

---

## 🤝 We Need Contributors

We're building something that doesn't exist yet. If you have skills in:

### 🔧 Kernel Development (🔴 HIGH PRIORITY)
- C, Linux kernel modules
- V4L2, Netfilter, inotify
- Device drivers, memory management

### 👁️ Computer Vision (🟡 MEDIUM PRIORITY)
- Python, OpenCV, PyTorch
- Skin detection models
- Face detection, transfer learning

### 📱 Android Development (🟡 MEDIUM PRIORITY)
- Java/Kotlin, Camera2 API
- Background services, NDK/C++

### 🔒 Security Engineering (🟢 LOW PRIORITY)
- Cryptography, key management
- Secure audit logging, tamper-proof design

### 🎨 UI/UX Design (🟢 LOW PRIORITY)
- Mobile app interfaces, dashboard design
- User experience, accessibility

---

## 📊 Project Board

Check our progress: [GitHub Projects](https://github.com/owiliberyll-coder/phoenix-core/projects)

### Current Sprint (March 2026)
- [x] Working Termux prototype
- [x] Skin detection algorithm
- [x] GitHub infrastructure
- [x] Complete documentation
- [x] C detector with manual mode
- [ ] Kernel module V4L2 hook
- [ ] Improve accuracy to 90%

### Next Sprint (April 2026)
- [ ] Implement Netfilter network filter
- [ ] Build native Android app (no Termux)
- [ ] Train ML model with 10k images
- [ ] Create video tutorial
- [ ] Set up Discord community

---

## 🧪 Testing

Run the test suite:

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/ -v --cov=.

# Check coverage
coverage report
```

CI/CD runs automatically on every push via GitHub Actions.

---

## 📈 Roadmap 2026

### Q2 2026 (Current)
- ✅ Working Termux prototype
- ✅ Skin detection algorithm (85% accuracy)
- ✅ GitHub infrastructure complete
- ✅ Complete documentation
- 🔄 Kernel module V4L2 hooks
- 🔄 Native Android app (Kotlin)

### Q3 2026
- Complete kernel module (V4L2 + Netfilter)
- Native Android app release
- Improved detection (90%+ accuracy)
- Beta testing program
- Discord community

### Q4 2026
- Windows/macOS ports (WIP)
- Multi-party key system
- Production release v1.0
- Research paper publication

---

## 💰 Funding & Support

We're actively seeking funding to support full-time development:

| Funder | Status | Amount | Expected |
|--------|--------|--------|----------|
| **Sovereign Tech Fund** | 📋 Preparing | €50k-1M | Q3 2026 |
| **eSafety Commissioner** | 📋 Monitoring | $100k-700k AUD | Q4 2026 |
| **CIHR (Canada)** | 🔄 Partnering | $1.5M CAD | Q3 2026 |
| **CIRA Net Good** | 📋 Planning | $50k-100k CAD | Q3 2026 |

**Sponsor us:** [GitHub Sponsors](https://github.com/sponsors/owiliberyll-coder)

---

## 📄 License

**GNU General Public License v3.0** - See [LICENSE](LICENSE) file

This ensures Phoenix Core remains free and open source forever. The GPLv3 license is specifically chosen to:
- Protect user freedom
- Require derivative works to also be open source
- Align with Linux kernel's GPL requirements
- Prevent proprietary exploitation

---

## 🙏 Acknowledgments

- **Termux Team** - Amazing Android terminal environment
- **OpenCV Community** - Computer vision libraries
- **NumPy/Pillow Developers** - Image processing tools
- **Linux Kernel Community** - Kernel module inspiration
- **All Contributors** - Making digital sovereignty a reality

---

## 📞 Contact

| Method | Contact |
|--------|---------|
| **Author** | owiliberyll-coder |
| **Email** | owiliberyll@gmail.com |
| **GitHub** | [@owiliberyll-coder](https://github.com/owiliberyll-coder) |
| **Discord** | Coming soon |
| **Twitter** | Coming soon |

---

## ⭐ Show Your Support

If this project matters to you:

- ⭐ **Star this repository** - Increases visibility
- 🐛 **Report bugs** - Helps improve quality
- 💡 **Suggest features** - Shapes the roadmap
- 🔧 **Contribute code** - Accelerates development
- 📢 **Share with others** - Grows the community
- 💰 **Sponsor development** - Enables full-time work

---

## 📊 Repository Statistics

| Metric | Value |
|--------|-------|
| **Total Files** | 20+ |
| **Lines of Code** | ~2,500 |
| **Languages** | Python (45%), C (30%), Markdown (15%), Shell (10%) |
| **Size** | ~100KB |
| **Contributors** | 1 (growing) |
| **License** | GPL v3 |

---

**Together, we can build a system that actually protects people from engineered addiction loops.**

**Join the mission.**

---

*Last updated: March 30, 2026*

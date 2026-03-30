#!/bin/bash
# Phoenix Core One-Click Installer for Termux

set -e

echo "🔥 Phoenix Core Installer"
echo "========================"
echo ""

if [ ! -d /data/data/com.termux ]; then
    echo "❌ This installer is for Termux on Android"
    exit 1
fi

echo "📦 Installing dependencies..."
pkg update -y
pkg install -y python python-pip termux-api git
pkg install -y python-numpy python-pillow

echo "🔐 Setting up permissions..."
termux-setup-storage
termux-camera-photo /sdcard/phoenix_test.jpg 2>/dev/null || true
rm -f /sdcard/phoenix_test.jpg

if [ -d ~/phoenix-core ]; then
    echo "🔄 Updating existing installation..."
    cd ~/phoenix-core
    git pull
else
    echo "📥 Cloning repository..."
    git clone https://github.com/owiliberyll-coder/phoenix-core.git ~/phoenix-core
    cd ~/phoenix-core
fi

echo "✅ Installation complete!"
echo ""
echo "To run: cd ~/phoenix-core && python fast_scanner.py"

# Cursor Trial Reset Tool

A utility tool designed to manage the Cursor editor's device identification system by resetting stored device IDs. This can assist users in resolving issues related to account restrictions when switching between accounts or during trial periods.

## ⚠️ Version Compatibility

> **IMPORTANT:** This tool currently supports:
> - ✅ Cursor v0.44.11 and below
> - ❌ Latest 0.45.x versions (temporarily unsupported)
>
> Please check your Cursor version before using this tool.

### Download Compatible Version
> 💾 **Cursor v0.44.11**
> - [Official Download](https://downloader.cursor.sh/builds/250103fqxdt5u9z/windows/nsis/x64)
> - [ToDesktop Mirror](https://download.todesktop.com/230313mzl4w4u92/Cursor%20Setup%200.44.11%20-%20Build%20250103fqxdt5u9z-x64.exe)

## Overview

This tool helps reset Cursor's free trial limitation when encountering the following message:
```
Too many free trial accounts used on this machine.
Please upgrade to pro. We have this limit in place
to prevent abuse. Please let us know if you believe
this is a mistake.
```

## ✨ Key Features

- Reset Cursor's trial limitations
- Automatic backup creation with timestamp
- Safe file operations with error handling
- Cross-platform compatibility

## 💻 System Requirements

### Supported Platforms
- Windows
- macOS
- Linux

### Prerequisites
- Python 3.7 or higher
- Administrator/root privileges

## 🚀 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yx-elite/cursor-limit-reset.git
cd cursor-limit-reset
```

2. Run the script:
```bash
python cursor_reset.py
```

> **Important:** Ensure Cursor is completely closed before running the script. If Cursor is running in the background, the reset will not be successful.

## 🔧 Technical Details

### Configuration File Locations

The script modifies Cursor's `storage.json` configuration file at:

- **Windows**: `%APPDATA%\Cursor\User\globalStorage\storage.json`
- **macOS**: `~/Library/Application Support/Cursor/User/globalStorage/storage.json`
- **Linux**: `~/.config/Cursor/User/globalStorage/storage.json`

### Modified Fields
The tool generates new unique identifiers for:
- `telemetry.machineId`
- `telemetry.macMachineId`
- `telemetry.devDeviceId`
- `telemetry.sqmId`

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is developed for educational purposes only. Use it at your own risk. The author is not responsible for any damage or issues caused by the use of this tool.
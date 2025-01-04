# Cursor Trial Reset Tool

A utility tool designed to manage the Cursor editor's device identification system by resetting stored device IDs. This can assist users in resolving issues related to account restrictions when switching between accounts or during trial periods.


## Description

This tool helps reset Cursor's free trial limitation when you encounter the following message:

```
Too many free trial accounts used on this machine.
Please upgrade to pro. We have this limit in place
to prevent abuse. Please let us know if you believe
this is a mistake.
```

## Key Features

- ✅ Reset Cursor's trial limitations
- ✅ Automatic backup creation with timestamp
- ✅ Safe file operations
- ✅ Error handling
- ✅ Cross-platform compatibility


## 💻 System Support

- **Windows**
- **macOS**
- **Linux**


## Installation & Usage

### Prerequisites
- Python 3.7 or higher
- Administrator/root privileges

### Quick Start

1. Clone the repository:

```bash
git clone https://github.com/yx-elite/cursor-limit-reset.git
cd cursor-limit-reset
```

2. Run the script in terminal/cmd:

```bash
python cursor_reset.py
```

**Important Note:** Before using the script, ensure that Cursor is completely closed. If Cursor is running in the background, the reset script will keep reverting, preventing you from successfully resetting the trial limit.

## Technical Details

### Configuration Files

The script modifies Cursor's `storage.json` configuration file located at:

- **Windows**: `%APPDATA%\Cursor\User\globalStorage\storage.json`
- **macOS**: `~/Library/Application Support/Cursor/User/globalStorage/storage.json`
- **Linux**: `~/.config/Cursor/User/globalStorage/storage.json`

### Modified Fields

The tool generates new unique identifiers for:
- `telemetry.machineId`
- `telemetry.macMachineId`
- `telemetry.devDeviceId`
- `telemetry.sqmId`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Important Notice

This tool is developed for educational purposes only. Use it at your own risk. The author is not responsible for any damage or issues caused by the use of this tool.

<div align="center">

<img src="https://img.shields.io/badge/Download%20sorter-CLI%20Tool-3776ab?style=for-the-badge&labelColor=0d1117" alt="Download Organizer" height="36"/>

<br/><br/>

<!-- VERSION_START -->
[![Version](https://img.shields.io/badge/Version-1.0.0-3776ab?style=flat-square)](https://github.com/Robotics-now/Download-Organizer/releases)
[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-GPL3.0-f59e0b?style=flat-square)](https://github.com/Robotics-now/Download-Organizer?tab=GPL-3.0-1-ov-file)
[![Platform](https://img.shields.io/badge/Platform-macOS%20Only-apple?style=flat-square)](#-compatibility)
<!-- VERSION_END -->

<br/>

**Automatically sort your Downloads folder · JSON-driven path mappings · Native macOS notifications · Zero third-party dependencies**
<br>
<br>
👉 **<a href="https://roboticsnow.dpdns.org/"> Visit our Official Website & Projects Showcase</a>**
<br/>

| |
| --- |
| <img src="https://avatars.githubusercontent.com/u/192281838?v=4" width="28" height="28" style="border-radius:50%;" align="center"> **[@Robotics-now](https://github.com/Robotics-now)** |

<br/>

[Quick Start](#-quick-start) · [Setup](#-setup) · [Features](#-features) · [Config Schema](#-config-schema) · [File Structure](#-file-structure)

</div>

---

## ⚡ Why Download Sorter?
Is your Download folder a chaotic mess of unorganized `.pdf`, `.mp4`, `.zip`, and `.png` files cluttering up your system's download folder? 

Download Sorter is a lightweight macOS (more platforms comming soon) tool built for Python 3.10+ that instantly categorizes incoming files into custom directories based on a simple Python script that uses a JSON file to sort items into respective locations — complete with native AppleScript notifications and duplicate file protection. It also uses no external libraries and therefore is extremly lightweight. 

---

## ✨ Features

| Feature | Description |
|---|---|
| 📂 **JSON Mapping** | Map any extension (`.mp4`, `.pdf`, `.zip`) to custom target paths in a single file |
| 🔔 **macOS Notifications** | Triggers native AppleScript banner notifications whenever files are organized |
| 🛡️ **Overwrite Guard** | Appends incremental counters (`file_1.pdf`) so your existing files are never lost |
| 📁 **Auto-Create Paths** | Creates destination directories on the fly if they don't already exist |
| 🪶 **Zero Dependencies** | Built using only standard Python 3.10+ modules (`pathlib`, `json`, `subprocess`) |
| 🎯 **Smart Normalization** | Handles both lowercase, uppercase, and missing dot formats (`"MP4"` vs `".mp4"`) |
| 🧹 **Clean Execution** | Silently skips hidden files, folders, and macOS system files (`.DS_Store`) |
| **Lightweight**| Main script is only 2 KB |

 
## 🚀 Quick Start
Start by first downloading python 3.10 or later form [python.org](https://www.python.org/downloads/) if you havent already. Then you can download the sorter.py script for your platform from the releases tab (windows comming soon) then plase it in a location along with the `config.json` file in the same directory. 

```json

//example
{
".mp4": "/Users/yourusername/Movies",
".pdf": "/Users/yourusername/Documents/PDFs",
".zip": "/Users/yourusername/Downloads/Archives",
".png": "/Users/yourusername/Pictures"
}

```

Run the organizer using Python 3.10+:

```bash
python3 sorter.py

```

You will see Terminal output detailing transferred files along with a native macOS notification banner:

```
Moved: document.pdf -> /Users/yourusername/Documents/PDFs/document.pdf
Moved: video.mp4 -> /Users/yourusername/Movies/video.mp4

```

> [!IMPORTANT]
> Make sure `config.json` is located in the exact same directory as `sorter.py` so the script can resolve configuration paths correctly.


## 📁 File Structure
```
Download-sorter/
├── config.json              # Extension mapping configuration
└── sorter.py    # Core macOS execution & AppleScript notification logic
```

## 📄 Config Schema

The script expects a plain JSON object with extension keys and macOS directory path values.

**File:** `config.json`

**Format:** `"extension": "absolute_target_path"`

```json
{
".mp4": "/Users/yourusername/Movies",
".mkv": "/Users/yourusername/Movies",
".pdf": "/Users/yourusername/Documents/PDFs",
".docx": "/Users/yourusername/Documents",
".zip": "/Users/yourusername/Archives",
".tar.gz": "/Users/yourusername/Archives"
}

```

- Extensions can be defined with or without a leading dot (`".pdf"` or `"pdf"`).
- Extensions are automatically converted to lowercase during parsing (`".PDF"` matches `.pdf`).
- Target paths support deep nesting (e.g., `/Users/username/Documents/Work/PDFs`) and auto-create missing folders.

## 🍎 Compatibility

- **OS:** macOS only (10.15 Catalina or newer recommended)
- **Python:** Python 3.10 or higher required
- **Dependencies:** None (uses built-in standard library)

## 📋 Quick Reference

| Parameter | Default |
| --- | --- |
| **Source Directory** | `~/Downloads` |
| **Config Location** | `./config.json` |
| **Python Version** | Python 3.10+ |
| **Notification Engine** | Native AppleScript (`osascript`) |
| **Security** | 100% offline & local processing |

### Releases version numbers

The first number is the major version, the second number is the feature update, and the third number represents minor bug fixes or patches.

**Built for developers who want an organized macOS workspace.** ---- Releases ----

## License

> **GPL 3.0 License**
>
> Copyright © 2026 Robotics-now
>
>

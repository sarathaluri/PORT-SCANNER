# ⚔️ Advanced Port Scanner (Python)

## 📌 Overview
A multi-threaded port scanner built in Python for network reconnaissance and security analysis.  
This tool identifies open ports, detects services, and performs banner grabbing to extract service and version information.

---

## 🚀 Features
- Multi-threaded scanning for faster performance
- Detection of open TCP ports
- Service identification (e.g., SSH, HTTP)
- Banner grabbing (service/version detection)
- Configurable port range
- Adjustable timeout and thread count
- CLI-based professional interface
- Export scan results to file

---

## 🛠️ Tech Stack
- Python
- Socket Programming
- Multithreading
- Argparse (CLI)

---

## ▶️ Usage

### Basic Scan
```bash
python scanner.py scanme.nmap.org

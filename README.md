# ⚔️ Advanced Port Scanner (Python)

## 📌 Overview
This project is a multi-threaded port scanner built in Python for network reconnaissance and security analysis.  
It scans a target system to identify open ports, detects running services, and performs banner grabbing to extract service and version information.

---

## 🚀 Features
- Multi-threaded scanning for high performance
- Detection of open TCP ports
- Service identification (e.g., HTTP, SSH)
- Banner grabbing for service/version detection
- Configurable port range
- Adjustable timeout and thread count
- Command-line interface (CLI)
- Optional result export to file

---

## 🛠️ Tech Stack
- Python
- Socket Programming
- Multithreading
- Argparse (CLI handling)

---

## ▶️ Usage

### 🔹 Basic Scan
```bash
python scanner.py scanme.nmap.org

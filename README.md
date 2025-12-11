Network Scanner Tool

A lightweight and practical Python network scanning tool designed for penetration testing, cybersecurity learning, and home lab analysis.

The tool performs:

Ping Sweeps → Discover active hosts

Port Scans → Detect open ports & services

Styled CLI Output → Clean tables using rich

Nmap Integration → Accurate network results


Features

🔍 1. Ping Sweep

Scan an entire subnet to identify devices online.

Example:

192.168.1.0/24

🔎 2. Port Scan

Scan the first 1024 ports of a target to reveal:

Open ports

Services

State (open / filtered / closed)

🎨 3. Styled Output

Powered by the rich library:

Color-coded info

Professional tables

Easy to read for reports

Requirements
✔ Python

Python 3.9 or higher

python --version

✔ Nmap

Download:
https://nmap.org/download.html

Verify Nmap:

nmap --version

✔ Python Libraries
pip install python-nmap rich

Project Structure
network-scanner/
│── scanner.py
│── README.md
│── requirements.txt
│── assets/
│     └── logo.png      ← your custom logo here
│── reports/            ← future reporting system

How to Run
python scanner.py


Menu shown:

Network Scanner Tool
1. Ping Sweep
2. Port Scan
Choose an option (1-2):

Example Output
Ping Sweep
Performing ping sweep on 192.168.43.0/24...
Live hosts found: 2
✔ 192.168.43.1
✔ 192.168.43.62

Port Scan
Open Ports on 192.168.43.62
┏━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ Port ┃ State    ┃ Service      ┃
┡━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│ 135  │ open     │ msrpc        │
│ 139  │ open     │ netbios-ssn  │
│ 445  │ open     │ microsoft-ds │
└──────┴──────────┴──────────────┘

requirements.txt
python-nmap
rich

Future Enhancements

🔹 Save results to JSON / HTML
🔹 Add OS detection
🔹 Add vulnerability checks
🔹 Add threaded scanning
🔹 Build a GUI version
🔹 Build a web dashboard version

Author

Prince Mokgwadi
Cybersecurity Projects

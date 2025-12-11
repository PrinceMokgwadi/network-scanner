Network Scanner Tool

A Python-based network scanning tool that performs:

Ping Sweep — detect active hosts on a network

Port Scan — discover open ports and running services

Uses Nmap for accurate scanning

Uses Rich for clean, styled CLI output

Features
1. Ping Sweep

Detect all live hosts in a given subnet.
Example input:

192.168.1.0/24

2. Port Scanning

Scan the first 1024 ports of any target IP and list:

Open ports

Service names

Port states (open, filtered, closed)

3. Styled Output

Uses rich to print clean tables and colored text.

Requirements
1. Python

Version 3.9 or newer recommended.
Check version with:

python --version

2. Nmap

Download and install from:
https://nmap.org/download.html

Ensure it is added to your PATH:

nmap --version

3. Python Packages

Install dependencies with:

pip install python-nmap rich

Project Structure
network-scanner/
│── scanner.py
│── README.md
│── requirements.txt
│── assets/
│     └── logo.png (optional)
│── reports/        (future use)

How to Run

Run the script with:

python scanner.py


You will see:

Network Scanner Tool
1. Ping Sweep
2. Port Scan
Choose an option (1-2):

Example Output
Ping Sweep Example
Performing ping sweep on 192.168.43.0/24...
Live hosts found: 2
✔ 192.168.43.1
✔ 192.168.43.62

Port Scan Example
Open Ports on 192.168.43.62
┏━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ Port ┃ State    ┃ Service      ┃
┡━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│ 135  │ open     │ msrpc        │
│ 139  │ open     │ netbios-ssn  │
│ 445  │ open     │ microsoft-ds │
└──────┴──────────┴──────────────┘

requirements.txt

Create a file named requirements.txt with:

python-nmap
rich

Future Enhancements (Optional)

Save scan results to HTML or JSON

Add multi-threading for speed

Add OS detection

Add vulnerability checks

Author

Prince Mokgwadi
Cybersecurity Projects

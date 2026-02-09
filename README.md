D4C PORT SCAN

Description

This Python script is a network tool that combines ping, port scanning, and SSH brute-forcing capabilities.

Important Notes

This tool is for educational and authorized testing purposes only.
Unauthorized use is illegal. Always have permission to scan and test systems.
The wordlists must be provided by the user. Example wordlists can be found online, but ensure you have the right to use them

Features

Ping a target IP address to check if it's alive.
Scan ports 1 to 100 on the target.
If port 22 (SSH) is open, attempt to brute-force SSH credentials using wordlists (user.txt and passwords.txt).
If successful, provide an interactive SSH session.

Prerequisites

Python 3.x
Libraries: tqdm, paramik

Installation

Install Python 3.x from python.org.
Install the required libraries using pip:
pip install -r requirements.txt

Usage

Run the script:
python D4C.py
Follow the prompts:
Enter the target IP address.
The script will ping the target and then scan ports 10-29.
If port 22 is found open, it will ask if you want to brute-force SSH.
If you choose 'y', it will attempt to log in using the wordlists

Disclaimer

The author is not responsible for any misuse of this tool. Use it ethically and legally.

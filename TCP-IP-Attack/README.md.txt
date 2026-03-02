""Overview""

This project is based on the SEEDLabs TCP/IP Attack Lab.
The purpose of this lab was to understand how TCP works and how it can be attacked in a controlled environment.

In this project, I performed several TCP-related attacks using Docker containers and Python with Scapy.

All experiments were done in a safe lab environment for educational purposes only.


""Lab Environment""

The lab was set up using Docker containers inside the SEED Ubuntu 20.04 VM.

Network configuration:

Attacker: 10.9.0.1

Victim (Telnet server): 10.9.0.5

User (Telnet client): 10.9.0.6

Network: 10.9.0.0/24

The attacker container was configured in host mode so it could sniff network traffic.


""Attacks Implemented""


1. SYN Flood Attack

Sent many spoofed SYN packets

Filled the victim’s half-open connection queue

Tested backlog size changes

Compared behavior with SYN cookies enabled


2. TCP RST Attack

Injected a forged RST packet

Terminated an active Telnet session


3. TCP Session Hijacking

Sniffed TCP session parameters

Injected malicious commands into an active session


4. Reverse Shell via Session Hijacking

Injected reverse shell command

Gained remote shell access to the victim machine


""Tools Used""

Python

Scapy

Docker

Netcat

Linux networking commands


""What I Learned""

How TCP 3-way handshake works

How half-open connections can be abused

Why correct sequence numbers are important

How TCP trusts packets without authentication

How SYN cookies protect against SYN flooding


""Disclaimer""

This project was completed in a controlled Ubuntu lab environment for learning purposes only.

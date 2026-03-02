""Goal""


The goal of this task was to perform a Denial-of-Service attack by flooding the victim with spoofed TCP SYN packets.

The idea is to fill the victim’s half-open connection queue so that legitimate users cannot connect.


""How It Works""

When a TCP connection starts:

Client sends SYN

Server replies with SYN-ACK

Client sends ACK

In a SYN flood attack, the attacker sends many SYN packets but never completes the handshake.

This causes many connections to stay in the SYN_RECV state.


""Observations""

The victim’s backlog queue filled up.

Telnet connections sometimes failed.

Reducing the backlog size made the attack more effective.

Enabling SYN cookies reduced the attack impact.



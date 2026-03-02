""Goal""

The goal of this task was to terminate an active Telnet session by injecting a forged TCP RST packet.


""How It Works""

TCP uses sequence numbers to track connections.
If a valid RST packet with the correct sequence number is received, the connection is immediately closed.


""Observations""

After sending the RST packet, the Telnet session closed instantly.

This shows that TCP does not verify the identity of the sender.

If the sequence number is wrong, the packet is ignored.
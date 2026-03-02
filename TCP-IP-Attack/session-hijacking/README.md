""Goal""

The goal of this task was to inject a malicious command into an active Telnet session.


""How It Works""

1. Sniff the TCP session.

2. Capture:

-Source IP

-Destination IP

-Source port

-Destination port

-Sequence number

-Acknowledgment number

3. Create a spoofed packet with correct values.

4. Inject a command into the session.


""Observations""

If the sequence number is correct, the command is executed.

If it is wrong, the packet is ignored.

TCP trusts packets that match session parameters.

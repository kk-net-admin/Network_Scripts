import subprocess
import ipaddress

subnet = ipaddress.ip_network(input("What IP subnet do you want to ping (In a X.X.X.X/X format)"))

for ip in subnet:
    pingcmd = subprocess.run(["ping","-n","1","-w","500",str(ip)],stdout=subprocess.DEVNULL)
    if pingcmd.returncode == 0:
        print (ip,"is active")
    else:
        print (ip,"is inactive")
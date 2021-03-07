import sys
import socket
from termcolor import colored

ip_address = sys.argv[1]

for ports in range(1, 65535):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   if s.connect_ex((ip_address, ports)) == 0:
      print(colored(f"[+] PORT {ports} OPEN", "green"))
      s.close()
   else:
      print(colored(f"[-] PORT {ports} CLOSED", "red"))
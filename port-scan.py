import socket
from colorama import Fore, init, Style # type: ignore
import argparse
from typing import List


class PortScan(object):
   def __init__(self, ports: int = 65535, /) -> None:
      self.ports = ports
      
   
   def verify_ports(self, ip_address: str) -> None:
      socket.setdefaulttimeout(0.5)
      for port in range(1, self.ports):
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         if s.connect_ex((ip_address, port)) == 0:
            print(Fore.GREEN + f"[+] {port} OPEN")
            s.close()
         else:
            print(Fore.RED + f"[-] {port} CLOSED")
            
            
   def get_arguments(self, /) -> str:
      parser = argparse.ArgumentParser()
      parser.add_argument("-ip", dest="ip", help="Enter with the ip address")
      options = parser.parse_args()
      if not options.ip:
         options.ip = str(input("[+] IP Address: "))
      return options.ip
         
   
   def start(self, /) -> None:
      ip_address = self.get_arguments()
      self.verify_ports(ip_address)
      

if __name__ == "__main__":
   init(autoreset=True)
   scan = PortScan()
   scan.start() 
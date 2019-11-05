#!/usr/bin/env python
#!Developer: BetterOffGone
#!Website : http://insanitysecurityteam.co.uk
#!Twitter : http://twitter.com/OVHBypass
#!Note: Please Ensure To Give Credit To The Developer If You Change This Up.
import socket 
import sys, time
from datetime import datetime
import threading
import os
import getpass

open_ports = ['[*] List of Open Ports']
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
print "-" * 43
print "---------------Insanity Portscan-----------"
print "----------For Educational Research---------" * 1
print "----------------Purposes Only--------------" * 1
print "-" * 43
print "[*] Welcome To Insanity Portscan"
ip = raw_input("[*] Enter IP/Domain: ")

target = socket.gethostbyname(ip)
targetip = socket.gethostbyname(target)
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
print "-" * 43
print "---------------Insanity Portscan-----------"
print "----------For Educational Research---------" * 1
print "----------------Purposes Only--------------" * 1
print "-" * 43
print "[*] Welcome To Insanity Portscan"
print("[*] Selected Target: %s "% target)
print("[*] Target's IP Address: %s" % targetip)
print("[*] Date: %s" % (time.strftime("%A %d %B %Y")))
print("[*] Scan Started: %s\n"%(time.strftime("%H:%M:%S%p")))
start = datetime.now()
def check(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        open_ports.append(str(port))
        sock.close()
    except socket.error:
        pass
    return

for i in range(0, 65355):
    sys.stdout.write("\r[*] Probing Port: %s" % (i))
    thread = threading.Thread(target=check, args=(i,))
    thread.start()
    
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
print "-" * 43
print "---------------Insanity Portscan-----------"
print "----------For Educational Research---------" * 1
print "----------------Purposes Only--------------" * 1
print "-" * 43
print("[*] Scan Completed")
print "[*] Getting Port Results"
thread.join()
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
print "-" * 43
print "---------------Insanity Portscan-----------"
print "----------For Educational Research---------" * 1
print "----------------Purposes Only--------------" * 1
print "-" * 43    
print "[*] Port Results For: %s" % target
print ""
print("\n[+] Open Port: ".join(open_ports))
stop = datetime.now()
total = stop - start
print("\n[*] Scan Finished: %s" % (time.strftime("%H:%M:%S%p")))
print("[*] Date: %s" % (time.strftime("%A %d %B %Y")))
print("[*] Scan Duration: %s" % (total))
print ""
print("Thank you for using Insanity Portscan")
print("Developer: BetterOffGone\nWebsite: http://insanitysecurityteam.co.uk\nTwitter: http://twitter.com/OVHBypass")

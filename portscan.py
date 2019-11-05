#!/usr/bin/env python
#!Developer: BetterOffGone
#!Website : http://insanitysecurityteam.co.uk
#!Twitter : http://twitter.com/OVHBypass
#!Note: Please Ensure To Give Credit To The Developer If You Change This Up.
import sys
import socket
import threading
import os
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
ip = raw_input("[*] Enter IP/Domain: ")

host = socket.gethostbyname(ip)
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
print "-" * 43
print "---------------Insanity Portscan-----------"
print "----------For Educational Research---------" * 1
print "----------------Purposes Only--------------" * 1
print "-" * 43
print "[*] Portscanning:", host
def check(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        open_ports.append(str(port))
        sock.close()
    except socket.error:
        pass
    return

for i in range(0, 65355):
    sys.stdout.write("\r[*] Checking Port: %s" % (i))
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
print "[*] Getting Port Results For:", host
print("[*] Scan Completed")
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
print "[*] Port Results For:", host
print ""
print("\n[+] Open Port: ".join(open_ports))
print("\n")
print("Thank you for using Insanity Portscan")
print("Developer: BetterOffGone\nWebsite: http://insanitysecurityteam.co.uk\nTwitter: http://twitter.com/OVHBypass")
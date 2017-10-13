#!python
import socket
import subprocess
import sys

from datetime import datetime

#clear the screen
subprocess.call('clear',shell=True)

#How to use
print "-" * 60
print "# HOW TO USE" + " " * 47 + "#"
print "# $python xaqmap.py" + " " * 40 + "#"
print "# host :127.0.0.1" + " " * 42 + "#"
print "# range scan port from : 0" + " " * 33 + "#"
print "# range scan port to : 1000" + " " * 32 + "#"
print "-" * 60

#input
remoteServer = raw_input("host :")
remoteServerIP = socket.gethostbyname(remoteServer)
remotePort = int (raw_input ("range scan port from : "))
remotePort2 = int (raw_input ("range scan port to : "))

#print banner
print ""
print ""
print "=" * 60
print "scan IP ", remoteServerIP
print "=" * 60
print ""

#start checking time
firstTime=datetime.now()


#scan
try:
    for port in range(remotePort,remotePort2):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP,port))
        if result == 0:
            print "Port {} Open".format(port) + " " ,(sock.recv(1024))
            sock.close()
except KeyboardInterrupt:
        print "You stoped it"
        sys.exit()

except socket.gaierror :
        print "hostname couldn't be resolved"
        sys.exit()

#last checking time
lastTime= datetime.now()

#Time to scan
total =lastTime - firstTime

#printing
print 'Scan completed in :',total
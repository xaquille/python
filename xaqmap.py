#!python
import socket
import subprocess
import sys

from datetime import datetime

#clear the screen
subprocess.call('clear',shell=True)

#input
remoteServer = raw_input("host :")
remoteServerIP = socket.gethostbyname(remoteServer)
remotePort = int (raw_input ("range scan port from : "))
remotePort2 = int (raw_input ("range scan port to : "))

#print banner
print "=" * 60
print "please wait", remoteServerIP
print "=" * 60

#start checking time
firstTime=datetime.now()

#scan
try:
    for port in range(remotePort,remotePort2):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP,port))
        #banner = sock.recv(1024)
        if result == 0:
            print "Port {}:Open".format(port)
            sock.close()
except KeyboardInterruptet :
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
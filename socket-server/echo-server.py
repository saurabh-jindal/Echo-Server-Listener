#!/usr/bin/env py 

import socket 
import sys

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = input("Enter the port you want to listen on....")
tcpSocket.bind(("0.0.0.0", port))

con = input("Enter the number of connection you want....")
tcpSocket.listen(con)
(client, (ip,sock)) = tcpSocket.accept()

while client:
	print 'Got a connection from '+ip
	data = "Hi there!"
	while data:
		client.send(data)
		client.send("Enter something you want to send...")
		data = client.recv(2048)
		print data
		data = raw_input("Enter something you want to send!")
	(client, (ip,sock)) = tcpSocket.accept()	
	



print "Closing connection....."
client.close()


print "Closing Socket!"

tcpSocket.close()	
import socket

def connect():
	file=open("proxy.txt","r")
	content=file.read()
	content=content.rstrip("\n")
	ip,port=tuple(content.split())
	port=int(port)

	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect((ip,port))
	return sock

def disconnect(sock):
	sock.close()

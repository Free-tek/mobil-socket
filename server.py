import socket
import sys
from datetime import datetime

#fuser -k 9999/tcp

def create_socket():
	try:
		global host
		global port
		global s
		host = ""
		port = 9999
		s = socket.socket()

	except socket.error as message:
		print(f"socket creation error: {message}")


#bind socket and listening for connections
def bind_socket():
	try:
		global host
		global port
		global s

		print(f"binding the Port: {port}")

		s.bind((host,port))
		s.listen(5)

	except socket.error as message:
		bind_socket()
		print(f"socket binding error: {message} \n Retrying:")


#accept connection after listening
def socket_accept():
	connection, address = s.accept()
	print(f"Connection established from IP: {address[0]} and port {address[1]}")
	recieve_data(connection, address)
	#send_command(connection)
	#connection.close()

def recieve_data(connection, address):
	client_response = str(connection.recv(1024),"utf-8")

	now = datetime.now()
	current_time = now.strftime("%Y-%m-%d %H:%M:%S")

	f = open("streams.txt", "a")
	f.write(f"Time: {current_time} \n")
	f.write(f"Connection established from IP: {address[0]} and port: {address[1]} \n")
	f.write(f"Message: {client_response} \n")
	f.write(f"\n")
	f.close()


	print(f"{client_response}")
	connection.close()
	socket_accept()
			
	
		
def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
















import socket
import sys

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
	recieve_data(connection)
	#send_command(connection)
	#connection.close()

def recieve_data(connection):
	client_response = str(connection.recv(1024),"utf-8")
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
















import socket
from json import loads, dumps

def main():
    host = '127.0.0.1'  # Localhost
    port = 12345  # Same port as server

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while(True):
        message = input("Enter a string to send to the server: ")
        message2=input("enter other string: ")

        client_socket.send(dumps([message,message2]).encode())  # Send the string to the server

        result = loads(client_socket.recv(1024).decode())  # Receive the elaborated result from the server
        print("Elaborated result from server:", result)

if __name__ == "__main__":
    main()

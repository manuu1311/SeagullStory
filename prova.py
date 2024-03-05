import socket
from json import loads,dumps

def elaborate_string(input_string):
    for string in input_string:print(string)
    return 'got it'

def main():
    host = '127.0.0.1'  # Localhost
    port = 12345  # Arbitrary non-privileged port

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for a single connection

    conn, addr = server_socket.accept()

    while True:
        data = conn.recv(1024).decode()  # Receive data from the client
        if not data:
            break
        data=loads(data)

        print("Received data:", data)

        result = elaborate_string(data)
        conn.send(dumps(result).encode())  # Send the elaborated result back to the client


if __name__ == "__main__":
    main()

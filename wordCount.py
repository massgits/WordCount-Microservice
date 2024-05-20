import socket

with socket.socket() as server_socket:
    server_socket.bind(('localhost', 4547))
    server_socket.listen(1)
    print("Server is listening on port 4547...")

    while True:
        connection, _ = server_socket.accept()
        with connection:
            data = connection.recv(1024)
            if data:
                print("Request received from main program.")                    # this line was just for Assignment 8, and can be deleted
                print(f'Sending word count for string: {data}')                 # this line was just for Assignment 8, and can be deleted
                connection.sendall(str(len(data.decode().split())).encode())
# WordCount-Microservice
## How to Programmatically Request Data
### The microservice uses TCP Sockets as the communication pipeline, users of the service must import socket to their main program and create a socket for it. The microservice runs locally and is set to listen for requests on port 4547, although this can be modified to another port number, if preferred. To request data, the main program must create a connection and send the request. Example below:
> __with socket.create_connection(('localhost', 4547)) as client_socket:
> &emsp;client_socket.send(string.encode())__
## How to Programmatically Receive Data
### In order to recieve data from the microservice, you must specify the socket where the microservice is to return the data. Presently, the microservice is set to return data to 1024. Example below:
> __received_data = client_socket.recv(1024).decode()__
## UML Sequence Diagram
### ![image](https://github.com/massgits/WordCount-Microservice/assets/122513510/9d13dc06-42b6-4e9b-b9f6-95051e675937)

import socket

class server:
    def __init__(self,host,port,max_connections,max_bytes):
        self.HOST = host
        self.PORT = port
        self.MAX_CONNECTIONS = max_connections
        self.MAX_BYTES = max_bytes

    def accept_connections(self):
        # create the socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen(self.MAX_CONNECTIONS)

        print("Online Server")
        (self.client_socket, self.address) = self.server_socket.accept()
        print("Connected\n")

    def send_mesage(self, mesage):
        self.client_socket.send(mesage.encode())
        print("Mesage Sent: ", mesage) 
    
    def receive_mesage(self):
        print("Waiting for data...\n")
        receive = self.client_socket.recv(self.MAX_BYTES)
        mesage = receive.decode() 
        print("Received mesage: ", mesage)
        return mesage

    def close_connection(self):
        self.server_socket.close()
    
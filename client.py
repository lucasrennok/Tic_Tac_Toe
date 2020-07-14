import socket

class client:
    def __init__(self, host_server, port_server, max_bytes):
        self.HOST_SERVER = host_server
        self.PORT_SERVER = port_server
        self.MAX_BYTES = max_bytes

    def connect_to_server(self):
        # create the socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.HOST_SERVER, self.PORT_SERVER))

        # create the socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.client_socket.connect((self.HOST_SERVER,self.PORT_SERVER))
        print("Connected\n")
        
    def send_mesage(self,mesage):
        self.client_socket.send(mesage.encode()) 
        print("Mesage Sent: ", mesage) 

    def receive_mesage(self):
        print("Waiting for data...\n")
        receive = self.client_socket.recv(self.MAX_BYTES)
        mesage = receive.decode() 
        print("Received mesage: ", mesage)
        return mesage

    def close_connection(self):
        self.client_socket.close()
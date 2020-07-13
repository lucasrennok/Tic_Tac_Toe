from server import server
from client import client

class multiplayer:
    def __init__(self, host_server, port_server, max_connections, max_bytes):
        self.server = server("",port_server,max_connections,max_bytes)
        self.client = client(host_server,port_server)

    def start_server(self):
        self.server.accept_connections()

    def server_receive_mesage(self):
        mesage = self.server.receive_mesage()
        return mesage

    def start_client(self):
        self.client.connect_to_server()

    def client_send_mesage(self):
        mesage = input("coordinate: ")
        self.client.send_mesage(mesage)
        return mesage

    def close_multiplayer(self):
        self.server.close_connection()
        self.client.close_connection()
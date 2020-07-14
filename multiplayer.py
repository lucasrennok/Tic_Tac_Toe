from server import server
from client import client

class multiplayer:
    def __init__(self, host_server, port_server, max_connections, max_bytes, first):
        self.first = first
        if(first=='1'):
            self.server = client(host_server,port_server, max_bytes)
        else:
            self.server = server("",port_server,max_connections,max_bytes)
        
    def start_server(self):
        self.server.accept_connections()

    def any_receive_mesage(self):
        mesage = self.server.receive_mesage()
        return mesage

    def start_client(self):
        self.server.connect_to_server()

    def any_send_mesage(self):
        mesage = input("coordinate: ")
        self.server.send_mesage(mesage)
        return mesage

    def close_multiplayer(self):
        self.server.close_connection()
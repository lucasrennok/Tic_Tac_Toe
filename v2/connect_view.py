
import PySimpleGUI as sg
from multiplayer import multiplayer
from tictactoe import TicTacToe
import time

class ConnectView:
    def __init__(self, play_first, game):
        self.play_first = play_first
        self.game = game
        #layout
        if(play_first==True):
            layout = [
                [sg.Text("Type your friend's IP", key="text")],
                [sg.Input(key="ip", size=(15,0))],
                [sg.Button("Connect", key="start")]
            ]
        elif(play_first==False):
            layout = [
                [sg.Text("Start Server", key="text")],
                [sg.Button("Create", key="start")]
            ]
        #window
        self.window = sg.Window('Tic Tac Toe Game').layout(layout)

    def get_multiplayer_data(self):
        self.HOST = ""
        if(self.play_first):
            self.button, self.data = self.window.Read()
            self.HOST = self.data["ip"]
            self.multiplayer = multiplayer(self.HOST,1500,3,1024,self.play_first,self.game)
        else:
            self.multiplayer = multiplayer(self.HOST,1500,3,1024,self.play_first,self.game)
        return self.HOST

    def stablish_connection(self):
        if(self.multiplayer.get_play_first()==False):
            self.button, self.data = self.window.Read()
            self.multiplayer.start_server()
            self.window.finalize()
            self.window.FindElement("text").Update("Connected!")
            self.window.FindElement("start").Update("Starting", disabled=True)
            mesage = self.multiplayer.any_receive_mesage()
            self.multiplayer.close_multiplayer()
            return mesage
        elif(self.multiplayer.get_play_first()==True):
            self.multiplayer.start_client()
            self.window.finalize()
            self.window.FindElement("ip").Update("OK", disabled=True)
            self.window.FindElement("text").Update("Connected!")
            self.window.FindElement("start").Update("Starting",disabled=True)
            mesage = self.multiplayer.any_send_mesage(0,0)
            self.multiplayer.close_multiplayer
            return mesage
        else:
            return None

    def close_window(self):
        self.window.close()
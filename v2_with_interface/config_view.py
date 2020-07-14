#Imports
import PySimpleGUI as sg
from tictactoe import TicTacToe

class ConfigScreen:
    def __init__(self, online):
        layout = ""
        self.online = online
        #layout
        if(online==0):
            layout = [
                [sg.Text('You will play:'),sg.Radio('Solo', 'players', key='solo', default=True), sg.Radio('With a Friend', 'players', key='duo')],
                [sg.Text('Want to be the first?'), sg.Radio('Yes', 'play-first', key='player1', default=True), sg.Radio('No', 'play-first', key='player2')],
                [sg.Button('Confirm')]
            ]
        elif(online==1):
            layout = [
                [sg.Text('Select')],
                [sg.Radio('Create a game', 'optgame', key='create'), sg.Radio('Connect to a game', 'optgame', key='connect', default=True)],
                [sg.Button('Confirm Option')]
            ]
        #window
        self.window = sg.Window('Tic Tac Toe Config').layout(layout)
        #data extract
        self.button, self.data = self.window.Read()

    def get_config(self):
        print(self.data)
        game = ""
        if(self.online==0):
            one_player = self.data['solo']
            play_first = self.data['player1']
            if(one_player==True):
                game = TicTacToe(1,play_first,False)
            elif(one_player==False):
                game = TicTacToe(2,play_first,False)
            else:
                game = None
        elif(self.online==1):
            create = self.data['create']
            connect = self.data['connect']
            if(create==True):
                game = TicTacToe(2,False,True)
            elif(connect==True):
                game = TicTacToe(2,True,True)
            else:
                game = None
        return game

    def close_window(self):
        self.window.close()



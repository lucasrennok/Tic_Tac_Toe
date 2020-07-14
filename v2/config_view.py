#Imports
import PySimpleGUI as sg
from tictactoe import TicTacToe

class ConfigScreen:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('You will play:'),sg.Radio('Solo', 'players', key='solo', default=True), sg.Radio('With a Friend', 'players', key='duo')],
            [sg.Text('Want to be the first?'), sg.Radio('Yes', 'play-first', key='player1', default=True), sg.Radio('No', 'play-first', key='player2')],
            [sg.Button('Confirm')]
        ]
        #window
        self.window = sg.Window('Tic Tac Toe Config').layout(layout)
        #data extract
        self.button, self.data = self.window.Read()

    def get_config(self):
        print(self.data)
        one_player = self.data['solo']
        play_first = self.data['player1']
        if(one_player==True):
            game = TicTacToe(1,play_first)
        elif(one_player==False):
            game = TicTacToe(2,play_first)
        else:
            game = None
        return game

    def close_window(self):
        self.window.close()



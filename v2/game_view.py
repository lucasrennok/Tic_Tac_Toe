#Imports
import PySimpleGUI as sg
from tictactoe import TicTacToe
from random import randint

class GameScreen():
    def __init__(self, game):
        #layout
        layout = [
            [sg.Text("Choose a coordinate")],
            [sg.Text("x:"),sg.Input(key="x",size=(3,0)),sg.Text("y:"),sg.Input(key="y",size=(3,0))],
            [sg.Button("0", key="1", size=(2,0),pad=((35,0),0)),sg.Button("0", key="2", size=(2,0),pad=((0,0),0)),sg.Button("0", key="3", size=(2,0),pad=((0,35),0))],
            [sg.Button("0", key="4", size=(2,0),pad=((35,0),0)),sg.Button("0", key="5", size=(2,0),pad=((0,0),0)),sg.Button("0", key="6", size=(2,0),pad=((0,35),0))],
            [sg.Button("0", key="7", size=(2,0),pad=((35,0),0)),sg.Button("0", key="8", size=(2,0),pad=((0,0),0)),sg.Button("0", key="9", size=(2,0),pad=((0,35),0))]
        ]
        #window
        self.window = sg.Window('Tic Tac Toe Game').layout(layout)
        #data extract
        self.game = game
        self.play_first = game.get_play_first()

    def play(self):
        self.game.set_game_view(self)
        num_players = self.game.get_num_players()
        if(num_players==1 and self.play_first==False):
            x = randint(0,2)
            y = randint(0,2)
            self.game.writeInCoordinate(2,x,y)

        print(self.game)
        finished = 4
        while(finished==4 or finished==-1):
            #read data
            self.button = self.window.FindElement('1')
            self.button, self.data = self.window.Read()
            
            print('teste')

            player = self.game.get_actual_player()
            
            # button data
            x = self.data['x']
            y = self.data['y']

            finished = self.game.writeInCoordinate(int(player),int(x),int(y))

            if(finished==4):
                if(num_players==1):
                    x = randint(0,2)
                    y = randint(0,2)
                    finished = self.game.writeInCoordinate(2,x,y)
                    while(finished==-1):
                        x = randint(0,2)
                        y = randint(0,2)
                        finished = self.game.writeInCoordinate(2,x,y)
                        self.game.set_actual_player(1)

            print(self.game)
            
        return finished

    def close_window(self):
        self.window.close()

    def buttonLock(self,number_button,player):
        self.window.FindElement(number_button).Update(str(player), disabled=True)

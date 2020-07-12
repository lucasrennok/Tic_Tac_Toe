#Imports
import PySimpleGUI as sg
from tictactoe import TicTacToe
from random import randint

class GameScreen():
    def __init__(self, game):
        #layout
        layout = [
            [sg.Text("Game", key='players')],
            [sg.Text("x:"),sg.Input(key="x"),sg.Text("y:"),sg.Input(key="y")],
            [sg.Button("Confirm")],
            [sg.Output(size=(30,20), key="output")]
        ]
        #window
        self.window = sg.Window('Game').layout(layout)
        #data extract
        self.game = game
        self.play_first = game.get_play_first()

    def play(self):
        num_players = self.game.get_num_players()
        if(num_players==1 and self.play_first==False):
            x = randint(0,2)
            y = randint(0,2)
            self.game.writeInCoordinate(2,x,y)

        print(self.game)
        finished = 4
        while(finished==4 or finished==-1):
            #read data
            self.button, self.data = self.window.Read()
            
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

            self.window.FindElement("output").Update("")
            print(self.game)
            
        return finished


    def close_window(self):
        self.window.close()
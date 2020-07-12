#Imports
import PySimpleGUI as sg
from tictactoe import TicTacToe
from random import randint

class GameScreen():
    def __init__(self, game):
        #layout
        layout = [
            [sg.Text("Choose a coordinate")],
            [sg.Button("0,0", key="b1", size=(2,0),pad=((35,0),0)),sg.Button("0,1", key="b2", size=(2,0),pad=((0,0),0)),sg.Button("0,2", key="b3", size=(2,0),pad=((0,35),0))],
            [sg.Button("1,0", key="b4", size=(2,0),pad=((35,0),0)),sg.Button("1,1", key="b5", size=(2,0),pad=((0,0),0)),sg.Button("1,2", key="b6", size=(2,0),pad=((0,35),0))],
            [sg.Button("2,0", key="b7", size=(2,0),pad=((35,0),0)),sg.Button("2,1", key="b8", size=(2,0),pad=((0,0),0)),sg.Button("2,2", key="b9", size=(2,0),pad=((0,35),0))]
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
            button, self.data = self.window.Read()

            player = self.game.get_actual_player()

            x = 0
            y = 0

            if(button=="b1"):
                x = 0
                y = 0
            elif(button=="b2"):
                x = 0
                y = 1
            elif(button=="b3"):
                x = 0
                y = 2
            elif(button=="b4"):
                x = 1
                y = 0
            elif(button=="b5"):
                x = 1
                y = 1
            elif(button=="b6"):
                x = 1
                y = 2
            elif(button=="b7"):
                x = 2
                y = 0
            elif(button=="b8"):
                x = 2
                y = 1
            elif(button=="b9"):
                x = 2
                y = 2
            else:
                return 0

            finished = self.game.writeInCoordinate(int(player),x,y)

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

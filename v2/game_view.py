#Imports
import PySimpleGUI as sg
from tictactoe import TicTacToe
from random import randint
from multiplayer import multiplayer

class GameScreen:
    def __init__(self, game):
        #layout
        if(game.online==True):
            layout = [
                [sg.Text("Player 1 Starts", key="text", size=(18,0))],
                [sg.Button(" ", key="b1", size=(2,0),pad=((40,0),0)),sg.Button(" ", key="b2", size=(2,0),pad=((0,0),0)),sg.Button(" ", key="b3", size=(2,0),pad=((0,35),0))],
                [sg.Button(" ", key="b4", size=(2,0),pad=((40,0),0)),sg.Button(" ", key="b5", size=(2,0),pad=((0,0),0)),sg.Button(" ", key="b6", size=(2,0),pad=((0,35),0))],
                [sg.Button(" ", key="b7", size=(2,0),pad=((40,0),0)),sg.Button(" ", key="b8", size=(2,0),pad=((0,0),0)),sg.Button(" ", key="b9", size=(2,0),pad=((0,35),0))]
            ]
        else:
            layout = [
                [sg.Text("Choose a coordinate", key="text")],
                [sg.Button(" ", key="b1", size=(2,0),pad=((35,0),0)),sg.Button(" ", key="b2", size=(2,0),pad=((0,0),0)),sg.Button(" ", key="b3", size=(2,0),pad=((0,35),0))],
                [sg.Button(" ", key="b4", size=(2,0),pad=((35,0),0)),sg.Button(" ", key="b5", size=(2,0),pad=((0,0),0)),sg.Button(" ", key="b6", size=(2,0),pad=((0,35),0))],
                [sg.Button(" ", key="b7", size=(2,0),pad=((35,0),0)),sg.Button(" ", key="b8", size=(2,0),pad=((0,0),0)),sg.Button(" ", key="b9", size=(2,0),pad=((0,35),0))]
            ]
        
        #window
        self.window = sg.Window('Tic Tac Toe Game').layout(layout)
        #data extract
        self.game = game
        self.play_first = game.get_play_first()
        

    def play(self):
        self.game.set_game_view(self)
        num_players = self.game.get_num_players()

        self.window.finalize()
        if(num_players==1 and self.play_first==False):
                x = randint(0,2)
                y = randint(0,2)
                self.game.writeInCoordinate(2,x,y)

        print(self.game)
        finished = 4
        while(finished==4):
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
                return None

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

    def play_online(self, host_ip):
        self.game.set_game_view(self)
        instances_server_cliente = multiplayer(host_ip,1500,3,1024,self.game.get_play_first(),self.game)
        if(self.game.get_play_first()==False):
            instances_server_cliente.start_server()
        elif(self.game.get_play_first()==True):
            instances_server_cliente.start_client()
        self.game.set_actual_player(1)
        finished=4
        while(finished==4):
            first = self.game.get_play_first()
            x = 0
            y = 0
            if(first):
                button, self.data = self.window.Read(close=False)
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
                    instances_server_cliente.any_send_mesage(-1,-1)
                    return None
                finished = self.game.writeInCoordinate(self.game.get_actual_player(),x,y)
                if(self.game.get_actual_player()==1):
                    player_round = "Wait Player 1"
                else:
                    player_round = "Wait Player 2" 
                self.window.FindElement("text").Update(player_round)
                instances_server_cliente.any_send_mesage(x,y)
                self.game.set_play_first(False)
            else:
                self.window.finalize()
                self.window.FindElement("text").Update("Choose a coordinate")
                received = instances_server_cliente.any_receive_mesage()
                mesage = int(received)
                if(mesage>=7):
                    x = 2
                    y = mesage-7
                elif(mesage>=4):
                    x = 1
                    y = mesage-4
                elif(mesage>=1):
                    x = 0
                    y = mesage-1
                else:
                    return None
                finished = self.game.writeInCoordinate(self.game.get_actual_player(),x,y)
                self.game.set_play_first(True)
        instances_server_cliente.close_multiplayer()
        return finished

    def close_window(self):
        self.game.reset_game()
        self.window.close()

    def buttonLock(self,number_button,player):
        self.window.FindElement(number_button).Update(str(player), disabled=True)

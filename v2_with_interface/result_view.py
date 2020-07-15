#Imports
import PySimpleGUI as sg

class ResultScreen:
    def __init__(self, result):
        if(result==1):
            who_won = "*Player One Won*"
        elif(result==2):
            who_won = "*Player Two Won*"
        elif(result==3):
            who_won = "*Computer Won*"
        elif(result==0):
            who_won = "*Nobody Won*"
        #layout
        layout = [
            [sg.Text(who_won)],
            [sg.Button('Quit', key="quit"),sg.Button('Play More', key="more")]
        ]
        #window
        self.window = sg.Window('End Window').layout(layout)
        
    def more_games(self):
        #read data
        self.button, self.data = self.window.Read()
        if(self.button=='more'):
            return 1
        else:
            return 0 

    def close_window(self):
        self.window.close()
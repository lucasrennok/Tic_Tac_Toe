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
            [sg.Button('Ok')]
        ]
        #window
        self.window = sg.Window('End Window').layout(layout)
        #read data
        self.button, self.data = self.window.Read()


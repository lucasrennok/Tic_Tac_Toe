#Imports
import PySimpleGUI as sg

class MenuScreen:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Tic Tac Toe Game')],
            [sg.Radio('Offline', 'multiplayer', key='off', default=True), sg.Radio('Online', 'multiplayer', key='on')],
            [sg.Button('Play')]
        ]
        #window
        self.window = sg.Window('Tic Tac Toe Config').layout(layout)
        #data extract
        self.button, self.data = self.window.Read()

    def get_config(self):
        print(self.data)
        off = self.data['off']
        on = self.data['on']
        if(off==True):
            return "offline"
        elif(on==True):
            return "online"
        else:
            return None
        

    def close_window(self):
        self.window.close()



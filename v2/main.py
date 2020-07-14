#Imports
import re
from config_view import ConfigScreen
from game_view import GameScreen
from tictactoe import TicTacToe
from result_view import ResultScreen

#Main
def main():
    more_games = 1
    while(more_games==1):
        config_window = ConfigScreen()
        game = config_window.get_config()
        if(game==None):
            break
        config_window.close_window()

        game_window = GameScreen(game)
        result = game_window.play()
        if(result==None):
            break
        game_window.close_window()

        del config_window
        del game_window

        result_window = ResultScreen(result)
        more_games = result_window.more_games()

        del result_window
        

#The program start here
main()
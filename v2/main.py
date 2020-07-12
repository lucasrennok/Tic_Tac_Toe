#Imports
import re
from config_view import ConfigScreen
from game_view import GameScreen
from tictactoe import TicTacToe
from result_view import ResultScreen

#Main
def main():
    config_window = ConfigScreen()
    game = config_window.get_config()
    config_window.close_window()

    game_window = GameScreen(game)
    result = game_window.play()
    game_window.close_window()

    del config_window
    del game_window

    result_window = ResultScreen(result)

    del result_window
        

#The program start here
main()
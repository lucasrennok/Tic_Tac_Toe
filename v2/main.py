#Imports
import re
import time
from config_view import ConfigScreen
from game_view import GameScreen
from tictactoe import TicTacToe
from result_view import ResultScreen
from menu_view import MenuScreen
from multiplayer import multiplayer
from connect_view import ConnectView

#Main
def main():
    more_games = 1
    while(more_games==1):
        menu_config = MenuScreen()
        option = menu_config.get_config()
        menu_config.close_window()
        if(option=="offline"):
            config_window = ConfigScreen(0)
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
        elif(option=="online"):
            config_window_o = ConfigScreen(1)
            game = config_window_o.get_config()
            if(game==None):
                break
            config_window_o.close_window()

            server_create = game.get_play_first()
            connect_view = ConnectView(server_create, game)
            host_ip = connect_view.get_multiplayer_data()
            if(host_ip==None):
                break

            connection = connect_view.stablish_connection()
            if(connection==None):
                break
            time.sleep(1)
            connect_view.close_window()

            game_window_o = GameScreen(game)
            result = game_window_o.play_online(host_ip)
            if(result==None):
                break
            game_window_o.close_window()

            del config_window_o
            del game_window_o

            result_window = ResultScreen(result)
            more_games = result_window.more_games()

            del result_window
        else:
            break
        del menu_config
        

#The program start here
main()
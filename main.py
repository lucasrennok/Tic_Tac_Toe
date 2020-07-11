#Imports
import re
from tictactoe import TicTacToe

#Main
def main():
    while(True):
        option = 0

        print("\n\n**Welcome to the Tic Tac Toe Game**\n\n>Select one:\n 1- Player One vs Computer\n 2- One Player vs Player Two\n ")
        while(option!=1 and option!=2):
            answer = input(">")
            if re.match('^\d+$', answer):
                option = int(answer)
                if(option==1 or option==2):
                    print("\nGood game...\n")
                else:
                    print("\nThere aren't that option in the Menu\nOnly 1 or 2\n")
            else:
                option = -1
                print("\nHey, you can't put a caracter different from an integer number!\n")
        game = TicTacToe(option)
        status = game.execute_game()
        print(game)
        if(status==0):
            print("*Nobody Won*\n")
        elif(status==1):
            print("*Player One Won*\n")
        elif(status==2):
            print("*Player Two Won*\n")
        else:
            print("*Computer Won*\n")
        if(game.start_new_game()==False):
            return None
        else:
            game.reset_game()

#The program start here
main()
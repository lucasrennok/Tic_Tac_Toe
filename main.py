#Imports
from random import randint
import re

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

#Class of the TicTacToe
class TicTacToe:
    #Variables
    matrix_game = [[0,0,0],[0,0,0],[0,0,0]]
    players = 1

    def __init__(self,players):
        self.players = players

    def __str__(self):
        num_of_players = "Game with " + str(self.players) + " players"
        matrix_str = ""
        for i in range(3):
            for j in range(3):
                matrix_str+=" " + str(self.matrix_game[i][j])
            matrix_str+="\n"
        result = num_of_players + "\n" + matrix_str + "\n"
        return result

    def execute_game(self):
        p1_x=-1; p1_y=-1; p2_x=-1; p2_y=-1
        if(self.players==1):
            print("--You chose to play alone--")
        else:
            print("--Have a good battle--")
        print("\nPlayer One:")
        first = input(">Do you want to be the first?\n1-Yes\nAny Key-No\n>")
        while(True):
            if(first=='1'):
                print(self)
                while(p1_x<0 or p1_x>2 or p1_y<0 or p1_y>2 or self.place_already_selected(p1_x,p1_y)==True):
                    p1_x = int(input("P1-Choose a row: "))
                    p1_y = int(input("P1-Choose a column: "))
                self.matrix_game[p1_x][p1_y] = 1
                if(self.won(1)):
                    return 1
                elif(self.matrix_completed()):
                    return 0
                if(self.players==2):
                    print(self)
                    while(p2_x<0 or p2_x>2 or p2_y<0 or p2_y>2 or self.place_already_selected(p2_x,p2_y)==True):
                        p2_x = int(input("\nP2-Choose a row: "))
                        p2_y = int(input("P2-Choose a column: "))
                else:
                    while(self.place_already_selected(p2_x,p2_y)==True):
                        p2_x = randint(0,2)
                        p2_y = randint(0,2)  
                self.matrix_game[p2_x][p2_y] = 2
                if(self.won(2)):
                    if(self.players==2):
                        return 2
                    else:
                        return 3
                elif(self.matrix_completed()):
                    return 0
            else:
                if(self.players==2):
                    print(self)
                    while(p2_x<0 or p2_x>2 or p2_y<0 or p2_y>2 or self.place_already_selected(p2_x,p2_y)==True):
                        p2_x = int(input("\nP2-Choose a row\n>"))
                        p2_y = int(input("P2-Choose a column\n>"))
                else:
                    while(self.place_already_selected(p2_x,p2_y)==True):
                        p2_x = randint(0,2)
                        p2_y = randint(0,2)  
                self.matrix_game[p2_x][p2_y] = 2
                if(self.won(2)):
                    if(self.players==2):
                        return 2
                    else:
                        return 3
                elif(self.matrix_completed()):
                    return 0
                print(self)
                while(p1_x<0 or p1_x>2 or p1_y<0 or p1_y>2 or self.place_already_selected(p1_x,p1_y)==True):
                    p1_x = int(input("P1-Choose a row\n>"))
                    p1_y = int(input("P1-Choose a column\n>"))
                self.matrix_game[p1_x][p1_y] = 1
                if(self.won(1)):
                    return 1
                elif(self.matrix_completed()):
                    return 0
    
    def start_new_game(self):
        answer = input(">Do you want to play one more game?\n1-Yes\nAny Key-No\n>")
        if(answer=='1'):
            answer = True
        else:
            answer = False
        return answer

    def place_already_selected(self,x,y):
        if(self.matrix_game[x][y]!=0):
            return True
        return False
    
    def matrix_completed(self):
        for i in range(3):
            for j in range(3):
                if(self.matrix_game[i][j]==0):
                    return False
        return True

    def won(self,player):
        won = False
        for i in range(3):
            if(self.matrix_game[i][0]==player and self.matrix_game[i][1]==player and self.matrix_game[i][2]==player):
                won = True
        for j in range(3):
            if(self.matrix_game[0][j]==player and self.matrix_game[1][j]==player and self.matrix_game[2][j]==player):
                won = True
        if(self.matrix_game[0][0]==player and self.matrix_game[1][1]==player and self.matrix_game[2][2]==player):
            won = True
        elif(self.matrix_game[0][2]==player and self.matrix_game[1][1]==player and self.matrix_game[2][0]==player):
            won = True
        return won
    
    def reset_game(self):
        self.players=1
        for i in range(3):
            for j in range(3):
                self.matrix_game[i][j]=0

   
#The program start here
main()
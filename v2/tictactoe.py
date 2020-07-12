#Imports


#Class of the TicTacToe
class TicTacToe:
    #Variables
    matrix_game = [[0,0,0],[0,0,0],[0,0,0]]

    def __init__(self,players,play_first):
        self.players = players
        if(play_first):
            self.actual_player = 1
        else:
            self.actual_player = 2
        self.play_first = play_first

    def __str__(self):
        str_result = ""
        for i in range(3):
            for j in range(3):
                str_result+= " " + str(self.matrix_game[i][j])
            str_result+="\n"
        return str_result

    def writeInCoordinate(self,player_number,x,y):
        if(self.matrix_game[x][y]!=0):
            return -1

        number_of_button=1
        if(x==1):
            number_of_button=4
        elif(x==2):
            number_of_button=7
        number_of_button+=y

        self.game_view.buttonLock('b'+str(number_of_button), player_number)
        self.matrix_game[x][y]=player_number

        if(player_number==1):
            self.actual_player = 2
        elif(player_number==2):
            self.actual_player = 1

        if(self.won(1)):
            return 1
        elif(self.won(2)):
            if(self.players==2):
                return 2
            else:
                return 3
        elif(self.matrix_completed()):
            return 0

        return 4
    
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

    def get_actual_player(self):
        return self.actual_player

    def get_num_players(self):
        return self.players

    def get_matrix(self):
        return self.matrix_game
    
    def get_play_first(self):
        return self.play_first

    def set_actual_player(self,actual_player):
        self.actual_player = actual_player

    def set_game_view(self,game_view):
        self.game_view = game_view
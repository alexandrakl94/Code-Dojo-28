"A test suite for a Three Men's Morris game"

class Game():
    rows = 3
    colums = 3
    
    def frame(self):
        board =  ""
        for i in range(0,self.rows):
            if i == 0:
                board += "\n"
            elif i == 1:
                board += "\n|\|/| \n"
            else:
                board += "\n|/|\| \n"

            for j in range(0,self.colums):
                if j == 0:
                    board += "o"
                else:
                    board += "-o"    

        return board


        
if __name__ == "__main__":
    game=Game()
    board = game.frame()
    print(board)
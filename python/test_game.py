"A test suite for a Three Men's Morris game"

class Game():
    rows = 3
    colums = 3
    state = []
    
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
                thing = "o"

                for piece in self.state:   
                    if piece[0]==i and piece[1]==j:
                        thing = 'x'

                if j == 0:
                    board += thing
                else:
                    board += "-" + thing

        return board

    def place(self,x,y):
        piece = (x,y)
        self.state.append(piece)
        
if __name__ == "__main__":
    game=Game()
    board = game.frame()
    print(board)

    for op in range(0,3):

        text_white = input("White player turn:")

        x= int(text_white[0])-1
        y= int(text_white[2])-1
        game.place(x,y)

        print(game.frame())
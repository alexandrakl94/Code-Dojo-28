"A test suite for a Three Men's Morris game"

class Game():
    rows = 3
    colums = 3
    state = []
    whiteCount = 3
    blackCount = 3

    
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
                        if piece[2]:
                            thing = 'x'
                        else:
                            thing = '#'

                if j == 0:
                    board += thing
                else:
                    board += "-" + thing

        return board


    def hasPieceLeft(self, isWhite):
        if isWhite and self.whiteCount > 0:
            return True
        elif not isWhite and self.blackCount > 0:
            return True
        else:
            return False


    def validateMove(self,x,y):
        for piece in self.state:
            if (piece[0] == x and piece[1] == y):
                return False

        return True


    def place(self,x,y,isWhite):
        piece = (x,y,isWhite)
        self.state.append(piece)

        if isWhite:
            self.whiteCount -= 1
        else:
            self.blackCount -= 1
        
if __name__ == "__main__":
    game=Game()
    board = game.frame()
    print(board)

    isWhite = True

    while True:

        currPlayer = "White" if isWhite else "Black"

        text_white = input('{0} player turn:'.format(currPlayer))

        x= int(text_white[0])-1
        y= int(text_white[2])-1

        if not game.hasPieceLeft(isWhite):
            # Todo: Ask for origin and destination, validate move, update the game
            movePiece = input("No moves left! Please select which piece to move!")
            print("TODO")
        else:
            if game.validateMove(x,y):
                game.place(x,y,isWhite)
            else:
                print("Don't touch this!")
                continue

        print(game.frame())

        isWhite = not isWhite

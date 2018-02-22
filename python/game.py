class Game():
    rows = 3
    columns = 3
    state = []
    whiteCount = 3
    blackCount = 3

    def start(self):
        
        board = self.frame()
        print(board)

        isWhite = True

        while True:

            currPlayer = "White" if isWhite else "Black"
            playerSymbol = "x" if isWhite else "#" 

            if not self.hasPieceLeft(isWhite):
                # Todo: Ask for origin and destination, validate move, update the game

                # The validation rules are: can't put your piece...
                # - You can only move your piece [DONE]
                # - On another player's piece [DONE]
                # - On your piece's current location [DONE]
                # - Where your piece has previously been [DONE]
                # Bugfix
                # - make strings into tuples for origin and destination

                origin = input("No moves left! Please select which piece to move!")

                if self.doesPlayerOwn(currPlayer, origin[0], origin[2]):
                    destination = input("And now the destination location")
                
                if self.validateMove(destination[0], destination[2]):
                    success = self.movePiece(origin, destination)

                    if not success:
                        continue

                else:
                    print("you can't move it")
                    continue
                
            else:
                text_white = input('{0} player turn ({1}):'.format(currPlayer, playerSymbol))

                x = int(text_white[0]) - 1
                y = int(text_white[2]) - 1
                if self.validateMove(x,y):
                    self.place(x, y, isWhite)
                else:
                    print("Don't touch this!")
                    continue

            print(self.frame())

            isWhite = not isWhite
        
    @classmethod
    def makeTuple(cls,inputString):
        
        x = int(inputString[0]) - 1
        y = int(inputString[2]) - 1
        return (x, y)

    def movePiece(self, origin, destination):

        for piece in self.state:
            if piece.x == origin[0] and piece.y == origin[2]:
                if piece.x_original == destination[0] and piece.y_original == destination[2]:
                    print("Go away!")
                    return False    
                else:
                    piece.x = destination[0]
                    piece.y = destination[2]
                    return True
        print("oh something is wrong")
        return False

    def frame(self):
        board =  ""
        for i in range(0, self.rows):
            if i == 0:
                board += "\n"
            elif i == 1:
                board += "\n|\|/| \n"
            else:
                board += "\n|/|\| \n"

            for j in range(0, self.columns):
                thing = "o"

                for piece in self.state:   
                    if piece['x'] == i and piece['y'] == j:
                        if piece['isWhite']:
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


    def validateMove(self, x, y):
        for piece in self.state:
            if (piece['x'] == x and piece['y'] == y):
                return False

        return True

    def doesPlayerOwn(self, isWhite, x, y):
      for piece in self.state:
        print(piece, x, y, isWhite)  
        if (piece['x'] == x and piece['y'] == y and piece['isWhite'] == isWhite):
          return True

      return False

    @classmethod
    def createPiece(cls, x, y, isWhite):
        return { 
          "x": x,
          "y": y,
          "x_original":x,
          "y_original":y,
          "isWhite": isWhite 
        }


    def place(self, x, y, isWhite):
        piece = Game.createPiece(x, y, isWhite = True)
        self.state.append(piece)

        if isWhite:
            self.whiteCount -= 1
        else:
            self.blackCount -= 1


    
        
        
if __name__ == "__main__":
    game=Game()
    game.start()
    
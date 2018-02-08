class Game():
    rows = 3
    columns = 3
    state = []
    whiteCount = 3
    blackCount = 3

    
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
        if (piece['x'] == x and piece['y'] == y and piece['isWhite'] == isWhite):
          return True

      return False


    def createPiece(x, y, isWhite):
        return { 
          "x": x,
          "y": y,
          "isWhite": isWhite 
        }


    def place(self, x, y, isWhite):
        piece = Game.createPiece(x, y, isWhite)
        self.state.append(piece)

        if isWhite:
            self.whiteCount -= 1
        else:
            self.blackCount -= 1

    def __init__(self):
        self.something = "blue"


if __name__ == "__main__":
    game=Game()
    board = game.frame()
    print(board)

    isWhite = True

    while True:

        currPlayer = "White" if isWhite else "Black"

        text_white = input('{0} player turn:'.format(currPlayer))

        x = int(text_white[0]) - 1
        y = int(text_white[2]) - 1

        if not game.hasPieceLeft(isWhite):
            # Todo: Ask for origin and destination, validate move, update the game

            # The validation rules are: can't put your piece...
              # - You can only move your piece [DONE]
              # - On another player's piece
              # - On your piece's current location
              # - Where your piece has previously been

            movePiece = input("No moves left! Please select which piece to move!")

            if game.doesPlayerOwn(currPlayer, movePiece[0], movePiece[2]):
              destination = input("And now the destination location")
              
              if game.validateMove(destination[0], destination[2]):
                print("Nice, we have validated the destination! ((:")

            else:
                print("")
                continue
              
        else:
            if game.validateMove(x,y):
                game.place(x, y, isWhite)
            else:
                print("Don't touch this!")
                continue

        print(game.frame())

        isWhite = not isWhite

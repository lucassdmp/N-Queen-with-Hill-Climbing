from ChessCell import ChessCell


class Queen:
    def __init__(self,number, row=0, col=0):
        self.row = row
        self.col = col
        self.number = number

    def move(self, origin: ChessCell, destination: ChessCell):
        if destination.queen != None:
            print("Destination cell already has a queen")
        else:
            origin.queen = None
            destination.queen = self
            self.row = destination.row
            self.col = destination.col

    def getLowestCollisionMovableCell(self, ChessBoard):
        lowestCollision = ChessBoard.board[self.row][self.col].collisions
        lowestCollisionCell = ChessBoard.board[self.row][self.col]
        for i in range(ChessBoard.n):
            if (
                self.row - i > 0
                and ChessBoard.board[self.row - i][self.col].collisions
                < lowestCollision
                and ChessBoard.board[self.row - i][self.col].queen == None
            ):
                lowestCollision = ChessBoard.board[self.row - i][self.col].collisions
                lowestCollisionCell = ChessBoard.board[self.row - i][self.col]
            if (
                self.row + i < ChessBoard.n
                and ChessBoard.board[self.row + i][self.col].collisions
                < lowestCollision
                and ChessBoard.board[self.row - i][self.col].queen == None
            ):
                lowestCollision = ChessBoard.board[self.row + i][self.col].collisions
                lowestCollisionCell = ChessBoard.board[self.row + i][self.col]
            if (
                self.col - i > 0
                and ChessBoard.board[self.row][self.col - i].collisions
                < lowestCollision
                and ChessBoard.board[self.row - i][self.col].queen == None
            ):
                lowestCollision = ChessBoard.board[self.row][self.col - i].collisions
                lowestCollisionCell = ChessBoard.board[self.row][self.col - i]
            if (
                self.col + i < ChessBoard.n
                and ChessBoard.board[self.row][self.col + i].collisions
                < lowestCollision
                and ChessBoard.board[self.row - i][self.col].queen == None
            ):
                lowestCollision = ChessBoard.board[self.row][self.col + i].collisions
                lowestCollisionCell = ChessBoard.board[self.row][self.col + i]
            if (
                self.row - i > 0
                and self.col - i > 0
                and ChessBoard.board[self.row - i][self.col - i].collisions
                < lowestCollision
                and ChessBoard.board[self.row - i][self.col].queen == None
            ):
                lowestCollision = ChessBoard.board[self.row - i][
                    self.col - i
                ].collisions
                lowestCollisionCell = ChessBoard.board[self.row - i][self.col - i]
            if (
                self.row - i > 0
                and self.col + i < ChessBoard.n
                and ChessBoard.board[self.row - i][self.col + i].collisions
                < lowestCollision
                and ChessBoard.board[self.row - i][self.col].queen == None
            ):
                lowestCollision = ChessBoard.board[self.row - i][
                    self.col + i
                ].collisions
                lowestCollisionCell = ChessBoard.board[self.row - i][self.col + i]
            if (
                self.row + i < ChessBoard.n
                and self.col - i > 0
                and ChessBoard.board[self.row + i][self.col - i].collisions
                < lowestCollision
                and ChessBoard.board[self.row - i][self.col].queen == None
            ):
                lowestCollision = ChessBoard.board[self.row + i][
                    self.col - i
                ].collisions
                lowestCollisionCell = ChessBoard.board[self.row + i][self.col - i]
            if (
                self.row + i < ChessBoard.n
                and self.col + i < ChessBoard.n
                and ChessBoard.board[self.row + i][self.col + i].collisions
                < lowestCollision
                and ChessBoard.board[self.row - i][self.col].queen == None
            ):
                lowestCollision = ChessBoard.board[self.row + i][
                    self.col + i
                ].collisions
                lowestCollisionCell = ChessBoard.board[self.row + i][self.col + i]

        return lowestCollisionCell

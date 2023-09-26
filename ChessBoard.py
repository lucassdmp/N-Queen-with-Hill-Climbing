from random import randint
from ChessCell import ChessCell
from Queen import Queen


class ChessBoard:
    def __init__(self, n: int):
        self.n = n
        self.queens = [Queen(i) for i in range(n)]
        self.board = [[ChessCell(x, y) for y in range(n)] for x in range(n)]
        self.fillBoard()

    def fillBoard(self):
        row = 0
        col = 0
        for queen in self.queens:
            while self.board[row][col].queen != None:
                row = randint(0, self.n - 1)
                col = randint(0, self.n - 1)
            self.board[row][col].queen = queen
            queen.row = row
            queen.col = col

        self.calculateCollisions()

    def calculateCollisions(self):
        for i in range(self.n):
            for j in range(self.n):
                self.board[i][j].collisions = self.getCollisionsFromPos(i, j)

    def getCollisionsFromPos(self, row, col):
        collisions = 0
        for i in range(self.n):
            if self.board[row][i].queen != None and i != col:
                collisions += 1
            if self.board[i][col].queen != None and i != row:
                collisions += 1

        # Main Diagonal
        for i in range(self.n):
            if (
                row + i < self.n
                and col + i < self.n
                and self.board[row + i][col + i].queen != None
                and i != 0
            ):
                collisions += 1
            if (
                row - i >= 0
                and col - i >= 0
                and self.board[row - i][col - i].queen != None
                and i != 0
            ):
                collisions += 1
                
        # Secondary Diagonal
        for i in range(self.n):
            if (
                row + i < self.n
                and col - i >= 0
                and self.board[row + i][col - i].queen != None
                and i != 0
            ):
                collisions += 1
            if (
                row - i >= 0
                and col + i < self.n
                and self.board[row - i][col + i].queen != None
                and i != 0
            ):
                collisions += 1

        return collisions

    def printBoard(self):
        qCount = 0
        for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col].queen != None:
                    print("Q"+str(self.board[row][col].queen.number), (row,col), end=" ")
                    qCount += 1
                else:
                    print(self.board[row][col].collisions, (row,col), end="  ")
            print()
            
        for queen in self.queens:
            print("Colisões atuais:", self.board[queen.row][queen.col].collisions, end=" ")
            cell = queen.getLowestCollisionMovableCell(self)
            print("Celula com menos colisões:", cell.row, cell.col)
            
    def isSolved(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j].collisions != 0:
                    return False
        return True

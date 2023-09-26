class ChessCell:
    def __init__(self, row = 0, col = 0):
        self.row = row
        self.col = col
        self.collisions = 0
        self.queen = None
    

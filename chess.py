from graphics import *
import math

#board
class Board:
    def __init__(self, p1, img, win, cells):
        self.img = img
        self.win = win
        self.cells = cells

        I = Image(p1, img)
        I.draw(win)

        self.size = I.getWidth()
        self.p1 = Point(((p1.x * 2) - self.size), ((p1.y * 2) - self.size))

        self.pieces = {}
        for i in range(8):
            for j in range(8):
                self.pieces.update({str(i) + str(j):False})

    def whereClicked(self, p):
        p1 = self.p1
        size = self.size
        cells = self.cells
        p = Point(p.x - p1.x, p.y - p1.y)
        if p.x < 0 or p.y < 0:
            return False
        if p.x > self.size or p.y > self.size:
            return False
        print(p.x, p.y)
        x = math.trunc((p.x / size) * cells)
        y = math.trunc((p.y / size) * cells)
        return [x, y]

    def whatPiece(self, p):
        return(self.pieces.get(p))

    def updateSquare(self, p):
        if self.pieces.get(p):
            self.pieces.update({p:False})
            return
        self.pieces.update({p:True})
        


def main():
    win = GraphWin("Chess", 1000, 700)
    
    board = Board(Point(350, 350), "chess.png", win, 8)

    while True:
        p = win.getMouse()
        print(board.whereClicked(p))
    

if __name__ == "__main__":
    main()

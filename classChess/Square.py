# Square Class
from graphics import *
from Piece import *

class Square:

    def __init__(self, pos, win):

        self.pieceExist = False
        self.r = Rectangle(pos, Point(pos.getX() + 80, pos.getY() + 80))
        self.r.draw(win)
        self.piece = None
        self.pos = pos
        self.x = ((pos.getX() - 100)//80)
        self.y = ((pos.getY() - 100)//80)

    def getPos(self):
        return [self.x, self.y]

    def hasPiece(self):
        return self.pieceExist

    def getPiece(self):
        return self.piece

    def addPiece(self, piece):
        self.piece = piece
        self.pieceExist = True

    def removePiece(self):
        self.piece = None
        self.pieceExist = False

    def isClicked(self, m):
        maxX = self.pos.getX() + 80
        minX = self.pos.getX()
        maxY = self.pos.getY() + 80
        minY = self.pos.getY()

        if m.getX() < maxX:
            if m.getX() > minX:
                if m.getY() < maxY:
                    if m.getY() > minY:
                        return True
        return False




    

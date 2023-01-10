# Piece Class
from graphics import *

class Piece:

    def __init__(self, pos, name, win):

        self.image = Circle(pos, 30)
        self.image.draw(win)
        self.name = name
        self.T = Text(pos, name)
        self.T.draw(win)
        self.x = ((pos.getX() - 140)//80)
        self.y = ((pos.getY() - 140)//80)

    def getName(self):
        return self.name

    def getPos(self):
        return [self.x, self.y]

    def move(self):
        possibleMoves = []

        if self.name == "pawn":
            newY = self.y - 1
            possibleMoves.append([self.x, newY])

        if self.name == "queen":
            right = 8 - self.x
            left = self.x
            above = self.y
            below = 8 - self.y

        if self.name == "knight":
            rawMoves = []
            x = self.x
            y = self.y
            rawMoves.append([x + 2, y + 1])
            rawMoves.append([x + 2, y - 1])
            rawMoves.append([x + 1, y + 2])
            rawMoves.append([x + 1, y - 2])
            rawMoves.append([x -1, y + 2])
            rawMoves.append([x -1, y - 2])
            rawMoves.append([x -2, y + 1])
            rawMoves.append([x -2, y - 1])
    
            newMoves = []
            for i in range(8):
                i = rawMoves[i-1]
                if i[0] < 0 or i[0] > 7 or i[1] < 0 or i[1] > 7:
                    continue
                newMoves.append(i)
                    

            return newMoves
            

    
        #return possibleMoves






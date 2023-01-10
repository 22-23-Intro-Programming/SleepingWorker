from graphics import *

class Button:

    def __init__(self, win, p1, p2, color, text):
        self.color = color
        self.text = text

        x1 = p1.getX()
        x2 = p2.getX()
        y1 = p1.getY()
        y2 = p2.getY()
        self.minX = x1
        self.maxX = x2
        self.minY = y1
        self.maxY = y2
        
        center = Point((x1 + x2)/2, (y1 + y2)/2)
        
        self.body = Rectangle(p1, p2)
        self.body.draw(win)
        self.body.setFill(self.color)

        self.T = Text(center, self.text)
        self.T.draw(win)

    def isClicked(self, p):
        x = p.getX()
        y = p.getY()

        if x > self.minX:
            if x < self.maxX:
                if y > self.minY:
                    if y < self.maxY:
                        return True

        return False











        

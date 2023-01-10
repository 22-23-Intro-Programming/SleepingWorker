from graphics import *

class RectButton:

    def __init__(self, win, p1, p2):
        self.self = self
        self.win = win
        self.p1 = p1
        self.p2 = p2
        

    def Draw(self):
        p1 = self.p1
        p2 = self.p2
        c = Rectangle(p1, p2)
        c.draw(self.win)
        self.c = c
    
    
    def UnDraw(self):
        c = self.c
        c.undraw()
        if self.t:
            t = self.t
            t.undraw()


    def Color(self, color):
        win = self.win
        c = self.c
        c.setFill(color)


    def Text(self, text):
        p1 = self.p1
        p2 = self.p2
        try:
            t = self.t
            t.undraw()
            t = Text(Point((p1.x + p2.x)/2, (p1.y + p2.y)/2), text)
            t.draw(self.win)
        except:
            t = Text(Point((p1.x + p2.x)/2, (p1.y + p2.y)/2), text)
            t.draw(self.win)
            self.t = t
            

    def IsClicked(self, p):
        win = self.win
        p1 = self.p1
        p2 = self.p2
        if p1.x < p.x and p.x < p2.x and p1.y < p.y and p.y < p2.y:
            return True
        return False


#some sample code showing usage of RectButton class:
'''
def main():
    win = GraphWin("Button", 400, 400)
    b1 = RectButton(win, Point(100, 100), Point(300, 300))
    b1.Draw()
    b1.Text("Not Clicked")
    if b1.IsClicked(win.getMouse()):
        b1.Color("red")
        b1.Text("Clicked")

main()
'''
#check graphics.py for other classes



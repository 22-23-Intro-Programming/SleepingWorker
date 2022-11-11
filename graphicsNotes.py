from graphics import *

def main():
    win = GraphWin("Rectangles?")
    for i in range(5):
        c = Rectange(Point(100, 600/i - 20), Point(100, 600/i))
        c.drawWin()
        win.GetMouse()
        win.Close()
    
    

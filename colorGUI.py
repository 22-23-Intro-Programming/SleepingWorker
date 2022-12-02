from button import *

win = GraphWin("Color GUI", 800, 800)

E = Entry(Point(400, 400), 20)
T = Text(Point(400, 300), "Enter Hex Code For Color Above")
Q = RectButton(win, Point(675, 675), Point(775, 775))
C = RectButton(win, Point(375, 425), Point(425, 475))
c = "#000000"

def main():
    E.draw(win)
    T.draw(win)
    Q.Draw()
    Q.Color("#FF0000")
    C.Draw()
    C.Color("cyan")
    while True:
        p = win.getMouse()
        if Q.IsClicked(p):
            break
        if C.IsClicked(p):
            try:
                win.setBackground("#" + E.getText())
            except:
                continue
    win.close()

main()
        
    

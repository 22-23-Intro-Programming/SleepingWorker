from button import *
from Shark import *
from Fish import *
import time

'''creates a grid using lines from graphics module
takes in parameters g(# of columns/rows), p(total width/height in pixels
and win(window to be draw in)'''
def grid(g, p, win):
    
    '''draws vertical lines of grid'''
    for i in range(g + 1):
        p1 = Point(((p/g) * (i)) + 50, 100)
        p2 = Point(((p/g) * (i)) + 50, 500)
        l = Line(p1, p2)
        l.draw(win)

    '''draws horizontal lines of grid'''
    for i in range(g + 1):
        p1 = Point(50, ((p/g) * (i)) + 100)
        p2 = Point(450, ((p/g) * (i)) + 100)
        l = Line(p1, p2)
        l.draw(win) 


def main():
    '''creates the window'''
    win = GraphWin("Shark Simulator", 600, 600)
    win.setBackground("white")
    
    '''calls grid function to draw grid with 20 collumns and 400 pixel width'''
    grid(20, 400, win)
    '''creating all the buttons
    steps one move forward'''
    Step = RectButton(win, Point(475, 100), Point(575, 200))
    Step.Text("Step")
    Step.Draw()
    '''runs until all fish or sharks are dead'''
    Run = RectButton(win, Point(475, 205), Point(575, 305))
    Run.Text("Run")
    Run.Draw()
    '''quits window'''
    Quit = RectButton(win, Point(475, 310), Point(575, 410))
    Quit.Text("Quit")
    Quit.Draw()
    '''resets simulation'''
    Reset = RectButton(win, Point(475, 415), Point(575, 515))
    Reset.Text("Reset")
    Reset.Draw()
    '''creating the instances of sharks and fish'''
    S1 = Shark(win)
    F1 = Fish(win)
    F2 = Fish(win)
    F3 = Fish(win)
    '''puts shark and fish instances in lists'''
    fishes = [F1, F2, F3]
    sharks = [S1]
    oF = fishes.copy()
    oS = sharks.copy()
    '''runs to allow buttons to be clicked mulitple times and run forever'''
    for i in oF + oS:
        i.Reset(oS + oF)
    while True:
        '''waits for mouse click and gets mouse position'''
        p = win.getMouse()
        #checks if step button was clicked and steps forward on move
        if Step.IsClicked(p):
            for i in sharks:
                i.Move(fishes, sharks)
                for j in fishes:
                    if j.CheckDie(sharks):
                        fishes.remove(j)
            for i in fishes:
                i.Move(sharks, fishes)
        #checks if quit button was clicked and quits the window if it was
        elif Quit.IsClicked(p):
            win.close()
            break
        #checks if run button was clicked and starts a loop where it steps
        #once forward each .5 seconds
        elif Run.IsClicked(p):
            while len(fishes) != 0:
                for i in sharks:
                    i.Move(fishes, sharks)
                    for j in fishes:
                        if j.CheckDie(sharks):
                            fishes.remove(j)
                for i in fishes:
                    i.Move(sharks, fishes)
                time.sleep(.1)
        #checks if reset button was clicked and resets the board
        elif Reset.IsClicked(p):
            for i in oF + oS:
                i.Reset(oS + oF)
            sharks = oS.copy()
            fishes = oF.copy()

'''runs main function'''          
if __name__ == "__main__":
    main()

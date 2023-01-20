from button import *
import random
import sharkSimulator
import imageEditor
import palindromeGUI
import characterCreator
import pythonProblemSet2
import pythonProblemSet3

def main():
    #creates window
    mainWin = GraphWin("Python Portfolio", 600, 600)
    mainWin.setBackground("#FFFFFF")

    #creating the buttons
    
    S = RectButton(mainWin, Point(100, 100), Point(200, 200))
    S.Draw()

    I = RectButton(mainWin, Point(300, 100), Point(400, 200))
    I.Draw()

    P = RectButton(mainWin, Point(100, 300), Point(200, 400))
    P.Draw()

    C = RectButton(mainWin, Point(300, 300), Point(400, 400))
    C.Draw()

    CC = RectButton(mainWin, Point(100, 500), Point(200, 600))
    CC.Draw()

    PS = RectButton(mainWin, Point(300, 500), Point(400, 600))
    PS.Draw()

    Q = RectButton(mainWin, Point(500, 500), Point(600, 600))
    Q.Draw()

    ST = Text(Point(150, 90), "Simulation where shark hunts fishes")
    ST.draw(mainWin)

    IT = Text(Point(350, 85), "allows you to edit an \n image with different buttons")
    IT.draw(mainWin)

    PT = Text(Point(150, 290), "Enter a string and it tells you if it is a palindrome")
    PT.draw(mainWin)

    CT = Text(Point(350, 280), "has buttons that allow \nyou to change the \nfeatures of a face")
    CT.draw(mainWin)

    CCT = Text(Point(150, 480), "you enter amount, starting \ncurrency, and ending currency and \n it converts it")
    CCT.draw(mainWin)

    PST = Text(Point(350, 460), "you enter a string \n and it doubles \n each character in it \n you enter a string \n and it converts \n it to camel case")
    PST.draw(mainWin)

    S.Text("Shark Sim")
    I.Text("Image Editor")
    P.Text("Palindrome GUI")
    C.Text("Character Creator")
    CC.Text("Problem Set 3")
    PS.Text("Problem Set 2")
    Q.Text("Quit")
    while True:
        #gives all buttons random colors
        for i in [S, I, P, C, CC, PS, Q]:
            i.Color(color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        #checks for button clicks
        p = 0
        p = mainWin.getMouse()
        if S.IsClicked(p):
            sharkSimulator.main()
        elif I.IsClicked(p):
            imageEditor.main()
        elif P.IsClicked(p):
            palindromeGUI.main()
        elif C.IsClicked(p):
            characterCreator.main()
        elif CC.IsClicked(p):
            pythonProblemSet3.main()
        elif PS.IsClicked(p):
            pythonProblemSet2.main()
        elif Q.IsClicked(p):
            break
    mainWin.close()
        


if __name__ == "__main__":
    main()

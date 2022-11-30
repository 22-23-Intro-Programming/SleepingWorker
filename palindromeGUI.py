from button import *

win = GraphWin("Palidnrome", 800, 800)

Desc = Text(Point(400, 250), "Write word")

Czech = RectButton(win, Point(350, 450), Point(450, 500))
Quit = RectButton(win, Point(700, 700), Point(775, 775))
M = Text(Point(400, 200), "")

T = Entry(Point(400, 400), 10)



def main():
    Czech.Draw()
    Czech.Text("Check")
    Czech.Color("green")
    Quit.Draw()
    Quit.Text("Quit")
    Quit.Color("red")
    T.draw(win)
    M.draw(win)
    while True:
        p = win.getMouse()
        l = T.getText()
        if Czech.IsClicked(p):
            if l == l[::-1]:
                M.setText("Thats a palindrome")
            else:
                M.setText("Thats not a palindrome")
        if Quit.IsClicked(p):
            break
    win.close()

if __name__ == "__main__":
    main()

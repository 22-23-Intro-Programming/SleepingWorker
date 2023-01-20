from button import *


def main():
    win = GraphWin("Palindrome", 800, 800)
    win.setBackground("#FFFFFF")

    Desc = Text(Point(400, 250), "Write word")

    Czech = RectButton(win, Point(350, 450), Point(450, 500))
    Quit = RectButton(win, Point(700, 700), Point(775, 775))
    M = Text(Point(400, 200), "")

    T = Entry(Point(400, 400), 10)
    Czech.Draw()
    Czech.Text("Check")
    Czech.Color("#FFFF00")
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
                win.setBackground("#00FF00")
            else:
                M.setText("Thats not a palindrome")
                win.setBackground("#FF0000")
        if Quit.IsClicked(p):
            break
    win.close()

if __name__ == "__main__":
    main()

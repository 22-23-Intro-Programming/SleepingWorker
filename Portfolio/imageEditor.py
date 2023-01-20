from button import *
import math

#loops through all pixels and makes them darker
def darken(im, b):
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b:
                p = color_rgb(int(pix[0]*.75), int(pix[1]*.75), int(pix[2]*.75))
                im.setPixel(j, i, p)

#loops through all pixels and makes them lighter
def lighten(im, b):
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b: 
                rgb = [(255 - pix[0]) / 2, (255 - pix[1]) / 2, (255 - pix[2]) / 2]
                p = color_rgb(int(pix[0] + rgb[0]), int(pix[1] + rgb[1]), int(pix[2] + rgb[2]))
                im.setPixel(j, i, p)

#loops through all pixels and makes their rgb values all the average of the values
#ex:  rgb(10, 12, 14) -> rgb(12, 12, 12)          
def grayScale(im, b):
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b:
                av = (pix[0] + pix[1] + pix[2])/3
                p = color_rgb(int(av), int(av), int(av))
                im.setPixel(j, i, p)

#loops through all pixels and makes them lighter or darker if their average
#is above or below 127
def contrast(im, b):
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b:
                av = (pix[0] + pix[1] + pix[2])/3
                p = color_rgb(int(av), int(av), int(av))
                if av > 127:
                    rgb = [(255 - pix[0]) / 2, (255 - pix[1]) / 2, (255 - pix[2]) / 2]
                    p = color_rgb(int(pix[0] + rgb[0]), int(pix[1] + rgb[1]), int(pix[2] + rgb[2]))
                    im.setPixel(j, i, p)
                else:
                    p = color_rgb(int(pix[0]*.75), int(pix[1]*.75), int(pix[2]*.75))
                    im.setPixel(j, i, p)

#just like contrast but goes to either white or black in one click
def superContrast(im, b):
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b:
                av = (pix[0] + pix[1] + pix[2])/3
                '''if av < 86:
                    im.setPixel(j, i, color_rgb(0, 0, 0))
                elif av < 171:
                    im.setPixel(j, i, color_rgb(127, 127, 127))
                else:
                    im.setPixel(j, i, color_rgb(225, 225, 225))'''
                if av > 127:
                    im.setPixel(j, i, color_rgb(225, 225, 225))
                else:
                    im.setPixel(j, i, color_rgb(0, 0, 0))

#loops through all pixels and makes them grayscale unless their red value is
#25 more than both the other ones
def redBoost(im, b):
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b:
                if (pix[0] > (pix[1] + 25)) and (pix[0] > (pix[2] + 25)):
                    continue
                else:
                    av = (pix[0] + pix[1] + pix[2])/3
                    p = color_rgb(int(av), int(av), int(av))
                    im.setPixel(j, i, p)

#red boost but green
def greenBoost(im, b):
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b:
                if (pix[1] > (pix[0])) and (pix[1] > (pix[2])):
                    continue
                else:
                    av = (pix[0] + pix[1] + pix[2])/3
                    p = color_rgb(int(av), int(av), int(av))
                    im.setPixel(j, i, p)

#green boost but blue
def blueBoost(im, b):
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b:
                if (pix[2] > (pix[0] + 25)) and (pix[2] > (pix[1] + 25)):
                    print("found one")
                    continue
                else:
                    av = (pix[0] + pix[1] + pix[2])/3
                    p = color_rgb(int(av), int(av), int(av))
                    im.setPixel(j, i, p)

#find the average of the pixels around every pixel and records that value
#loops over all the pixels again and sets their values to the averages
def blur(im, b):
    colors = []
    k = 0
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b:
                try:
                    up = im.getPixel(j+1, i)
                except:
                    up = im.getPixel(j, i)
                try:
                    down = im.getPixel(j-1, i)
                except:
                    down = im.getPixel(j, i)
                try:
                    right = im.getPixel(j, i+1)
                except:
                    right = im.getPixel(j, i)
                try:
                    left = im.getPixel(j, i-1)
                except:
                    left = im.getPixel(j, i)
                av1 = int((up[0] + down[0] + right[0] + left[0])/4)
                av2 = int((up[1] + down[1] + right[1] + left[1])/4)
                av3 = int((up[2] + down[2] + right[2] + left[2])/4)
                av4 = [av1, av2, av3]
                colors.append(av4)
            else:
                colors.append(b)
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            im.setPixel(j, i, color_rgb(colors[k][0], colors[k][1], colors[k][2]))
            k += 1

#finds the edges
def edge(im, b):
    #superContrast(im, b)
    colors = []
    k = 0
    for i in range(1, im.getHeight() - 1, 1):
        for j in range(1, im.getWidth() - 1, 1):
            pix = im.getPixel(j, i)
            if pix != b:
                av = (pix[0] + pix[1] + pix[2])/3
                up = im.getPixel(j+1, i)
                down = im.getPixel(j-1, i)
                right = im.getPixel(j, i+1)
                left = im.getPixel(j, i-1)
                '''up = math.sqrt((abs(up[0]-pix[0]) * abs(up[0]-pix[0])) + (abs(up[1]-pix[1]) * abs(up[1]-pix[1])) + (abs(up[2]-pix[2]) * abs(up[2]-pix[2])))
                down = math.sqrt((abs(down[0]-pix[0]) * abs(down[0]-pix[0])) + (abs(down[1]-pix[1]) * abs(down[1]-pix[1])) + (abs(down[2]-pix[2]) * abs(down[2]-pix[2])))
                left = math.sqrt((abs(left[0]-pix[0]) * abs(left[0]-pix[0])) + (abs(left[1]-pix[1]) * abs(left[1]-pix[1])) + (abs(left[2]-pix[2]) * abs(left[2]-pix[2])))
                right = math.sqrt((abs(right[0]-pix[0]) * abs(right[0]-pix[0])) + (abs(right[1]-pix[1]) * abs(right[1]-pix[1])) + (abs(right[2]-pix[2]) * abs(right[2]-pix[2])))'''
                c = []
                for z in [up, down, left, right]:
                    z = math.sqrt((abs(z[0]-pix[0]) * abs(z[0]-pix[0])) + (abs(z[1]-pix[1]) * abs(z[1]-pix[1])) + (abs(z[2]-pix[2]) * abs(z[2]-pix[2])))
                    if z > 25:
                        c.append(1)
                    else:
                        c.append(0)
                colors.append(max(c))
            else:
                colors.append(0)
    for i in range(1, im.getHeight() - 1, 1):
        for j in range(1, im.getWidth() - 1, 1):
            if colors[k] == 1:
                im.setPixel(j, i, color_rgb(0, 0, 0))
            else:
                im.setPixel(j, i, color_rgb(255, 255, 255))
            k+=1
                    
                
                
                
                
                
                
        

def main():
    #sets up window
    background = color_rgb(50, 50, 100)
    b = [0, 0, 0]
    win = GraphWin("Image Editor", 800, 800)
    win.setBackground(background)

    I = Image(Point(400, 450), "plant.png")
    I.draw(win)

    #makes all the buttons
    D = RectButton(win, Point(200, 0), Point(300, 100))
    D.Draw()
    D.Color("blue")
    D.Text("darken")

    L = RectButton(win, Point(500, 0), Point(600, 100))
    L.Draw()
    L.Color("blue")
    L.Text("lighten")

    G = RectButton(win, Point(350, 0), Point(450, 100))
    G.Draw()
    G.Color("gray")
    G.Text("grayscale")

    C = RectButton(win, Point(50, 0), Point(150, 100))
    C.Draw()
    C.Color("yellow")
    C.Text("contrast")
    
    RB = RectButton(win, Point(650, 0), Point(750, 100))
    RB.Draw()
    RB.Color("orange")
    RB.Text("red boost")

    B = RectButton(win, Point(25, 150), Point(125, 250))
    B.Draw()
    B.Color("brown")
    B.Text("blur")

    N = RectButton(win, Point(675, 525), Point(775, 625))
    N.Draw()
    N.Color("green")
    N.Text("reset")

    BB = RectButton(win, Point(0, 400), Point(100, 500))
    BB.Draw()
    BB.Color("cyan")
    BB.Text("blue boost")

    GB = RectButton(win, Point(0, 550), Point(100, 650))
    GB.Draw()
    GB.Color("green")
    GB.Text("green boost")

    E = RectButton(win, Point(0, 700), Point(100, 800))
    E.Draw()
    E.Color("purple")
    E.Text("edge thing")

    Q = RectButton(win, Point(675, 675), Point(775, 775))
    Q.Draw()
    Q.Color("red")
    Q.Text("quit")

    #checks for button clicks
    while True:
        p = win.getMouse()
        if Q.IsClicked(p):
            break
        elif N.IsClicked(p):
            I = Image(Point(400, 450), "plant.png")
            I.draw(win)
        elif D.IsClicked(p):
            darken(I, b)
        elif L.IsClicked(p):
            lighten(I, b)
        elif G.IsClicked(p):
            grayScale(I, b)
        elif C.IsClicked(p):
            superContrast(I, b)
        elif RB.IsClicked(p):
            redBoost(I, b)
        elif BB.IsClicked(p):
            blueBoost(I, b)
        elif GB.IsClicked(p):
            greenBoost(I, b)
        elif B.IsClicked(p):
            blur(I, b)
        elif E.IsClicked(p):
            edge(I, b)


    win.close()

if __name__ == "__main__":
    main()

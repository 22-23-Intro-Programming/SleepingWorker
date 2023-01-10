from button import *

def RGBtoHSV(r, g, b):
    r /= 255
    g /= 255
    b /= 255
    j = max(r, g, b)
    k = min(r, g, b)
    d = j-k
    v = j
    if d == 0:
        return 0, 0, v
    elif j == r:
        h = 60*(((g - b)/d)%6)
    elif j == g:
        h = 60*(((b - r)/d)+4)
    elif j == b:
        h = 60*(((r - g)/d)+2)
    else:
        print("oops")
    s = d/j
    l = [abs(h-120), h+120]
    return [round(max(l)), round(s*100), round(v*100)]
    
def HSVtoRGB(h, s, v):
    s/=100
    v/=100
    c = s*v
    x = c * (1-(abs((h/60)%2)-1))
    m = v-c
    if h >= 300:
        r = c
        g = 0
        b = x
    elif h >= 240:
        r = x
        g = 0
        b = c
    elif h >= 180:
        r = 0
        g = x
        b = c
    elif h >= 120:
        r = 0
        g = c
        b = x
    elif h >= 60:
        r = x
        g = c
        b = 0
    else:
        r = c
        g = x
        b = 0
    r = round((r+m)*255)
    g = round((g+m)*255)
    b = round((b+m)*255)
    return [r, g, b]

def diff(rgb1, rgb2):
    l = [rgb1, rgb2]
    for i in l:
        p = l.index(i)
        r = i[0]
        g = i[1]
        b = i[2]
        r /= 255
        g /= 255
        b /= 255
        j = max(r, g, b)
        k = min(r, g, b)
        d = j-k
        v = j
        if d == 0:
            l[p] = [0, 0, v*100]
            continue
        elif j == r:
            h = 60*(((g - b)/d)%6)
        elif j == g:
            h = 60*(((b - r)/d)+4)
        elif j == b:
            h = 60*(((r - g)/d)+2)
        else:
            print("oops")
        s = d/j
        m = [abs(h-120), h+120]
        l[p] = [max(m), s*100, v*100]
    hue = abs(l[0][0]-l[1][0])
    sat = abs(l[0][1]-l[1][1])
    val = abs(l[0][2]-l[1][2])
    return [hue, sat, val]

def edge(im, b, h, s, v):
    colors = []
    k = 0
    for i in range(1, im.getHeight() - 1, 1):
        for j in range(1, im.getWidth() - 1, 1):
            hue = []
            sat = []
            val = []
            pix = im.getPixel(j, i)
            a = im.getPixel(j+1, i)
            b = im.getPixel(j-1, i)
            c = im.getPixel(j, i+1)
            d = im.getPixel(j, i-1)
            hue.append(diff(pix, a)[0])
            hue.append(diff(pix, b)[0])
            hue.append(diff(pix, c)[0])
            hue.append(diff(pix, d)[0])
            sat.append(diff(pix, a)[1])
            sat.append(diff(pix, b)[1])
            sat.append(diff(pix, c)[1])
            sat.append(diff(pix, d)[1])
            val.append(diff(pix, a)[2])
            val.append(diff(pix, b)[2])
            val.append(diff(pix, c)[2])
            val.append(diff(pix, d)[2])
            if (max(hue) > h) or (max(sat) > s) or (max(val) > v):
                colors.append(1)
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
    #print(RGBtoHSV(10, 34, 123))
    #print(diff([0, 0, 255], [0, 0, 255]))
    background = color_rgb(50, 50, 100)
    b = [0, 0, 0]
    win = GraphWin("Image Editor", 800, 800)
    win.setBackground(background)

    I = Image(Point(400, 450), "plant.png")
    I.draw(win)

    H = Entry(Point(400, 625), 20)
    H.draw(win)

    S = Entry(Point(400, 650), 20)
    S.draw(win)

    V = Entry(Point(400, 675), 20)
    V.draw(win)

    W = Text(Point(400, 625), "Invalid Entry")
    W.setTextColor(color_rgb(255, 0, 0))

    E = RectButton(win, Point(200, 0), Point(300, 100))
    E.Draw()
    E.Color("blue")
    E.Text("run")

    Q = RectButton(win, Point(675, 675), Point(775, 775))
    Q.Draw()
    Q.Color("red")
    Q.Text("quit")

    R = RectButton(win, Point(675, 525), Point(775, 625))
    R.Draw()
    R.Color("green")
    R.Text("reset")

    while True:
        p = win.getMouse()
        W.undraw()
        if Q.IsClicked(p):
            break
        elif E.IsClicked(p):
            try:
                edge(I, b, int(H.getText()), int(S.getText()), int(V.getText()))
            except:
                W.draw(win)
                continue
        elif R.IsClicked(p):
            I = Image(Point(400, 450), "plant.png")
            I.draw(win)
    
    win.close()

if __name__ == "__main__":
    main()

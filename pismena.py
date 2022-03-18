
from math import cos, sin, pi, degrees, radians
import random
import tkinter


def bod(x, y, hrubka = 1, farba = "red"):
    if hrubka < 1:
        hrubka = 1
    canvas.create_rectangle(x, y, x + hrubka, y + hrubka, fill = farba, outline = farba)
    #canvas.create_line(x0, y0, x, y)

def krok(rx, ry):
#    if (min(abs(rx), abs(ry)) * 2) == 0:
#        return 100
#    hodnota = 360 // (min(abs(rx), abs(ry)) * 2)
#    if hodnota == 0:
        return 1
#    return hodnota








def pismeno_a(x0, y0, rx, ry, outline = "black"):
    m, n = 0, 0

    for uhol in range(270, 360, krok(rx, ry)):
        m += 1
        x = int(x0 + rx - rx * 2 * cos(radians(uhol)))
        y = int(y0 + ry * 2 * sin(radians(uhol)))
        outline = "yellow"
        bod(x,y,hrubka = 1,farba = outline)

    for uhol in range(0, 270, krok(rx, ry)):
        n += 1
        if uhol <= 180:
            x = int(x0 - rx * cos(radians(uhol)))
            y = int(y0 + ry * sin(radians(uhol)))
            outline = "red"
        elif uhol <= 270:
            x = x0 + rx
            y = int(y0 + 2 * ry * sin(radians(uhol)))
            outline = "green"

        bod(x,y,hrubka = 1,farba = outline)
    return m, n, m + n


""" 4 """
def pismeno_u(x0, y0, rx, ry, outline = "black"):
    m, n, o = 0, 0, 0

    for uhol in range(270, 360 + 270, krok(rx, ry)):
        if uhol < 360:
            m += 1
            x = x0 - rx
            y = int(y0 - y0/6 + 3/2 * ry * sin(radians(uhol)))
            outline = "gray"
            if uhol > 270 + 60:
                outline = "silver"
        elif uhol < 360 + 180:
            n += 1
            x = int(x0 - rx * cos(radians(uhol)))
            y = int(y0 -ry + ry *2 * sin(radians(uhol)))
            outline = "red"
            if uhol > 360 + 90:
                outline = "yellow"
        else:
            o += 1
            x = x0 + rx
            y = int(y0 - y0/6 + 3/2 * ry * sin(radians(uhol)))
            outline = "green"
            if uhol > 360 + 210:
                outline = "lightgreen"

        bod(x,y,hrubka = 1,farba = outline)
    return m, n, o, m + n + o


""" 5 """
def pismeno_o(x0, y0, rx, ry, outline = "black"):
    m, n, o, p = 0, 0, 0, 0

    for uhol in range(270, 270 + 360 + 180 + 90, krok(rx, ry)):
        if uhol < 270 + 360:
            n += 1
            x = int(x0 - rx * cos(radians(uhol)))
            y = int(y0 - ry/2 + ry * 3/2 * sin(radians(uhol)))
            outline = "blue"
            if uhol > 270 + 180:
                outline = "lightblue"
        elif uhol < 270 + 360 + 180:
            o += 1
            x = int(x0 - rx /4 * cos(radians(uhol)))
            y = int(y0 - 2 * ry + ry /8 + ry /8 * sin(radians(uhol)))
            outline = "red"
            if uhol > 270 + 360 + 90:
                outline = "pink"
        else:
            p += 1
            x = int(x0 - 3/2*rx * cos(radians(uhol)))
            y = int(y0 - 2 * ry + ry/4 * sin(radians(uhol)))
            outline = "green"
            if uhol > 270 + 360 + 180 + 45:
                outline = "lightgreen"
        bod(x,y,hrubka = 1,farba = outline)
    return m, n, o, p, m + n + o + p


""" 6 """
def kvacka(x0, y0, rx, ry, outline = "black"):
    m, n, o = 0, 0, 0

    for uhol in range(0, 180, krok(rx, ry)):
        if uhol < 90:
            n += 1
            x = int(x0 - rx/2 * cos(radians(uhol)))
            y = int(y0 -ry + ry *2 * sin(radians(uhol)))
            outline = "red"
            if uhol > 45:
                outline = "yellow"
        else:
            o += 1
            x = int(x0 - rx*3/2 * cos(radians(uhol)))
            y = int(y0 -ry + ry *2 * sin(radians(uhol)))
            outline = "green"
            if uhol > 90 + 45:
                outline = "lightgreen"

        bod(x, y, hrubka = 1, farba = outline)
    return m, n, o, m + n + o




def polobluk(x0, y0, rx, ry, outline = "black", sklon = 0):
    n = 0

    for uhol in range(0, 90, krok(rx, ry)):
        n += 1
        x = int(x0 + rx - rx * cos(radians(uhol)))
        y = int(y0 - ry * sin(radians(uhol + sklon)))           # sklon
        
        if uhol < 45: outline = "red"
        else: outline = "orange"

        bod(x,y,hrubka = 1,farba = outline)
    return x, y, n


def polobluk_inv(x0, y0, rx, ry, outline = "black", sklon = 0):
    n = 0

    for uhol in range(0, 90, krok(rx, ry)):
        n += 1
        x = int(x0 - rx * sin(radians(uhol)))
        y = int(y0 + ry - ry * cos(radians(uhol + sklon)))      # sklon
        
        if uhol < 45: outline = "blue"
        else: outline = "lightblue"

        bod(x, y, hrubka = 1, farba = outline)
    return x, y, n


def plnyobluk(x0, y0, zaciatok, koniec, rx, ry, outline = "black", sklon = 0):
    n = 0

    for uhol in range(zaciatok - sklon, koniec - sklon, krok(rx, ry)):
        n += 1
        x = int(x0 - rx * sin(radians(uhol)))
        y = int(y0 + ry - ry * cos(radians(uhol + sklon)))      # sklon
        
        if uhol < zaciatok: outline = "blue"
        elif uhol > (koniec // 2 - sklon): outline = "lightblue"
        else: outline = "dodgerblue"

        bod(x, y, hrubka = 1, farba = outline)
    return x, y, n


def priamka(x0, y0, rx, ry, outline = "black"):
    n = 0
    posun = krok(rx, ry)
    abs_rx = abs(rx)

    for i in range(0, abs_rx, posun):
        n += 1
        x = int(x0 + (i * rx) / abs_rx)
        y = int(y0 - (i * ry) / abs_rx)

        if i < abs_rx // 2: outline = "purple"
        else: outline = "pink"

        bod(x, y, hrubka = 1, farba = outline)
    return x, y, n


def priamka_inv(x0, y0, rx, ry, outline = "black"):
    n = 0
    posun = krok(rx, ry)
    abs_rx = abs(rx)

    for i in range(0, abs_rx, posun):
        n += 1
        x = int(x0 - (i * rx) / abs_rx)
        y = int(y0 + (i * ry) / abs_rx)

        if i < abs_rx // 2: outline = "green"
        else: outline = "lightgreen"

        bod(x, y, hrubka = 1, farba = outline)
    return x, y, n


def plnapriamka(x0, y0, rx, ry, outline = "black", sklon = 0):
    n = 0
    posun = krok(rx, ry)
    abs_rx = abs(rx)

    for i in range(0, abs_rx, posun):
        n += 1
        x = int(x0 + (i * rx) / abs_rx) + sklon
        y = int(y0 - (i * ry) / abs_rx)

        if i < abs_rx // 2: outline = "purple"
        else: outline = "pink"

        bod(x, y, hrubka = 1, farba = outline)
    return x - sklon, y, n


canvas = tkinter.Canvas(width = 1000, height = 800)
canvas.pack()

rx, ry = 50, 50
x0, y0 = 400, 200
canvas.create_text(x0, y0, text = (rx, ry, "++"))
canvas.create_rectangle(x0, y0, x0 + rx, y0 - ry)
canvas.create_rectangle(x0, y0, x0 - rx, y0 + ry)
print(1, polobluk(x0, y0, rx, ry))
print(2, priamka(x0, y0, rx, ry))
print(3, polobluk_inv(x0, y0, rx, ry))
print(4, priamka_inv(x0, y0, rx, ry))

rx, ry = 50, -50
x0, y0 = 400, 400
canvas.create_text(x0, y0, text = (rx, ry, "+-"))
canvas.create_rectangle(x0, y0, x0 + rx, y0 - ry)
canvas.create_rectangle(x0, y0, x0 - rx, y0 + ry)
print(5, polobluk(x0, y0, rx, ry))
print(6, priamka(x0, y0, rx, ry))
print(7, polobluk_inv(x0, y0, rx, ry))
print(8, priamka_inv(x0, y0, rx, ry))

rx, ry = -50, -50
x0, y0 = 200, 400
canvas.create_text(x0, y0, text = (rx, ry, "--"))
canvas.create_rectangle(x0, y0, x0 + rx, y0 - ry)
canvas.create_rectangle(x0, y0, x0 - rx, y0 + ry)
print(9, polobluk(x0, y0, rx, ry))
print(10, priamka(x0, y0, rx, ry))
print(11, polobluk_inv(x0, y0, rx, ry))
print(12, priamka_inv(x0, y0, rx, ry))

rx, ry = -50, 50
x0, y0 = 200, 200
canvas.create_text(x0, y0, text = (rx, ry, "-+"))
canvas.create_rectangle(x0, y0, x0 + rx, y0 - ry)
canvas.create_rectangle(x0, y0, x0 - rx, y0 + ry)
print(13, polobluk(x0, y0, rx, ry))
print(14, priamka(x0, y0, rx, ry))
print(15, polobluk_inv(x0, y0, rx, ry))
print(16, priamka_inv(x0, y0, rx, ry))



velkost = 60

""" o """
sklon = 8
rx, ry = (velkost * 2) // 3, velkost
x0, y0 = 800, 300 - 2 * ry
x0, y0, n = plnyobluk(x0, y0, 0, 360, rx, ry, "orangered", sklon)
""" c """
# x0 -= sklon
# plnyobluk(x0, y0, -2 * sklon, 180 + 4 * sklon, rx, ry, "orangered", sklon)
# rx, ry = -(sklon  * 2), -2 * velkost
# plnapriamka(x0, y0, rx, ry, "orangered", sklon)

""" O """
sklon *= 2
rx, ry = velkost, 2 * velkost
x0, y0 = 600, 300 - 2 * ry
x0, y0, n = plnyobluk(x0, y0, 0, 360, rx, ry, "orangered", sklon)
""" C """
# x0 -= sklon
# plnyobluk(x0, y0, -2 * sklon, 180 + 4 * sklon, rx, ry, "orangered", sklon)
# rx, ry = -sklon * 2, -4 * velkost
# plnapriamka(x0, y0, rx, ry, "orangered", sklon)


""" c """
sklon = 8
rx, ry = (velkost * 2) // 3, velkost
x0, y0 = 800, 600 - 2 * ry
plnyobluk(x0, y0, -2 * sklon, 180 + 4 * sklon, rx, ry, "orangered", sklon)
rx, ry = -(sklon  * 2), -2 * velkost
plnapriamka(x0, y0, rx, ry, "orangered", sklon)

""" C """
sklon *= 2
rx, ry = velkost, 2 * velkost
x0, y0 = 600, 600 - 2 * ry
plnyobluk(x0, y0, -2 * sklon, 180 + 4 * sklon, rx, ry, "orangered", sklon)
rx, ry = -sklon * 2, -4 * velkost
plnapriamka(x0, y0, rx, ry, "orangered", sklon)






tkinter.mainloop()

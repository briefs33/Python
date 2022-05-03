# farebné pexeso
# Bc. Attila Csontos
# https://github.com/briefs33
# capsule.briefs@gmail.com

from tkinter import *
from tkinter.ttk import *
from random import randint
import time
from configparser import ConfigParser

color_config = ConfigParser()
color_config.read('Hry/Pexeso/farby.ini')

farby_kariet4 = [
'#00FFFF', '#000000',
'#0000FF', '#8A2BE2',
'#D2691E', '#98FB98',
'#DDA0DD', '#FF0000']

farby_kariet6 = [
'#6495ED', '#006400', '#8B008B',
'#FF8C00', '#FF1493', '#1E90FF',
'#FFD700', '#4B0082', '#FFF0F5',
'#7CFC00', '#800000', '#00FA9A',
'#FFA500', '#FF4500', '#8B4513',
'#EE82EE', '#FFFF00', '#9ACD32']

farby_kariet8 = [
'#00FFFF', '#7FFFD4', '#000000', '#0000FF',
'#8A2BE2', '#5F9EA0', '#D2691E', '#6495ED',
'#006400', '#8B008B', '#FF8C00', '#FF1493',
'#1E90FF', '#FFD700', '#808080', '#4B0082',
'#FFF0F5', '#7CFC00', '#800000', '#00FA9A',
'#FFA500', '#FF4500', '#98FB98', '#DDA0DD',
'#B0E0E6', '#FF0000', '#BC8F8F', '#4169E1',
'#8B4513', '#EE82EE', '#FFFF00', '#9ACD32']

farby_kariet10 = [
'#00FFFF', '#000000', '#0000FF', '#8A2BE2', '#D2691E',
'#6495ED', '#DC143C', '#00008B', '#008B8B', '#006400',
'#8B008B', '#556B2F', '#FF8C00', '#8FBC8F', '#483D8B',
'#FF1493', '#1E90FF', '#B22222', '#FF00FF', '#FFD700',
'#ADFF2F', '#FF69B4', '#4B0082', '#F0E68C', '#32CD32',
'#800000', '#7B68EE', '#00FA9A', '#C71585', '#808000',
'#FFA500', '#FF4500', '#98FB98', '#DDA0DD', '#B0E0E6',
'#FF0000', '#BC8F8F', '#4169E1', '#8B4513', '#FA8072',
'#F4A460', '#2E8B57', '#A0522D', '#C0C0C0', '#4682B4',
'#D2B48C', '#FF6347', '#EE82EE', '#FFFF00', '#9ACD32']

farby_kariet12 = [
'#00FFFF', '#7FFFD4', '#000000', '#0000FF', '#8A2BE2', '#5F9EA0',
'#D2691E', '#6495ED', '#DC143C', '#00008B', '#008B8B', '#B8860B',
'#A9A9A9', '#006400', '#BDB76B', '#8B008B', '#556B2F', '#FF8C00',
'#8FBC8F', '#483D8B', '#FF1493', '#1E90FF', '#B22222', '#FF00FF',
'#FFD700', '#DAA520', '#808080', '#ADFF2F', '#FF69B4', '#CD5C5C',
'#4B0082', '#F0E68C', '#FFF0F5', '#7CFC00', '#FFFACD', '#F08080',
'#E0FFFF', '#D3D3D3', '#FFB6C1', '#FFA07A', '#87CEFA', '#B0C4DE',
'#32CD32', '#800000', '#66CDAA', '#BA55D3', '#3CB371', '#7B68EE',
'#00FA9A', '#48D1CC', '#C71585', '#808000', '#FFA500', '#FF4500',
'#98FB98', '#DDA0DD', '#B0E0E6', '#FF0000', '#BC8F8F', '#4169E1',
'#8B4513', '#FA8072', '#F4A460', '#2E8B57', '#A0522D', '#C0C0C0',
'#4682B4', '#D2B48C', '#FF6347', '#EE82EE', '#FFFF00', '#9ACD32']


def miesanie(karty):
    """ funkcia pomieša farby
    náhodne sa vyberú dve karty, a navzájom sa vymenia,
    cyklus sa opakuje počtom kariet
    hrozí súčasný výber tej istej karty! """
    pocet_kariet = len(karty)
    for i in range(pocet_kariet):
        a = randint(0, pocet_kariet - 1)
        b = randint(0, pocet_kariet - 1)
        if a == b:
            # Čo by sa stalo ak by tu táto podmienka nebola?
            continue
        karty[a], karty[b] = karty[b], karty[a]


def karta(i, x, y): # oprava chyby v tagu, prepísanie na farbu
    """ funkcia na vytvorenie kariet
    s popiskom PEXESO (+-45°) a priradenie tagov """
    canvas.create_rectangle(
        -(configuration[1] - 5) + x * configuration[1],
        -(configuration[1] - 5) + y * configuration[1],
        -1 + x * configuration[1],
        -1 + y * configuration[1],
        fill = 'green',
        outline = 'white',
        width = 4,
        tags = f'karta{i}')

    for s in 45, 315:
        canvas.create_text(
            -(configuration[1] // 2 - 2) + (x * configuration[1]),
            -(configuration[1] // 2 - 2) + (y * configuration[1]),

            font = (configuration[2], configuration[3]),

            fill = 'white',
            angle = s,
            text = 'PE  / ESO',
            tags = f'karta{i}')

    canvas.tag_bind(
        f'karta{i}',
        "<Button-1>",
        clicked)


def clicked(event):
    """ funkcia na obsluhu klikacej udalosti """
    if len(card_array) < 2:
        current = event.widget.find_withtag("current")[0] # toto: event.widget.find_withtag by potrebovalo vysvetlenie
        try:
            angle = event.widget.itemcget(current, 'angle')
        except:
            angle = ''

        color = colors(current, angle)
        card_array.append((current, angle, color))

        from_to = from_to_range(angle)
        for i in from_to:
            try:
                event.widget.itemconfig(current + i, fill = color, outline = color)
            except:
                event.widget.itemconfig(current + i, fill = color)

        string(color)

        if len(card_array) == 2:
            count()


def colors(current, angle = ''):
    """ funkcia vráti farbu,
    ktorá náleží danej karte - canvas_rectangle
    alebo popisku karty - canvas_text """
    if angle == '315.0':
        current -= 1
    color = farby_kariet[current // 3]
    return color


def from_to_range(angle):
    """ funkcia na základe uhla zistí
    či sa jedná o canvas_rectangle alebo canvas_text
    a vrári range tagov napr.:
        range(-1, 2) -> current - 1, current, current + 1 """
    if angle == '45.0':
        return range(-1, 2)
    elif angle == '315.0':
        return range(-2, 1)
    return range(0, 3)


def string(color):
    """ funkcia vypíše farbu na plochu (color label) """
    if color == None:
        canvas.itemconfig('color', text = '')
        return
    canvas.itemconfig('color', text = color_config.get('farby', color[1:]))
    # label.config(text = farby[color])


def count():
    """ funkcia vyhodnotí návratovú hodnotu funkcie is_pair()
    ak je návratová hodnota:
        None - uvoľní sa klikanie (nič sa nevykoná)
        True - po "čase" sa zavolá funkcia score() na započítanie páru
        False - po "čase" sa zavolá funkcia to_face() na otočenie kariet """
    pair = is_pair()
    if pair == None:
        return
    elif pair:
        canvas.after(500, score)
        return
    canvas.after(1000, to_face)


def is_pair():
    """ funkcia zistí či sa jedná o pár kariet
    ak bola zvolená identická karta
    odstráni sa duplikát z poľa (card_array) """
    current0, angle0, color0 = card_array[0]
    current1, angle1, color1 = card_array[1]
    if color0 == color1:
        from_to0 = from_to_range(angle0)
        from_to1 = from_to_range(angle1)
        if (current0 + from_to0[0] >= current1 + from_to1[0]) and (current0 + from_to0[1] <= current1 + from_to1[1]):
            # bug úspešne odstránený
            card_array.pop() # zamedzí odstráneniu karty po opätovnom kliknutí na tú istú kartu
            return None
        return True
    return False


def to_face():
    """ funkcia na otočenie kariet
    pričom zmenená farba indikuje,
    že daná karta už bola v minulosti otočená
    Následne sa vymaže popis farby z plochy (color label) """
    for i in range(len(card_array)):
        current, angle, color = card_array.pop()

        from_to = from_to_range(angle)
        for i in from_to:
            try:
                canvas.itemconfig(current + i, fill = 'green', outline = 'white')
            except:
                canvas.itemconfig(current + i, fill = 'yellow')
    string(None) # color text => ''


def score():
    """ funkcia na započítanie skóre,
    odstránenie kariet z plochy
    a výpis započítaného skóre na plochu (label) """
    score_array[0] += 1
    for a in range(len(card_array)):
        current, angle, color = card_array.pop()

        from_to = from_to_range(angle)
        for i in from_to:
            canvas.delete(current + i)
    canvas.itemconfig('score', text = f'score: {score_array[0]: 4}')
    string(None) # color text => ''

root = Tk()
root.title("Pexeso")
# root.iconbitmap("Hry/Pexeso/logo.ico")
canvas = Canvas(width = 800, height = 600, background = 'green')
canvas.pack(side = LEFT)

pocet = 4  # hracie pole 4 * 4
# pocet = 6  # hracie pole 6 * 6
# pocet = 8  # hracie pole 8 * 8
# pocet = 10 # hracie pole 10 * 10
# pocet = 12 # hracie pole 12 * 12

# náhodný výber fontu
fonts = {
    0 : ("Rage Italic", 2),
    1 : ("Pristina", 2),
    2 : ("MV Boli", 0),
    3 : ("Monotype Corsiva", 2),
    4 : ("Mistral", 4),
    5 : ("Lucida Handwriting", 0),
    6 : ("Freestyle Script", 4),
    7 : ("Forte", 2),
    8 : ("Segoe Print", 0),
    9 : ("Segoe Script", 0)}

nahodne_cislo = randint(0, 9)

# [pole farieb, rozmer pre kartu, typ fontu, veľkosť fontu]
configuration = {
    4  : [farby_kariet4, 150, fonts[nahodne_cislo][0], fonts[nahodne_cislo][1] + 24],
    6  : [farby_kariet6, 100, fonts[nahodne_cislo][0], fonts[nahodne_cislo][1] + 16],
    8  : [farby_kariet8,  75, fonts[nahodne_cislo][0], fonts[nahodne_cislo][1] + 12],
    10 : [farby_kariet10, 60, fonts[nahodne_cislo][0], fonts[nahodne_cislo][1] +  8],
    12 : [farby_kariet12, 50, fonts[nahodne_cislo][0], fonts[nahodne_cislo][1] +  6]}

configuration = configuration[pocet]
card_array = []
score_array = [0]
color = 0

farby_kariet = configuration[0]

farby_kariet += farby_kariet
miesanie(farby_kariet)

for y in range(1, 1 + pocet):
    for x in range(1, 1 + pocet):
        # i = x * y # chybný vzorec a predsa to funguje správne
        i = x + ((y - 1) * pocet)
        karta(i, x, y)


canvas.create_rectangle(700 - 75, 50 - 12, 700 + 75, 50 + 12, fill = "white", outline = "yellow", width = 2)
canvas.create_text(700, 50, text = f'score: {score_array[0]: 4}', tags = 'score')

canvas.create_rectangle(700 - 75, 150 - 12, 700 + 75, 150 + 12, fill = "white", outline = "yellow", width = 2)
canvas.create_text(700, 150, text = '', tags = 'color')

# label = Label(root, fg = "dark green", pady = 25, width = 25, wraplength = 120)
# label.pack()
# label_timer = Label(root, fg = "dark green", pady = 25, width = 25, wraplength = 120, text = "0 s")
# label_timer.pack()

# button = Button(root, text = 'Stop', width = 25, command = canvas.delete("all"))
# button.pack()
root.mainloop()

"""
vytvoriť prípadne časovač a počet kliknutí, počítanie úspešnosti
vytvoriť tlačidlo na novú hru
umožniť výber hracej plochy (počet kariet)
ak je možné pridať ďalšieho hráča (prípadne počitač)
ak je možné pridať ikonu
vytvoriť .exe súbor
"""

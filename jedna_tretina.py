



""" suma = 0.0
for i in range(1, 401): # 5.998787255582524e-241          -> 1/4^399, výsledok = 0.3333333333333333
    suma += 1/4 ** i
    print(f"{1/4 ** i}\t\t-> 1/4^{i}, výsledok = {suma}") # od 1/27 sa opakuje: výsledok = 0.3333333333333333 // 16 desatinných miest // max je 1/3*10e307
 """

""" suma = 0.0
for i in range(500, 539): # 5.998787255582524e-241          -> 1/4^399, výsledok = 0.3333333333333333
    suma += 1/4 ** i
    print(f"{1/(4 ** i)}\t\t-> 1/4^{i}, výsledok = {suma}") # od 1/27 sa opakuje: výsledok = 0.3333333333333333 // 16 desatinných miest // max je 1/3*10e307
    if i == 5 or i % 10 == 0: #if i % 5 == 0:
        print()
        suma = 0.0 """


# nulovanie: suma = 0.0
# 2.0237e-320             -> 1/4^531, výsledok = 2.0237e-320
# 5.06e-321               -> 1/4^532, výsledok = 2.5296e-320
# 1.265e-321              -> 1/4^533, výsledok = 2.656e-320
# 3.16e-322               -> 1/4^534, výsledok = 2.6877e-320
# 8e-323          -> 1/4^535, výsledok = 2.6956e-320
# 2e-323          -> 1/4^536, výsledok = 2.6976e-320
# 5e-324          -> 1/4^537, výsledok = 2.698e-320
# 0.0             -> 1/4^538, výsledok = 2.698e-320





# print(((2**536)**2)) # 1/4^536
# print(1/50600563326827654588123836679729326762389162441035529589225339506857584891998836722990095925359281123796769466079202977847452184346448369216753349985184627480379356069141590341116726935523304085309941919618186267140501870856173174654525838912289889085202514128089692388083353653807625633046581877161501565826926935273373696)

""" for i in range(1, 539): # 5.998787255582524e-241          -> 1/4^399, výsledok = 0.3333333333333333
    print(f"{4 ** i}\t\t-> 4^{i}") # od 1/27 sa opakuje: výsledok = 0.3333333333333333 // 16 desatinných miest // max je 1/3*10e307
    if i == 5 or i % 10 == 0: #if i % 5 == 0:
        print() """



import tkinter
suma = 0
pocet_opakovani = 28

def zlomok(delenec, delitel, mocnina_delitela, znamienko = "", vysledok = ""):
    try:
        x0, y0, x, y = 100 + 55 * mocnina_delitela, 350, 14, 14
    except:
        x0, y0, x, y = 100 + 55 * 0, 350, 14, 14

    canvas.create_text(x0, y0 - y, text = delenec, font = ("Arial", 12))
    canvas.create_line(x0 - x, y0, x0 + x, y0)
    canvas.create_text(x0 - x / 2, y0 + y, text = delitel, font = ("Arial", 12))
    canvas.create_text(x0 + x / 2, y0 + y / 2, text = mocnina_delitela, font = ("Arial", 8))
    canvas.create_text(x0 + 2 * x, y0, text = znamienko)

    canvas.create_text(x0, y0 - 3 * y, text = vysledok, font = ("Arial", 12), anchor="nw", angle = 90)

canvas = tkinter.Canvas(bg = 'white', width = 1800, height = 600)
canvas.pack()


def vypocet_zlomku(i, znamienko):
#        print(f"{1/(4 ** i)}\t\t-> 1/4^{i}, výsledok = {suma}")
        vysledok = 1/(4 ** i)
        zlomok(1, 4, i, znamienko, vysledok)
        return vysledok

zlomok(1, 3, "", znamienko = "=")
for i in range(1, 28):
    if i < pocet_opakovani - 1:
        vysledok = vypocet_zlomku(i, "+")
    else:
        vysledok = vypocet_zlomku(i, "")
    suma += vysledok
    print(f"{vysledok}\t\t-> 1/4^{i}, výsledok = {suma}")

tkinter.mainloop()




import json
from operator import itemgetter
import tkinter as tk
import tkinter.ttk as ttk


class JSON():
    def __init__(self):
        try:
            self.subor_json = json.loads(open("diar.json", "r").read())
        except:
            self.subor_json = []

    def reading(self):
        print(f'{"Záznam:":25}{"Dátum:":15}{"Stav:"}')
        # subor_json = ''
        # string = ''
        for z in self.subor_json:
            print(f'{z["zaznam"]:25}{z["den"]:15}{z["splnene"]}')
            # string += f'{(z["zaznam"]):25}{(z["den"]):15}{z["splnene"]}\n'
        print()
        print(self.subor_json)
        # return self.subor_json

    def add_line(self, zaznam, den):
        data = {"zaznam": zaznam, "den": den, "splnene": False}
        self.subor_json.append(data)

    def add_new_line(self):
        data = {}
        zaznam = input("Zadaj názov: ")
        den = input("Zadaj dátum: ")
        data = {"zaznam": zaznam, "den": den, "splnene": False}
        self.subor_json.append(data)

    def sorting(self, item, reversed):
        self.subor_json = sorted(self.subor_json, key = itemgetter(item), reverse = reversed)

    def update_line(self, zaznam, co, data):
        for z in self.subor_json:
            if z["zaznam"] == zaznam: # upraviť na 0 + 1
                z[co] = data

    def _write(self):
        # print(self.subor_json)
        # export = sorted(self.subor_json, key = itemgetter("den"), reverse = False)
        # print(export)
        subor = open("diar.json", "w")
        # subor.write(json.dumps(export, indent = 4))
        # subor.write(json.dumps(self.subor_json, indent = 4))
        subor.write(json.dumps(self.subor_json, indent = 4))
        subor.close()










# class Application(tk.Tk):
#     def __init__(self):
#         super().__init__(self)
#         self.title('Diár')
#         self.objekt_json = JSON()
#         self.grid()
#         self.createWidgets()

#     def createWidgets(self):
#         # self.splneneLabel = tk.Label(self, text = "Splnené:").grid()
#         self.splneneCheckbutton = ttk.Checkbutton(self, text = "Splnené")#.grid(row = 2, column = 1)
#         self.windowBox = tk.Message(self, width = 240, text = f'{"Záznam:":25}{"Dátum:":15}{"Stav:"}')#.grid(row = 3, columnspan = 2)
#         # self.listBox = tk.Listbox(self).grid()
#         """
#         The width of the widget in characters (not pixels!), measured according to the current font size.

#         Set wrap=WORD and it will break the line after the last word that will fit.
#         With the default behavior, wrap=CHAR, any line that gets too long will be broken at any character.
#         """
#         self.textBox = tk.Text(self, name = "vystup", padx = 5, width = 50, yscrollcommand = set())#.grid(row = 4, columnspan = 2)
#         # self.splnene1Checkbutton = tk.Checkbutton(self.textBox, text = "Splnené").grid()

#         self.quitButton = ttk.Button(self, text = 'Quit', command = self.quit)#.grid(row = 5, column = 1)
#         self.pridatButton = ttk.Button(self, text = "Pridať", command = self.pridat())
#         self.upravitButton = ttk.Button(self, text = "Upraviť", command = self.upravit())


#         self.zaznamLabel.grid(row = 0, column = 0)
#         self.zaznamInput.grid(row = 0, column = 1)
#         self.datumLabel.grid(row = 1, column = 0)
#         self.datumInput.grid(row = 1, column = 1)
#         # self.splneneLabel.grid()
#         self.splneneCheckbutton.grid(row = 2, column = 1)
#         self.windowBox.grid(row = 3, columnspan = 4)
#         # self.listBox.grid()
#         self.textBox.grid(row = 4, columnspan = 4)
#         # self.splnene1Checkbutton.grid()

#         self.quitButton.grid(row = 5, column = 1)
#         self.pridatButton.grid(row = 1, column = 2)
#         self.upravitButton.grid(row = 1, column = 3)


def pridat():
    """ okno pre formulár pre pridanie zápisu """
        # zaznam = self.zaznamInput
        # den = self.datumInput
        # self.objekt_json.add_line(zaznam, den)
        # # self.objekt_json._write()
        # self.vypis()
    # pridať selekt/focus pre zadanie textu a možnosť entrovania (Zapísať)
    window_pridat = tk.Toplevel()
    zaznamLabel = ttk.Label(window_pridat, text = "Záznam:")
    zaznamInput = ttk.Entry(window_pridat)
    datumLabel = ttk.Label(window_pridat, text = "Dátum:")
    datumInput = ttk.Entry(window_pridat, name = "datumInput")

    zaznamLabel.grid(row = 0, column = 0)
    zaznamInput.grid(row = 0, column = 1)
    datumLabel.grid(row = 1, column = 0)
    datumInput.grid(row = 1, column = 1)
    
    zatvoritButton = ttk.Button(window_pridat, text = "Zapísať", command = lambda: (
        textBox.insert(0, zaznamInput.get() + datumInput.get() + "False" + '\n'),
        window_pridat.destroy()) # prečo treba zátvorky?
    )
    zatvoritButton.grid(row = 5, column = 1)

def upravit():
    # zaznam, co ,data = None, None, None
    # self.objekt_json.update_line(zaznam, co, data)
    # self.vypis()
    pass

def vypis(self):
    # subor_json = self.objekt_json.reading()
    # for z in subor_json:
    #     # self.textBox.insert(f'1.0',f'{z["zaznam"]:25}{z["den"]:15}{z["splnene"]}\n')
    #     # text_string = f'{z["zaznam"]:25}{z["den"]:15}{z["splnene"]}\n'
    #     # text_string = z["zaznam"], z["den"], z["splnene"]
    #     text_string = str(z["zaznam"]) + '\t'*3 + str(z["den"]) + '\t'*2 + str(z["splnene"]) + '\n' # TOTO potrebuje ďalšie vysvetlenie
    #     self.textBox.insert('1.0', text_string)
    pass


root = tk.Tk()
root.title('Diár')
root.grid()




textBox = tk.Listbox(root, width = 50)
textBox.grid(row = 4, columnspan = 4)

pridatButton = ttk.Button(root, text = "Pridať", command = lambda: pridat())
pridatButton.grid(row = 5, column = 1)
upravitButton = ttk.Button(root, text = "Upraviť", command = lambda: upravit())




# objekt_json = JSON()
# objekt_json.reading()

# objekt_json.update_line("druhy", "zaznam","upraveny_druhy_zaznam")
# objekt_json.update_line("upraveny_druhy_zaznam", "den", "1.6.2022")
# objekt_json.update_line("skusobny", "splnene", True)

# objekt_json.add_line("treti", "24.3.2018")

# objekt_json.write()

# objekt_json.add_new_line()
# objekt_json.sorting("den", True)

# objekt_json.write()
# objekt_json.reading()

root.mainloop()

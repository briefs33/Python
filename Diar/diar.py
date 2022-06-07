import json
from operator import itemgetter
import tkinter as tk
import tkinter.ttk as ttk


class JSON():
    def __init__(self):
        try:
            self.subor_json = json.loads(open("Diar/diar.json", "r").read())
        except:
            self.subor_json = []

    def reading(self):
        # print(f'{"Záznam:":25}{"Dátum:":15}{"Stav:"}')
        # subor_json = ''
        # # string = ''
        # for z in self.subor_json:
        #     print(f'{z["zaznam"]:25}{z["den"]:15}{z["splnene"]}')
        #     # string += f'{(z["zaznam"]):25}{(z["den"]):15}{z["splnene"]}\n'
        # print()
        # print(self.subor_json)
        # return self.subor_json

        # root.textBox.destroy?
        text_string = ''
        for z in self.subor_json:
            # self.textBox.insert(f'1.0',f'{z["zaznam"]:25}{z["den"]:15}{z["splnene"]}\n')
            text_string = f'{z["zaznam"]:25}{z["den"]:15}{z["splnene"]}\n'
            # text_string = z["zaznam"], z["den"], z["splnene"]
            # text_string = str(z["zaznam"]) + '\t'*3 + str(z["den"]) + '\t'*2 + str(z["splnene"]) + '\n' # TOTO potrebuje ďalšie vysvetlenie
        root.textBox.insert(0, text_string)

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

    def write(self):
        # print(self.subor_json)
        # export = sorted(self.subor_json, key = itemgetter("den"), reverse = False)
        # print(export)
        subor = open("Diar/diar.json", "w")
        # subor.write(json.dumps(export, indent = 4))
        subor.write(json.dumps(self.subor_json, indent = 4))
        subor.close()




class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Diár')
        self.objekt_json = JSON()
        self.grid()
        self.window_root()

    def window_root(self):
        self.textBox = tk.Listbox(self, width = 50)
        self.textBox.grid(row = 4, columnspan = 4)

        self.pridatButton = ttk.Button(self, text = "Pridať", command = lambda: Pridat().focus())
        self.pridatButton.grid(row = 5, column = 1)
        self.upravitButton = ttk.Button(self, text = "Upraviť", command = lambda: Upravit().focus())
        self.upravitButton.grid(row = 5, column = 3)

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
#         # self.splneneLabel.grid()
#         self.splneneCheckbutton.grid(row = 2, column = 1)
#         self.windowBox.grid(row = 3, columnspan = 4)
#         # self.listBox.grid()
#         self.textBox.grid(row = 4, columnspan = 4)
#         # self.splnene1Checkbutton.grid()


class Pridat(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Pridanie záznamu')
        self.grid()
        self.window_pridat()

    def window_pridat(self):
        """ okno pre formulár pre pridanie zápisu """
        # pridať selekt/focus pre zadanie textu a možnosť entrovania (Zapísať)
        # window_pridat = tk.Toplevel()
        zaznamLabel = ttk.Label(self, text = "Záznam:")
        zaznamInput = ttk.Entry(self, name = "zaznamInput")
        datumLabel = ttk.Label(self, text = "Dátum:")
        datumInput = ttk.Entry(self, name = "datumInput")

        zaznamLabel.grid(row = 0, column = 0)
        zaznamInput.grid(row = 0, column = 1)
        datumLabel.grid(row = 1, column = 0)
        datumInput.grid(row = 1, column = 1)
        
        zatvoritButton = ttk.Button(self, text = "Zapísať", command = lambda: (
            root.textBox.insert(0, zaznamInput.get() + datumInput.get() + "False" + '\n'),
            self.destroy()) # prečo treba zátvorky?
        )
        zatvoritButton.grid(row = 5, column = 1)

        # self.objekt_json.add_line(zaznam, den)
        # # self.objekt_json._write()
        # self.vypis()


class Upravit(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Upravenie záznamu')
        self.grid()
        self.window_upravit()

    def window_upravit(self):
        # zaznam, co ,data = None, None, None
        # self.objekt_json.update_line(zaznam, co, data)
        # self.vypis()
        pass







root = Root()
root.objekt_json.reading()


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

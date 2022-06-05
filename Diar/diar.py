import json
from operator import itemgetter
import tkinter as tk
import tkinter.ttk as ttk


def pridat():
    textBox.insert(0, zaznamInput.get() + '\n')




root = tk.Tk()
root.title('Diár')
root.grid()

zaznamLabel = ttk.Label(root, text = "Záznam:")
zaznamInput = ttk.Entry(root)

zaznamLabel.grid(row = 0, column = 0)
zaznamInput.grid(row = 0, column = 1)

textBox = tk.Listbox(root, width = 50)
textBox.grid(row = 4, columnspan = 4)

pridatButton = ttk.Button(root, text = "Pridať", command = pridat)
pridatButton.grid(row = 5, column = 1)


root.mainloop()

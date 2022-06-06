import json
from operator import itemgetter
import tkinter as tk
import tkinter.ttk as ttk


def pridat():
    window_pridat = tk.Toplevel()
    zaznamLabel = ttk.Label(window_pridat, text = "Záznam:")
    zaznamInput = ttk.Entry(window_pridat)

    zaznamLabel.grid(row = 0, column = 0)
    zaznamInput.grid(row = 0, column = 1)
    
    zatvoritButton = ttk.Button(window_pridat, text = "Zapísať", command = lambda: (
        textBox.insert(0, zaznamInput.get() + '\n'),
        window_pridat.destroy())
    )
    zatvoritButton.grid(row = 5, column = 1)



root = tk.Tk()
root.title('Diár')
root.grid()

textBox = tk.Listbox(root, width = 50)
textBox.grid(row = 4, columnspan = 4)

pridatButton = ttk.Button(root, text = "Pridať", command = lambda: pridat())
pridatButton.grid(row = 5, column = 1)


root.mainloop()

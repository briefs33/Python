from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Kalkulačka")

entry = Entry(root, width = 35)
entry.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

def button_click(number):
    # entry.delete(0, END)
    entry.insert(END, number)

def button_clear():
    entry.delete(0, END)

buttons = {
    1           : ["1", 20, 10, lambda: button_click(1), 4, 0, None, None],
    2           : ["2", 20, 10, lambda: button_click(2), 4, 1, None, None],
    3           : ["3", 20, 10, lambda: button_click(3), 4, 2, None, None],
    5           : ["5", 20, 10, lambda: button_click(4), 3, 0, None, None],
    6           : ["6", 20, 10, lambda: button_click(5), 3, 1, None, None],
    7           : ["7", 20, 10, lambda: button_click(6), 3, 2, None, None],
    4           : ["4", 20, 10, lambda: button_click(7), 2, 0, None, None],
    8           : ["8", 20, 10, lambda: button_click(8), 2, 1, None, None],
    9           : ["9", 20, 10, lambda: button_click(9), 2, 2, None, None],
    0           : ["0", 47, 10, lambda: button_click(0), 5, 0, 2, None],
    "plus"      : ["+", 20, 32, button_click, 2, 3, None, 2],
    "minus"     : ["-", 22, 10, button_click, 1, 3, None, None],
    "krat"      : ["*", 20, 10, button_click, 1, 2, None, None],
    "deleno"    : ["/", 20, 10, button_click, 1, 1, None, None],
    "clear"     : ["C", 20, 32, button_clear, 4, 3, None, 2]}

for i in buttons:
    Button(
        root, text = buttons[i][0], padx = buttons[i][1], pady = buttons[i][2], command = buttons[i][3]
    ).grid(
        row = buttons[i][4], column = buttons[i][5], columnspan = buttons[i][6], rowspan = buttons[i][7]
    )














root.mainloop()

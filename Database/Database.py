from tkinter import *
from tkinter import ttk

import numpy as np
import re

def database_file():
    records = np.array([])

    my_file = input("enter name of file: ")
    symbol = input("enter symbol: ")

    headers = 0
    counter = 0

    with open(my_file, "r") as file:
        for i in file:
            counter += 1
            clean = re.split(symbol, i)
            headers = len(clean)
            
            for ii in clean:
                if ii != "":
                    records = np.append(records, ii)

    records.resize(counter, headers)

    return records

def database_input():
    db = np.array([])
    records = np.array([])

    rows = int(input("enter number of rows: "))
    columns = int(input("enter number of columns: "))

    for i in range(1, columns + 1):
        column_name = input("enter column name " + str(i) + ": ")
        db = np.append(db, column_name)
        records = np.append(records, column_name)

    for i in range(1, rows + 1):
        for ii in db:
            data = input("enter data for " + ii + " (" + str(i) + "): ")
            records = np.append(records, data)

    records.resize(rows + 1, columns)

    return records

def gui():
    my_array = database_file()

    window = Tk()
    tree = ttk.Treeview(window, column = my_array[0], show = "headings", height = 25)

    tables = -1

    for i in my_array[0]:
        tables += 1
        tree.column(tables, anchor = CENTER)
        tree.heading(tables, text = i)

    count = -1

    for i in my_array:
        count += 1
        if count >= 1:
            tree.insert("", "end", text = count, values = tuple(i,))

    tree.pack()

    window.mainloop()

#print(database_file())
gui()

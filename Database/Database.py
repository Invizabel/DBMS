from tkinter import *
from tkinter import ttk

import numpy as np
import re

#global variables
global delimiter
global label_delimiter
global label_open_txt_file
global open_txt_file
global window_display_txt_file
global window_open_txt_file

def engine_txt_file():
    my_file = open_txt_file.get()
    symbol = delimiter.get()
    
    records = np.array([])

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

    display_txt_file(records)

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

def display_txt_file(my_array):
    window_display_txt_file = Tk()
    window_display_txt_file.title("DBMS")

    window_open_txt_file.destroy()

    #start
    tree = ttk.Treeview(window_display_txt_file, column = my_array[0], show = "headings", height = 25)

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
    window_display_txt_file.mainloop()

def open_txt_file():
    #global variables
    global delimiter
    global label_delimiter
    global label_open_txt_file
    global open_txt_file
    global window_display_txt_file
    global window_open_txt_file

    window_open_txt_file = Tk()
    window_open_txt_file.title("DBMS")
    
    label_open_txt_file = Label(window_open_txt_file, text = "open txt file")
    label_open_txt_file.pack()

    open_txt_file = Entry(window_open_txt_file, width = 40)
    open_txt_file.pack()

    label_delimiter = Label(window_open_txt_file, text = "delimiter")
    label_delimiter.pack()

    delimiter = Entry(window_open_txt_file, width = 40)
    delimiter.pack()

    ttk.Button(window_open_txt_file, text = "ok", width = 20, command = engine_txt_file).pack()

    window_open_txt_file.mainloop()

open_txt_file()

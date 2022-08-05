from tkinter import *
from tkinter import ttk

import numpy as np
import re

#global variables
global data
global delimiter
global focus
global main
global open_txt_file
global tree

main = Tk()
main.title("DBMS")

def engine_txt_file():
    #global variables
    global column
    global data
    global delimiter
    global main
    global open_txt_file
    global tree

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

    db(records)
    
def edit(event):
    #global variables
    global data

    my_list = []

    result = data.get()

    column = tree.identify_column(event.x)
    clean = column.replace("#", "")
    
    cursor = tree.focus()
    cursor_dict = tree.item(cursor)

    counter = 0
    for i in cursor_dict["values"]:
        counter += 1

        if counter != int(clean):
            my_list.append(i)

        if counter == int(clean):
            my_list.append(result)
            
    try:
        edit_entry = tree.selection()[0]
        tree.item(edit_entry, text = "edit", values = my_list)

    except IndexError:
        pass

def db(my_array):
    #global variables
    global data
    global delimiter
    global focus
    global main
    global open_txt_file
    global tree
    
    #window
    main.destroy()
    main = Tk()
    main.title("DBMS")

    data = Entry(main, width = 40)
    data.pack()

    #start
    tree = ttk.Treeview(main, column = my_array[0], show = "headings", height = 25)

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

    main.bind("<Button 1>", edit)

    main.mainloop()

def open_txt_file():
    #global variables
    global data
    global delimiter
    global focus
    global main
    global open_txt_file
    global tree
    
    #window
    main.destroy()
    main = Tk()
    main.title("DBMS")

    #start
    label_open_txt_file = Label(main, text = "open txt file")
    label_open_txt_file.pack()

    open_txt_file = Entry(main, width = 40)
    open_txt_file.pack()

    label_delimiter = Label(main, text = "delimiter")
    label_delimiter.pack()

    delimiter = Entry(main, width = 40)
    delimiter.pack()

    ttk.Button(main, text = "ok", width = 20, command = engine_txt_file).pack()

    main.mainloop()

open_txt_file()

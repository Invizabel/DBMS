from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

import numpy as np
import os
import pandas as pd
import re

#global variables
global data
global delimiter
global focus
global main
global open_txt_file
global records
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
    global records
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

def my_event(event):
    #global variables
    global data

    result = data.get()

    if "edit:" in result:
        edit(event)

    if "filter:" in result:
        my_filter(event)

def edit(event):
    #global variables
    global data

    my_list = []

    result = data.get()
    result = result.replace("edit:", "")

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

def my_filter(event):
    #global variables
    global data
    global records

    new_records = np.array([])

    result = data.get()
    result = result.replace("filter:", "")
    result = result.replace("\n", "")

    counter = 0
    tracker = 0
    
    for i in records:
        headers = len(i)
        tracker += 1

        if tracker == 1:
            new_records = np.append(new_records, i)

        for ii in range(len(i)):
            i[ii] = i[ii].replace("\n", "")

            if result.lower() in i[ii].lower():
                counter += 1
                new_records = np.append(new_records, i)

    new_records.resize(counter + 1, headers)

    db(new_records)

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

    main.bind("<Button 1>", my_event)

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

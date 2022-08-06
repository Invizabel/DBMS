from kivy.app import App
from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

import kivy
import numpy as np
import os
import re

class DBMS(App):
    #home page
    def build(self, delimiter = "\"", my_array = np.array([]), my_file = "States.txt", my_font = 18):
        if len(my_array) > 0:
            records = my_array
            headers = len(records[0])

        else:
            records = self.open_txt_file()

            if os.path.isfile(my_file):
                with open(my_file, "r") as file:
                    for i in file:
                        clean = re.split(delimiter, i)
                        headers = len(clean)

            else:
                with open("States.txt", "r") as file:
                    for i in file:
                        clean = re.split(delimiter, i)
                        headers = len(clean)

        self.layout = GridLayout(cols = headers, spacing = 5, size_hint_y = None)
        self.layout.bind(minimum_height = self.layout.setter("height"))

        self.entry = TextInput(text = "", multiline = False)
        self.layout.add_widget(self.entry)

        self.ok = Button(text = "ok")
        self.layout.add_widget(self.ok)
        self.ok.bind(on_press = self.hub)

        for i in range(headers - 2):
            self.my_button = Button(text = "", size_hint_y = None, height = 50, font_size = my_font)
            self.layout.add_widget(self.my_button)

        for i in records:
            for ii in i:
                self.my_button = Button(text = ii, size_hint_y = None, height = 50, font_size = my_font)
                self.layout.add_widget(self.my_button)

        self.my_scroll = ScrollView(size_hint = (1, 1), size = (Window.width, Window.height))
        self.my_scroll.add_widget(self.layout)

        runTouchApp(self.my_scroll)

        return self.layout

    def hub(self, btn):
        self.layout.clear_widgets()

        if "file:" in self.entry.text:
            clean = self.entry.text.replace("file:", "")
            self.build(my_file = clean)

        if "filter:" in self.entry.text:
            self.my_filter()

    def my_filter(self):
        new_records = np.array([])

        result = self.entry.text
        result = result.replace("filter:", "")

        counter = 0
        tracker = 0

        records = self.open_txt_file()
        
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

        self.build(my_array = new_records)
            
    def open_txt_file(self, delimiter = "\"", my_file = "States.txt"):
        records = np.array([])

        headers = 0
        counter = 0

        if os.path.isfile(my_file):
            with open(my_file, "r") as file:
                for i in file:
                    counter += 1
                    clean = re.split(delimiter, i)
                    headers = len(clean)
                    
                    for ii in clean:
                        if ii != "":
                            records = np.append(records, ii)

        else:
            with open("States.txt", "r") as file:
                for i in file:
                    counter += 1
                    clean = re.split(delimiter, i)
                    headers = len(clean)
                    
                    for ii in clean:
                        if ii != "":
                            records = np.append(records, ii)

        records.resize(counter, headers)

        return records
    
main = DBMS()
main.run()

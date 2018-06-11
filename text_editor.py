from tkinter import *
from tkinter import filedialog
import tkinter as tk
canvas = Tk()


class text_editize:
    def __init__(self, main, font_pack=['Courier']):
        self.main = main
        self.fonts = font_pack
        self.title = main.title("Basic Text Editor")
        self.text_init()

    def quit(self):
        self.main.destroy()

    def text_init(self):
        self.text = Text(self.main)
        self.f_val = -1
        self.font_switch()
        self.text.grid()

    def open(self, start):
        global text
        openlocation = filedialog.askopenfilename()
        try:
            f = open(openlocation, "rw")
        except BaseException:
            print("Can't open!")
            return
        self.data = f.readlines()
        f.close()
        self.compiled = ''
        for m in self.data:
            self.compiled += m
        if start:
            self.text.insert(start, self.compiled)
        else:
            self.text.insert(1.0, self.compiled)
#           self.text.insert(END, '\n')
#           self.text.insert(END, self.compiled)

    def saving(self):
        self.content = self.text.get(1.0, END)
        savelocation = filedialog.asksaveasfilename()
        try:
            f = open(savelocation, "w+")
            f.write(self.content)
            f.close()
        except BaseException:
            print("Couldn't save!")

    def font_switch(self, incr=1):
        lent = len(self.fonts)
        self.f_val += incr
        self.text.config(font=self.fonts[self.f_val % lent])


# Dependant class
class dashboard:
    def __init__(self, main, homebox):
        self.main = main
        self.homebox = homebox
        self.text = self.homebox.text
        self.numberize()
        self.fun = {
            "delete": self.delete_lines,
            "save": self.homebox.saving,
            "open": self.open,
            "quit": self.quit,
            "font+": self.font_switch,
            "font-": self.font_switch,
            "reset": self.delete_lines,
            "!numberize": self.numberize,
            "!commands": self.commands,
        }
        self.e = Entry()
        self.e.grid(row=1)
        self.commandbtn = Button(main, text="Enter", command=self.gofigure)
        self.commandbtn.grid(row=2)

    def gofigure(self):
        entry = self.e.get()
        self.ie = entry.split()
        try:
            self.fun[self.ie[0].lower()]()
            print(self.ie[0].upper())
        except BaseException:
            print("No Command / Error!")

    def quit(self):
        self.main.destroy()

    def open(self):
        try:
            start = float(self.ie[1])
        except BaseException:
            start = 0
        self.homebox.open(start)

    def delete_lines(self):
        try:
            entry = self.ie[1].lower()
            if entry == "all":
                self.text.delete(1.0, END)
            elif '-' in entry:
                entry = entry.split("-")
                self.text.delete(float(entry[0]), float(entry[1])+1)
            elif ',' in entry:
                entry = entry.split(",")
                for i in range(len(entry)):
                    self.text.delete(float(entry[i])-i, float(entry[i])-i+1)
            else:
                self.text.delete(float(entry), float(entry)+1)
        except IndexError:
            if self.ie[0].lower() == "reset":
                self.text.delete(1.0, END)
                self.numberize()
        else:
            print("Specify Line or type 'all' for all.")

    def numberize(self):
        for i in range(1, 201):
            self.text.insert(float(i), str(i)+'\t\n')

    def font_switch(self):
        incr = 1
        if self.ie[0][-1] == '-':
            incr = -1
        self.homebox.font_switch(incr)

    def commands(self):
        for com in self.fun.keys():
            print(com)


# Fonts in (str name, int size=12, str style='normal')
fonts_list = [
    ('Courier'),
    ('Halvetica'),
    ('Times'),
    ('Symbol'),
    ('Courier', 16),
    ('Halvetica', 16),
    ]
mainText = text_editize(canvas, fonts_list)
Dash = dashboard(canvas, mainText)
canvas.mainloop()

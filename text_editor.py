from Tkinter import *
import tkFileDialog
import Tkinter as tk
canvas = Tk()

class text_editize:
 def __init__(self, main, font_pack = ['Courier']):
  self.main = main
  self.fonts = font_pack
  self.title = main.title("Basic Text Editor")
  self.text_init()
  self.quitbtn = Button(main, text = 'Quit!', command = self.quit)
  self.quitbtn.grid(row=3,column=1)
  self.openbtn = Button(main, text = 'Insert File', command = self.open)
  self.openbtn.grid(row=2)
  self.savebtn = Button(main, text = 'Save', command = self.saving)
  self.savebtn.grid(row=3)
  self.delbtn = Button(main, text = 'Delete', command = self.delete_line)
  self.delbtn.grid(row=2,column=1)
  self.fontbtn = Button(main, text = 'Font Swap',command = self.font_switch)
  self.fontbtn.grid(row=1,column=1)
  self.e = Entry()
  self.e.grid(row=1)
  #self.main.mainloop()?
 def quit(self):
  self.main.destroy()
 def text_init(self):
  self.text = Text(self.main)
  self.f_val = 0
  self.font_switch()
  self.text.grid()
 def open(self):
  global text
  openlocation = tkFileDialog.askopenfilename()
  try:
   f=open(openlocation,"rw")
  except:
   print("Can't open!")
   return
  self.data = f.readlines()
  f.close()
  self.compiled = ''
  for m in self.data:
    self.compiled += m
  try:
   start = float(self.e.get())
   self.text.insert(start, self.compiled)
  except:
   self.text.insert(END, '\n')
   self.text.insert(END, self.compiled)
 def saving(self):
  self.content = self.text.get(1.0, END)
  savelocation = tkFileDialog.asksaveasfilename()
  try:
   f = open(savelocation, "w+")
   f.write(self.content)
   f.close()
  except:
   print("Couldn't save!")
 def delete_line(self):
  try:
   start = float(self.e.get())
   self.text.delete(start, start+1)
  except:
   print("Specify Line!!!")
 def font_switch(self):
   l = len(self.fonts)
   self.text.config(font=self.fonts[self.f_val%l])
   self.f_val += 1

fonts_list = ['Courier', 'Halvetica', 'Times', 'Verdana']
text_editize(canvas, fonts_list)


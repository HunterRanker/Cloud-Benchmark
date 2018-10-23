
#! -*- coding: utf-8 -*-
import tkinter
root = tkinter.Tk()
root.title("My tools")
root.geometry('300x300+300+300')
def on_off():
   if btonoff['text'] == 'on':
       btonoff['text'] = 'off'
   else:
       btonoff['text'] = 'on'
btonoff = tkinter.Button(root, text="on", command=on_off)
btonoff.place(x=100, y=160, width=100, height=40)
root.mainloop()
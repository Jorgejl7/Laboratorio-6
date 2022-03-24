from tkinter import *
from tkinter import ttk
from led import * 


class Interface:
    def __init__(self, window)-> None:
        self.frame = window
        self.letters = StringVar()
        self.createLabel()

    def createLabel(self):
        self.w = Label(root, textvariable=self.letters).place(x=70, y = 90)

    def isExit(self, char):
        char = char.lower()
        return char == 'j' or char == 'J'

    
    def isValid(self, letters):
        letters = letters.lower()
        if letters == "ay" or letters == 'AY':
            print("LED Encendido")
            onLed()
            

    def clearLetters(self, letters):
        if len(letters) == 3:
            self.letters.set("")

    def close(self):
        self.frame.destroy()

    def key_pressed(self, event):
        if self.isExit(event.char): self.close();
        before_letters = self.letters.get()
        new_letters = before_letters + event.char 
        self.letters.set(new_letters)
        self.isValid(self.letters.get())
        self.clearLetters(self.letters.get())

root = Tk()
aplication = Interface(root)
root.bind("<Key>", aplication.key_pressed)
root.mainloop()
# Created by: Chris Asante
# Created on: 10-March-2019
# Created for: ICS3U
# Assignment 7
# acceleration from gravity

from tkinter import *

root = Tk()

def calculation():
    userinput = TextBox.get()
    time = int(userinput) 
    height = 100 - 0.5 * 9.81* time**2
    Answer = str("%.2f" % height) 
    AnswerLabel = Label(root, text="Height is:" + " "+ Answer + " "+ "m")
    AnswerLabel.pack()
    

Label1 = Label(root, text="Enter the number of seconds since the object was dropped:")
Label1.pack()

TextBox = Entry(root)
TextBox.pack()
Button1 = Button(root, text= "Calculate", command=calculation)
Button1.pack()

root.mainloop()
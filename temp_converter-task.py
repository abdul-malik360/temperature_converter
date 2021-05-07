import tkinter as tk
from tkinter import *

root= Tk()
root.geometry("900x600")
root.title("Temperature Convertor")

fahrenheit = StringVar()
celcius = StringVar()

fahrenheit = Label(root, text="Celcius To Fahrenheit: ").place(x=120, y=100)
celcius = Label(root, text="Fahrenheit To Celcius").place(x=420, y=100)


entryF = Entry(root, textvariable=fahrenheit).place(x=120 , y=200)
entryC = Entry(root, textvariable=celcius).place(x=420 , y=200)

fbtn = Button(root, text="Activate - Fahrenheit", ).place(x=120, y=300)
cbtn = Button(root, text="Activate - Celcius", ).place(x=420, y=300 )
calconbtn = Button(root, text="Calculate Conversion", ).place(x=120, y=400 )
clearbtn = Button(root, text="Clear", ).place(x=500, y=400 )
extbtn = Button(root, text="Exit Program", ).place(x=450, y=500 )

root.mainloop()

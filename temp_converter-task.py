# Calling tkinter function.
from tkinter import*
# Basiclly the format you use when using tkinter.
root =Tk()
# Name of window
root. title("TEMPERATURE CONVERTOR")
# size of window
root.geometry("900x600")
#set background of window color
root.configure(bg='dark green')

#
fahrenheit = Frame(root)
fahrenheit.pack()

# Giving
celcius = Frame(root)
celcius.pack()

# Naming variables
num_1 = IntVar
num_2 = IntVar

# Title first frame.
fahrenheit=LabelFrame(root, text="Celcuis",padx="40", pady="40", background="light green")
fahrenheit.pack(fill="both")
# Placing the frame
fahrenheit.place(x =100, y = 50)
Cel_entry=Entry(fahrenheit, state="disable")
Cel_entry.pack()

# Title of the second frame.
celcius=LabelFrame(root, text="Faranheit",padx="40", pady="40", background="light green")
celcius.pack(fill="both")
# Placing the frame
celcius.place(x = 550, y = 50)
Far_entry=Entry(celcius, state="disable")
Far_entry.pack()

# defining functions
def active_cel():
    Cel_entry.configure(state="normal",)

cel_convert_btn=Button(root,text="Activate Celcuis", command=active_cel, background="light green")
cel_convert_btn.pack()
# Placing the celcius convert button
cel_convert_btn.place(x = 100, y = 180)
def convert():
    if Cel_entry:
        num1= float(Cel_entry.get())
        num2= (num1*9/5)+32
        answer.insert(0, float(num2))

def convert1():
    if Far_entry:
        num2= float(Far_entry.get())
        num1= (num2 -32)*5/9
        answer.insert(0, float(num1))

def active_cel():
    Far_entry.configure(state="normal")

f_convert_btn=Button(root,text="Activate Fahrenheit", command=active_cel, background="light green")
f_convert_btn.pack()
# Placing the fahrenheit convert button
f_convert_btn.place(x = 550, y = 180)

# To convert in frame 1
con_btn=Button(root,text="Convert to Fahrenheit ", command=convert, background="light green")
con_btn.pack(side=LEFT)
# Placing the convert button
con_btn.place(x = 100, y = 250)

# to convert in frame 2
con_btn1=Button(root,text="Convert to Calcius", command=convert1, background="light green")
con_btn1.pack(side=LEFT)
con_btn1.place(x = 550, y = 250)

# showing result
answer=Entry(root,text="", background="light grey")
answer.pack()
answer.place(x = 350, y = 300)

# clearing all entries
def clear_all_num():
    Cel_entry.delete(0,END)
    Far_entry.delete(0,END)
    answer.delete(0,END)
# Clear button.
clear_btn=Button(text="Clear", command=clear_all_num, background="light blue")
clear_btn.pack(side=RIGHT)
clear_btn.place(x = 550, y = 400)

# Defining function for exit button
def exit_program():
    root.destroy()

# Exit button
exit_btn=Button(text="Exit" ,command=exit_program, background="red")
exit_btn.pack(side=RIGHT)
exit_btn.place(x = 650, y = 400)


# Only way for program to run
root.mainloop()

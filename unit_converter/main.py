from tkinter import *

def button_clicked():
    my_label.config(text=input.get())

window = Tk()
window.title("My first Program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

# Label.
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="Budbak")
my_label.grid(column=1,row=1)
my_label.config(padx=20,pady=20)

#Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=2,row=2)

#NewButton
newbutton = Button(text="New button", command=button_clicked)
newbutton.grid(column=3,row=1)

#Input
input = Entry(width=10)
input.grid(column=4,row=3)

window.mainloop()

from tkinter import *

def calculate():
    bb.config(text=str(round(float(ab.get())*1.609,3)))


window = Tk()
window.title("Mile To Km Converter")
window.minsize()
window.config(pady=50, padx=50)

#iseqialto
ba = Label(text="is equal to")
ba.grid(row=2, column=1)

#input
ab = Entry()
ab.grid(row=1, column=2)

#miles
ac = Label(text="Miles")
ac.grid(row=1, column=3)

#Kms
bc = Label(text="Kms")
bc.grid(row=2, column=3)

#Answer
bb = Label(text="0")
bb.grid(row=2, column=2)

#button
cb = Button(text="Calculate", command=calculate)
cb.grid(row=3, column=2)


window.mainloop()
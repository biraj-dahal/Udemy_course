from tkinter import *

FONT=("Comic Sans MS", 10, "normal")

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(height=200, width=200)
picture = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=picture)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:", font=FONT)
web_label.grid(row=1, column=0, pady=5)

web_in = Entry(width=35)
web_in.grid(row=1, column=1,pady=5, columnspan=2,sticky=W)

email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(row=2, column=0,pady=5)

email_in = Entry(width=35)
email_in.grid(row=2, column=1, pady=5, columnspan=2,sticky=W)

pass_label = Label(text="Password:", font=FONT)
pass_label.grid(row=3, column=0,pady=5)

pass_in = Entry(width=21)
pass_in.grid(row=3, column=1,pady=5, sticky=W)

gen_button =Button(text="Generate Password", font=FONT)
gen_button.grid(row=3, column=2,pady=5)

add_button =Button(text="Add", width=42, font=FONT)
add_button.grid(row=4, column=1, pady=5, sticky=W, columnspan=2)

window.mainloop()
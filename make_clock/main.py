from tkinter import *
import subprocess


timer = None
def reset_timer():
    window.after_cancel(timer)
    hours.config(text=f"00:")
    mins.config(text=f"00:")
    secs.config(text=f"00")
    prompt.grid(row=4, column=2, padx=60)
    input.grid(row=5, column=2, padx=20, pady=20)
    start.grid(row=6, column=2)
    reset_btn.grid_forget()

def count_down(total_sec):
    HH = total_sec // 3600
    MM = (total_sec % 3600) // 60
    SS = total_sec % 60
    if HH > 9: hours.config(text=f"{HH}:")
    else: hours.config(text=f"0{HH}:")
    if MM > 9: mins.config(text=f"{MM}:")
    else: mins.config(text=f"0{MM}:")
    if SS > 9: secs.config(text=f"{SS}")
    else: secs.config(text=f"0{SS}")
    if total_sec > 0:
        global timer
        timer = window.after(1000, count_down, total_sec - 1)
    else:
        reset_btn.grid_forget()
        prompt.grid(row=4, column=2, padx=60)
        input.grid(row=5, column=2, padx=20, pady=20)
        start.grid(row=6, column=2)
        subprocess.run(['afplay', '/Users/birajdahal/Desktop/udemy/projects/make_clock/i_am_vin_diesel.mp3'])


def start_countdown():
    global total_sec
    HH, MM, SS = input.get().split(':')
    HH, MM, SS = int(HH), int(MM), int(SS)
    total_sec = HH * 3600 + MM * 60 + SS

    prompt.grid_forget()
    input.grid_forget()
    start.grid_forget()
    reset_btn.grid(row=7, column=2)
    count_down(total_sec)


window = Tk()
window.title("Timer")
window.config(bg="black")
window.iconbitmap("/Users/birajdahal/Desktop/udemy/projects/make_clock/timer_icon.icns")
window.state('zoomed')


# empty
empty1 = Label(text="", font=("Arial", 150, "bold"), fg="white")
empty1.config(bg="black")
empty1.grid(row=1, column=1, padx=60, pady=20)

# hours
hours = Label(text="00:", font=("Arial", 300, "bold"), fg="white")
hours.config(bg="black")
hours.grid(row=2, column=1, padx=60, pady=20, sticky="w")

# mins
mins = Label(text="00:", font=("Arial", 300, "bold"), fg="white")
mins.config(bg="black")
mins.grid(row=2, column=2, padx=20, pady=20, sticky="w")

# secs
secs = Label(text="00", font=("Arial", 300, "bold"), fg="white")
secs.config(bg="black")
secs.grid(row=2, column=3, padx=60, pady=20, sticky="w")

# empty
empty2 = Label(text="", font=("Arial", 50, "bold"), fg="white")
empty2.config(bg="black")
empty2.grid(row=3, column=2, padx=60, pady=20)

# prompt
prompt = Label(text="HH:MM:SS format", font=("Arial",20), bg="white", fg="white")
prompt.config(bg="black")
prompt.grid(row=4, column=2, padx=60)

#sixty_min
input = Entry(window, text="", font=("Arial",20), bg="white", fg="white")
input.config(fg="black")
input.config(borderwidth=0, highlightthickness=0, width=7)
input.grid(row=5, column=2, padx=20, pady=20)

#start
start = Button(text="START", borderwidth=0, command=start_countdown)
start.grid(row=6, column=2)

#start
reset_btn = Button(text="Reset", borderwidth=0, command=reset_timer)


window.mainloop()


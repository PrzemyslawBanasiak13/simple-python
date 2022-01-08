
from tkinter import *
import math

# constants ----------------------------
# ✔

PINK = "#e2979c"
RED = "#D32626"
GREEN = "#79D70F"
GREY = "#BBBBBB"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BEAK_MIN = 5
LONG_BREAK_MIN = 30
MIN_MULTIPIER = 60
reps = 0
app_clock = None

# timer reset ---------------------------


def reset_timer():
    global reps
    reps = 0
    sign.config(text="Ready?", fg="green")
    checkmarks.config(text="")
    window.after_cancel(app_clock)
    canvas.itemconfig(timer_text, text=f"0:00")


# timer mechanism -----------------------


def start_timer():
    global reps
    if reps == 0 or reps == 2 or reps == 4 or reps == 6:
        sign.config(text="WORK", fg="green")
        count_down(WORK_MIN * MIN_MULTIPIER)
    if reps == 1 or reps == 3 or reps == 5:
        sign.config(text="REST", fg="red")
        count_down(SHORT_BEAK_MIN * MIN_MULTIPIER)
    if reps == 7:
        sign.config(text="REST", fg="red")
        count_down(LONG_BREAK_MIN * MIN_MULTIPIER)
    checkmarks.config(text=math.ceil(reps/2) * "✔")
    reps += 1


# countdown mechanism -------------------


def count_down(total_seconds):
    minutes = math.floor(total_seconds / 60)
    seconds = total_seconds % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if total_seconds > 0:
        global app_clock
        app_clock = window.after(1000, count_down, total_seconds - 1)
    if total_seconds == 0:
        start_timer()


# UI setup ------------------------------

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREY)

canvas = Canvas(width=300, height=300, bg=GREY, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=tomato_png)
timer_text = canvas.create_text(150, 150, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="START", command=start_timer, font=(FONT_NAME, 13, "bold"))
start_button.grid(column=0, row=2)

reset_button = Button(text="RESET", command=reset_timer, font=(FONT_NAME, 13, "bold"))
reset_button.grid(column=2, row=2)

sign = Label(text="Hello!", font=(FONT_NAME, 50, "bold"), fg="green", bg=GREY)
sign.grid(column=1, row=0)

checkmarks = Label(text="", font=(FONT_NAME, 20, "bold"), fg="green", bg=GREY)
checkmarks.grid(column=1, row=3)

window.mainloop()

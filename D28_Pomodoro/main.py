import time
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
mark = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    window.after_cancel(timer)
    canvas.itemconfig(item_count, text="00:00")
    title_label.config(text='Timer', fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
    checkmarks.config(text="", fg=GREEN, font=(FONT_NAME, 15, "bold"))
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text='Break', fg=RED,
                           font=(FONT_NAME, 50), bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text='Break', fg=PINK,
                           font=(FONT_NAME, 50), bg=YELLOW)
    else:
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = '0' + str(count_sec)

    canvas.itemconfig(item_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global mark
        if reps % 2 == 0 and reps % 8 != 0:
            mark += "✔"
            checkmarks.config(text=f"{mark}", fg=GREEN,
                              font=(FONT_NAME, 15, "bold"))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
item_count = canvas.create_text(100, 130, text="00:00", fill="#FFF",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, rows=1)


button_start = Button(text="Start", width="7",
                      command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=2)


button_reset = Button(text="Reset", width="7",
                      highlightthickness=0, command=reset)
button_reset.grid(column=2, row=2)

checkmarks = Label(text="", fg=GREEN, font=(FONT_NAME, 15, "bold"))
checkmarks.config(bg=YELLOW)
checkmarks.grid(column=1, row=3)


window.mainloop()

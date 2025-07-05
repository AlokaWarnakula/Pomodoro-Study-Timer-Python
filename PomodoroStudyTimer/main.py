import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#0fae55"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REAPS = 0
TIMER = None

# Colors from the graduation hat image
COLOR_GRAY_PURPLE = "#636176"
COLOR_TEAL = "#2fd5c8"
COLOR_GOLD = "#e8bf54"

# Text colors for best contrast
TEXT_COLOR_LIGHT = "#FFFFFF"  # White
TEXT_COLOR_DARK = "#000000"  # Black


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global TIMER, REAPS
    # Cancel the ongoing timer if any
    if TIMER:
        window.after_cancel(TIMER)
        TIMER = None
    # Reset label text
    timer_label.config(text="Timer")
    # Reset check marks
    check_mark.config(text="")
    # Reset timer display
    canvas.itemconfig(timer_text, text="00:00")
    # Reset reaps count
    REAPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global REAPS
    REAPS +=1
    work_sec = WORK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    if REAPS % 8 == 0:
        count_down(long_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif REAPS % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work now", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global TIMER
    min = math.floor(count / 60)
    sec = math.floor(count % 60)
    time_format = f"{min:02d}:{sec:02d}"

    canvas.itemconfig(timer_text, text=time_format)
    print(count)
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_count()
        check_mark_emojo = ""
        work_sesions = math.floor(REAPS/2)
        for i in range(work_sesions):
            check_mark_emojo += "✖"
        check_mark.config(text=check_mark_emojo)


# ---------------------------- UI SETUP ------------------------------- #
# tk object make
window = Tk()
window.title("Pomodoro Timer")
# window.config(padx=10,pady=10,bg=YELLOW)


# canvas = Canvas(width=866,height=650,bg=YELLOW,highlightthickness=0)
canvas = Canvas(width=866, height=650)
bgPicture = PhotoImage(file="graduationHat.png")
canvas.create_image(433, 325, image=bgPicture)
timer_text = canvas.create_text(433, 325, text="00:00", fill="white", font=(FONT_NAME, 70, "bold"))
canvas.grid(column=1, row=1)

# Create the label
timer_label = Label(text="Timer", fg=COLOR_GRAY_PURPLE, font=(FONT_NAME, 60, "bold"), bg=TEXT_COLOR_LIGHT)
canvas.create_window(433, 70, window=timer_label)

# Star and reset buttons
start_button = Button(text="Start", highlightthickness=0, font=(FONT_NAME, 25, "bold"), fg=GREEN, command=start_count)
reset_button = Button(text="Rest", highlightthickness=0, font=(FONT_NAME, 25, "bold"), fg=RED,command=reset_timer)
canvas.create_window(200, 530, window=start_button)
canvas.create_window(650, 530, window=reset_button)

# Check mark
check_mark = Label(fg=COLOR_GOLD, font=(FONT_NAME, 50, "bold"), bg=TEXT_COLOR_LIGHT)
canvas.create_window(450, 530, window=check_mark)

# keep the window
window.mainloop()

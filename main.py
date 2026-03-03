from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = ("Courier", 35, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetition = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    text_mood.config(text="Timer", fg=GREEN)
    check_mark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global repetition
    repetition = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def starting_timer():
    global repetition
    repetition += 1

    focusing_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    if repetition % 8 == 0:
        count_down(long_break_time)
        text_mood.config(text="Break", fg=RED)
    elif repetition % 2 == 0:
        count_down(short_break_time)
        text_mood.config(text= "Break", fg=PINK)
    else:
        count_down(focusing_time)
        text_mood.config(text= "Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_m = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_m}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        starting_timer()
        check_marks = ""
        work_session = math.floor(repetition / 2)
        for n in range(work_session):
            check_marks += "✔"
        check_mark_label.config(text=check_marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Deep Focus Working")
window.configure(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_photo)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=FONT_NAME)
canvas.grid(row=2, column=2)

text_mood = Label(text="Timer", font=("Courier", 30, "bold"), fg=GREEN)
text_mood.grid(row=1, column=2)

start_button = Button(text="Start", command=starting_timer)
start_button.grid(row=3, column=1)

Reset_button = Button(text="Reset", command=reset)
Reset_button.grid(row=3, column=3)

check_mark_label = Label(text="", highlightthickness=0, font=("Courier", 25, "bold"), fg=GREEN)
check_mark_label.grid(row=4, column=2)

window.mainloop()

from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = ("Courier", 35, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Deep Focus Working")
window.configure(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_photo)
canvas.create_text(100, 140, text="00:00", fill="white", font=FONT_NAME)
canvas.grid(row=2, column=2)

text_Timer = Label(text="Timer", font=("Courier", 30, "bold"), fg=GREEN)
text_Timer.grid(row=1, column=2)

start_button = Button(text="Start")
start_button.grid(row=3, column=1)

Reset_button = Button(text="Reset")
Reset_button.grid(row=3, column=3)

check_box_label = Label(text="✔", font=("Courier", 25, "bold"), fg=GREEN)
check_box_label.grid(row=4, column=2)

window.mainloop()
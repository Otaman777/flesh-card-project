import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# ------------------------------ DATA PROCESSING ------------------------------ #
try:
    data = pandas.read_csv("./data/words_to_learn.csv.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")

current_card = {}


def yes_clicked():
    global current_card
    data_dict.remove(current_card)
    new_data = pandas.DataFrame(data=data_dict)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    show_next_word()


def no_clicked():
    show_next_word()


def show_next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(word_label, text=current_card[data.columns[0]])
    canvas.itemconfig(lang_label, text=data.columns[0], fill="black")
    canvas.itemconfig(word_label, fill="black")
    canvas.itemconfig(card_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(lang_label, text=data.columns[1], fill="white")
    canvas.itemconfig(word_label, text=current_card[data.columns[1]], fill="white")


# ------------------------------ UI settings ------------------------------ #

window = tkinter.Tk()
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_front_img = tkinter.PhotoImage(file="./images/card_front.png")
card_back_img = tkinter.PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
lang_label = canvas.create_text(400, 150, text="Title", fill="black", font=(FONT_NAME, 40, "italic"))
word_label = canvas.create_text(400, 263, text="word", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.itemconfig(lang_label, text=data.columns[0])

img_btn_no = tkinter.PhotoImage(file="./images/wrong.png")
img_btn_yes = tkinter.PhotoImage(file="./images/right.png")

btn_no = tkinter.Button(image=img_btn_no, highlightthickness=0, command=no_clicked)
btn_yes = tkinter.Button(image=img_btn_yes, highlightthickness=0, command=yes_clicked)
btn_no.grid(row=1, column=0)
btn_yes.grid(row=1, column=1)

flip_timer = window.after(3000, func=flip_card)
show_next_word()

window.mainloop()

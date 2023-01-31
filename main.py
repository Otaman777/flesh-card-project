import tkinter

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# -------------------- UI settings -------------------- #

window = tkinter.Tk()
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_front_img = tkinter.PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
lang_label = canvas.create_text(400, 150, text="Title", fill="black", font=(FONT_NAME, 40, "italic"))
word_label = canvas.create_text(400, 263, text="word", fill="black", font=(FONT_NAME, 60, "bold"))

img_btn_no = tkinter.PhotoImage(file="./images/wrong.png")
img_btn_yes = tkinter.PhotoImage(file="./images/right.png")

btn_no = tkinter.Button(image=img_btn_no, highlightthickness=0)
btn_yes = tkinter.Button(image=img_btn_yes, highlightthickness=0)
btn_no.grid(row=1, column=0)
btn_yes.grid(row=1, column=1)


window.mainloop()

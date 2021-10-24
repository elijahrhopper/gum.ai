
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.title('gumAI')

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    774.0,
    116.0,
    anchor="nw",
    text="AI",
    fill="#8793FF",
    font=("Roboto Bold", 72 * -1)
)

canvas.create_text(
    587.0,
    94.0,
    anchor="nw",
    text="gum",
    fill="#FF8787",
    font=("Roboto Medium", 96 * -1)
)

canvas.create_text(
    143.0,
    416.0,
    anchor="nw",
    text="Age:",
    fill="#000000",
    font=("Roboto Bold", 36 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    317.5,
    515.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Roboto Bold", 36 * -1)
)
entry_1.place(
    x=163.0,
    y=475.0,
    width=309.0,
    height=78.0
)

canvas.create_text(
    556.0,
    416.0,
    anchor="nw",
    text="Phone Number:",
    fill="#000000",
    font=("Roboto Bold", 36 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    926.5,
    515.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Roboto Bold", 36 * -1)
)
entry_2.place(
    x=576.0,
    y=475.0,
    width=701.0,
    height=78.0
)

canvas.create_text(
    143.0,
    233.0,
    anchor="nw",
    text="Name:",
    fill="#000000",
    font=("Roboto Bold", 36 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    544.0,
    332.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Roboto Bold", 36 * -1)
)
entry_3.place(
    x=163.0,
    y=292.0,
    width=762.0,
    height=78.0
)

canvas.create_text(
    1009.0,
    233.0,
    anchor="nw",
    text="Gender:",
    fill="#000000",
    font=("Roboto Bold", 36 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    1153.0,
    332.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Roboto Bold", 36 * -1)
)
entry_4.place(
    x=1029.0,
    y=292.0,
    width=248.0,
    height=78.0
)

canvas.create_text(
    143.0,
    599.0,
    anchor="nw",
    text="Date of Birth:",
    fill="#000000",
    font=("Roboto Bold", 36 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    544.0,
    698.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Roboto Bold", 36 * -1)
)
entry_5.place(
    x=163.0,
    y=658.0,
    width=762.0,
    height=78.0
)

canvas.create_text(
    1009.0,
    599.0,
    anchor="nw",
    text="Zip Code:",
    fill="#000000",
    font=("Roboto Bold", 36 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    1153.0,
    698.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Roboto Bold", 36 * -1)
)
entry_6.place(
    x=1029.0,
    y=658.0,
    width=248.0,
    height=78.0
)

canvas.create_text(
    143.0,
    782.0,
    anchor="nw",
    text="Image Path:",
    fill="#000000",
    font=("Roboto Bold", 36 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    576.0,
    881.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Roboto Bold", 36 * -1)
)
entry_7.place(
    x=163.0,
    y=841.0,
    width=826.0,
    height=78.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: os.system('python /Users/rohitvemuri/Downloads/Tkinter-Designer/gui_positive/gui.py'),
    relief="flat"
)
button_1.place(
    x=1184.0,
    y=841.0,
    width=113.0,
    height=80.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: os.system('python /Users/rohitvemuri/Downloads/Tkinter-Designer/gui_negative/gui.py'),
    relief="flat"
)
button_2.place(
    x=1077.0,
    y=841.0,
    width=120.0,
    height=80.0
)
window.resizable(False, False)
window.mainloop()


# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import os

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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    533.0,
    584.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1023.0,
    y=681.0,
    width=269.0,
    height=80.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: os.system('python /Users/rohitvemuri/Downloads/Tkinter-Designer/build/gui.py'),
    relief="flat"
)
button_2.place(
    x=1023.0,
    y=765.0,
    width=269.0,
    height=80.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1144.0,
    465.0,
    image=image_image_2
)

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
window.resizable(False, False)
window.mainloop()

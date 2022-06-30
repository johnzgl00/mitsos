from tkinter import colorchooser
def choose_color():
    color_code = colorchooser.askcolor(title="Choose Color")
    print(color_code)
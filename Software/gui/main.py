from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from colorPicker import choose_color
from controlBoard import *

root = Tk()
root.geometry("600x500")
root.configure(bg="grey30")

title = ttk.Label(root, text="Robot Control Panel", font=("Arial", 21, BOLD), foreground="grey70", background="grey30")
title.place(relx=0.26, rely=0)

title2 = ttk.Label(root, text="Control", font=("Arial", 17, BOLD), foreground="grey70", background="grey30")
title2.place(relx=0.7, rely=0.07)

pitchLabel = Label(root, text="Pitch:", bg="grey30", fg="grey70", font=("Arial", 15))
pitchLabel.place(relx=0.62, rely=0.13)
pitchInput = Text(root, height=1, width=13, bg="grey70", font=("Arial", 15))
pitchInput.place(relx=0.72, rely=0.131)

yawLabel = Label(root, text="Yaw:", bg="grey30", fg="grey70", font=("Arial", 15))
yawLabel.place(relx=0.62, rely=0.2)
yawInput = Text(root, height=1, width=13, bg="grey70", font=("Arial", 15))
yawInput.place(relx=0.72, rely=0.2)

LedLabel = Label(root, text="Led:", bg="grey30", fg="grey70", font=("Arial", 15))
LedLabel.place(relx=0.635, rely=0.274)
OnLedButton = Button(root, text="On", bg="green", fg="black", font=("Arial", 13), command=ledOn)
OnLedButton.place(relx=0.72, rely=0.27)
OffLedButton = Button(root, text="Off", bg="red3", fg="black", font=("Arial", 13), command=ledOff)
OffLedButton.place(relx=0.79, rely=0.27)

ColorLabel = Label(root, text="Color:", bg="grey30", fg="grey70", font=("Arial", 15))
ColorLabel.place(relx=0.615, rely=0.345)
ColorPicker = Button(root, text="Choose Color", bg="gold2", command=choose_color)
ColorPicker.place(relx=0.72, rely=0.345)

ModeLabel = Label(root, text="Mode:", bg="grey30", fg="grey70", font=("Arial", 15))
ModeLabel.place(relx=0.61, rely=0.415)
AutoModeButton = Button(root, text="Auto", bg="green", fg="black", font=("Arial", 13), command=modeA)
AutoModeButton.place(relx=0.72, rely=0.41)
ManualModeButton = Button(root, text="Manual", bg="red3", fg="black", font=("Arial", 13), command=modeM)
ManualModeButton.place(relx=0.81, rely=0.41)

SpeedLabel = Label(root, text="Speed:", bg="grey30", fg="grey70", font=("Arial", 15))
SpeedLabel.place(relx=0.6, rely=0.485)
SpeedInput = Text(root, height=1, width=13, bg="grey70", font=("Arial", 15))
SpeedInput.place(relx=0.72, rely=0.485)

DelayLabel = Label(root, text="Delay:", bg="grey30", fg="grey70", font=("Arial", 15))
DelayLabel.place(relx=0.61, rely=0.551)
DelayInput = Text(root, height=1, width=13, bg="grey70", font=("Arial", 15))
DelayInput.place(relx=0.72, rely=0.555)

DelayInput = Button(root, height=1, width=13, text="Refresh", bg="grey70", font=("Arial", 15), command=refresh)
DelayInput.place(relx=0.665, rely=0.63)

root.mainloop()
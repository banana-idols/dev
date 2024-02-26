import tkinter as tk
import ttkbootstrap as ttk

# window
window = ttk.Window(themename="darkly")
window.title ("Banana-Idols")
window.geometry('800x500')

# widgets
title_label = ttk.Label(
    master = window, 
    text = "Miles to Kilometars", 
    font="Calibri 24 bold")
title_label.pack()

input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
entry.pack(side = "left")
button = ttk.Button(master = input_frame, text = "Convert")
button.pack(side = "left")
input_frame.pack()

# run
window.mainloop()
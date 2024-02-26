import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title ("Banana-Idols")
window.geometry('800x500')

# widgets
title_label = ttk.Label(master = window, 
                        text = "Miles to Kilometars", 
                        font="Calibri 24 bold")
title_label.pack()

input_frame = ttk.Frame(master = window)
input_frame.pack()
entry = ttk.Entry(master = input_frame)
entry.pack(side = "left")
button = ttk.Button(master = input_frame, text = "Convert")
button.pack(side = "left")

# run
window.mainloop()
import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Widgets')
window.geometry('800x400')

# widgets
text = tk.Text(master=window)
text.pack()

# ttk widgets
label = ttk.Label(master=window, text = "This is a Text")
label.pack()

# run
window.mainloop()

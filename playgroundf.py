import tkinter as tk
from tkinter import font

root = tk.Tk()

# Create a font object with the desired size
my_font = font.Font(family="Helvetica", size=20)


# Create a label with the specified font
label = tk.Label(root, text="Hello, World!", font=my_font)
label.pack(pady=20)

root.mainloop()

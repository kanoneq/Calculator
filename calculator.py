import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Calculator (by kanoneq :D)")
root.geometry("600x750")

label = tk.Label(root, text = "Welcome to my calculator!", font=('Arial', 18))
label.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)



root.mainloop()
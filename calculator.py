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

btn1 = tk.Button(buttonframe, text="1", font=("Arial", 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=("Arial", 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=("Arial", 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=("Arial", 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=("Arial", 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=("Arial", 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btn7 = tk.Button(buttonframe, text="7", font=("Arial", 18))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)

btn8 = tk.Button(buttonframe, text="8", font=("Arial", 18))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)

btn9 = tk.Button(buttonframe, text="9", font=("Arial", 18))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)

btn0 = tk.Button(buttonframe, text="0", font=("Arial", 18))
btn0.grid(row=3, column=1, sticky=tk.W+tk.E)

btn_eq = tk.Button(buttonframe, text="=", font=("Arial", 18))
btn_eq.grid(row=3, column=0, sticky=tk.W+tk.E)

btn_add = tk.Button(buttonframe, text="+", font=("Arial", 18))
btn_add.grid(row=0, column=3, sticky=tk.W+tk.E)

btn_sub = tk.Button(buttonframe, text="-", font=("Arial", 18))
btn_sub.grid(row=1, column=3, sticky=tk.W+tk.E)

btn_mul = tk.Button(buttonframe, text="*", font=("Arial", 18))
btn_mul.grid(row=2, column=3, sticky=tk.W+tk.E)

btn_div = tk.Button(buttonframe, text="/", font=("Arial", 18))
btn_div.grid(row=3, column=3, sticky=tk.W+tk.E)

btn_dot = tk.Button(buttonframe, text=".", font=("Arial", 18))
btn_dot.grid(row=3, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

root.mainloop()
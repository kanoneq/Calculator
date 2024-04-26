import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Calculator (by kanoneq :D)")
root.geometry("500x400")

#Cframe (thingy for backspace and "C" button)
Cframe = tk.Frame(root)
Cframe.columnconfigure(0, weight=1)
Cframe.columnconfigure(1, weight=1)

def clear():
    empty: str = ""
    Label.configure(text=empty)
btnC = tk.Button(Cframe, text="C", font=('Arial', 20), command=clear)
btnC.grid(row=0, column=0, sticky=tk.W)

def back():
    new = Label["text"]
    new = new[:len(new)-1]
    Label.configure(text=new)
btnback = tk.Button(Cframe, text="backspace", font=('Arial', 20), command=back)
btnback.grid(row=0, column=1, sticky=tk.E)

Cframe.pack(fill="x")
#end of Cframe

#label which shows what user is typing into calculator
Label = tk.Label(root, text="", font=('Arial', 20))
Label.pack(padx=5, pady=20)
#end of the label, and start of the adding function
def adding(string: str):
    current = Label["text"]
    new = current + string
    Label.configure(text=new)
#end of the function

#buttonframe is basically every button on the bottom of the calculator
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

def one():
    adding("1")
btn1 = tk.Button(buttonframe, text="1", font=("Arial", 18), command=one)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
def two():
    adding("2")
btn2 = tk.Button(buttonframe, text="2", font=("Arial", 18), command=two)
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
def three():
    adding("3")
btn3 = tk.Button(buttonframe, text="3", font=("Arial", 18), command=three)
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
def four():
    adding("4")
btn4 = tk.Button(buttonframe, text="4", font=("Arial", 18), command=four)
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
def five():
    adding("5")
btn5 = tk.Button(buttonframe, text="5", font=("Arial", 18), command=five)
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
def six():
    adding("6")
btn6 = tk.Button(buttonframe, text="6", font=("Arial", 18), command=six)
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)
def seven():
    adding("7")
btn7 = tk.Button(buttonframe, text="7", font=("Arial", 18), command=seven)
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)
def eight():
    adding("8")
btn8 = tk.Button(buttonframe, text="8", font=("Arial", 18), command=eight)
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)
def nine():
    adding("9")
btn9 = tk.Button(buttonframe, text="9", font=("Arial", 18), command=nine)
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)
def zero():
    adding("0")
btn0 = tk.Button(buttonframe, text="0", font=("Arial", 18), command=zero)
btn0.grid(row=3, column=1, sticky=tk.W+tk.E)
def add2():
    adding("+")
btn_add = tk.Button(buttonframe, text="+", font=("Arial", 18), command=add2)
btn_add.grid(row=0, column=3, sticky=tk.W+tk.E)
def sub2():
    adding("-")
btn_sub = tk.Button(buttonframe, text="-", font=("Arial", 18), command=sub2)
btn_sub.grid(row=1, column=3, sticky=tk.W+tk.E)
def mul2():
    adding("*")
btn_mul = tk.Button(buttonframe, text="*", font=("Arial", 18), command=mul2)
btn_mul.grid(row=2, column=3, sticky=tk.W+tk.E)
def div2():
    adding("/")
btn_div = tk.Button(buttonframe, text="/", font=("Arial", 18), command=div2)
btn_div.grid(row=3, column=3, sticky=tk.W+tk.E)
def dot():
    adding(".")
btn_dot = tk.Button(buttonframe, text=".", font=("Arial", 18), command=dot)
btn_dot.grid(row=3, column=0, sticky=tk.W+tk.E)

def eq():
    current = Label["text"]
    
    result: str = ""
    try:
        result = eval(current)
    except Exception as e:
        result = "ERROR! Check console."
        print(f"error: {e}")

    Label.configure(text=str(result))
btn_eq = tk.Button(buttonframe, text="=", font=("Arial", 18), command=eq)
btn_eq.grid(row=3, column=2, sticky=tk.W+tk.E)


buttonframe.pack(fill='x', side=tk.BOTTOM)
#end of the buttonframe

root.mainloop()

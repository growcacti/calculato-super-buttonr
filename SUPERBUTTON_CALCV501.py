import tkinter as tk
from tkinter import ttk, Canvas, Frame, filedialog, font
from tkinter import *
import math
from math import *


root = tk.Tk()

root.title("Math App Ver2")

notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0)
f0 = ttk.Frame(notebook)
notebook.add(f0, text="SuperBtNCalc")
root.geometry("1200x900")

answer_ee2 = 0
cc_complete = 0

frm1 = ttk.Frame(f0, height=20, width=200)
frm1.grid(row=0, column=1, columnspan=2)


frm1.columnconfigure(0, weight=4)
frm1.columnconfigure(1, weight=5)
frm2 = tk.Canvas(f0, height=100, width=1100, background="Ivory3")
frm2.grid(row=5, column=0, columnspan=4)


frm3 = tk.Canvas(f0, height=100, width=200, background="azure")
frm3.grid(row=0, column=6)
##
lb = tk.Listbox(frm3)
lb.grid(row=25, column=1)

tk.Label(frm3, text="As Memory").grid(row=24, column=1)
e1 = tk.Entry(frm1, bd=7, bg="wheat")
e1.grid(row=0, column=0, padx=20, sticky="w")
e2 = tk.Entry(frm1, bd=7, bg="light blue")
e2.grid(row=0, column=1, padx=20, sticky="w")
e3 = tk.Entry(frm1, bd=7, bg="light green")
e3.grid(row=0, column=2, padx=20, sticky="w")
e4 = tk.Entry(frm1, bd=7, bg="light pink")
e4.grid(row=0, column=3, padx=20, sticky="w")

## future upgrade if need entry widgets are needed
##e7 = tk.Entry(frm3, bd=7, bg="wheat")
##e7.grid(row=5, column=6, padx=20, sticky="w")
##e8 = tk.Entry(frm3, bd=7, bg="light blue")
##e8.grid(row=6, column=6, padx=20, sticky="w")
##e9 = tk.Entry(frm3, bd=7, bg="light green")
##e9.grid(row=7, column=6, padx=20, sticky="w")
##e10 = tk.Entry(frm3, bd=7, bg="light pink")
##e10.grid(row=8, column=6, padx=20, sticky="w")
e6 = Entry(frm1, bd=7, bg="wheat")
e6.grid(row=1, column=1)
tk.Label(frm1, text="                ").grid(row=2, column=0)
tk.Label(frm1, text="                ").grid(row=3, column=1)
tk.Label(frm1, text="                ").grid(row=2, column=2)
tk.Label(frm1, text="                ").grid(row=3, column=2)
tk.Label(frm1, text="                ").grid(row=2, column=3)
tk.Label(frm1, text="                ").grid(row=3, column=3)


def add(n=1):
    if n == 1:

        if not len(e4.get()) == 0:
            lb.insert(1, e4.get())
            e4.delete(0, END)
        if not len(e3.get()) == 0:
            e4.insert(END, e3.get())
            e3.delete(0, END)
        if not len(e2.get()) == 0:
            e3.insert(END, e2.get())
            e2.delete(0, END)

        ee1 = float(e1.get())
        e2.insert(END, ee1)
        ee2 = e2.get()
        e1.delete(0, END)
    elif n == 2:

        ee4 = float(e4.get())
        ee3 = float(e3.get())
        ans = ee4 + ee3
        e3.delete(0, END)
        e3.insert(END, ans)

    def eq():
        if not len(e6.get()) == 0:
            lb.insert(1, e6.get())
            e6.delete(0, END)
        ee1 = float(e1.get())
        ee2 = float(e2.get())
        answer = float(ee1) + float(ee2)
        tk.Label(frm1, text="----Answer----").grid(row=3, column=1)
        return e6.insert(END, answer)

    eqbtn1 = tk.Button(
        frm1,
        text="  =  ",
        bd=7,
        bg="AntiqueWhite2",
        font=("URW Chancery L", 12, "bold"),
        command=eq,
    )
    eqbtn1.grid(row=1, column=0)


def subtract(n=1):
    if n == 1:
        if not len(e4.get()) == 0:
            lb.insert(1, e4.get())
            e4.delete(0, END)
        if not len(e3.get()) == 0:
            e4.insert(END, e3.get())
            e3.delete(0, END)
        if not len(e2.get()) == 0:
            e3.insert(END, e2.get())
            e2.delete(0, END)

        ee1 = e1.get()
        e2.insert(END, ee1)
        ee2 = e2.get()
        e1.delete(0, END)
    elif n == 2:

        ee4 = float(e4.get())
        ee3 = float(e3.get())
        ans = ee4 - ee3
        e3.delete(0, END)
        return e3.insert(END, ans)

    def eq():
        if not len(e6.get()) == 0:
            lb.insert(1, e6.get())
            e6.delete(0, END)
        ee1 = float(e1.get())
        ee2 = float(e2.get())
        answer = float(ee2) - float(ee1)
        tk.Label(frm1, text="----Answer----").grid(row=3, column=1)
        return e6.insert(END, answer)

    eqbtn1 = tk.Button(
        frm1,
        text="  =  ",
        bd=7,
        bg="AntiqueWhite2",
        font=("URW Chancery L", 12, "bold"),
        command=eq,
    )
    eqbtn1.grid(row=1, column=0)


def mul(n=1):
    if n == 1:

        if not len(e4.get()) == 0:
            lb.insert(1, e4.get())
            e4.delete(0, END)
        if not len(e3.get()) == 0:
            e4.insert(END, e3.get())
            e3.delete(0, END)
        if not len(e2.get()) == 0:
            e3.insert(END, e2.get())
            e2.delete(0, END)
        ee1 = e1.get()
        e2.insert(END, ee1)
        ee2 = e2.get()
        e1.delete(0, END)

    elif n == 2:

        ee4 = float(e4.get())
        ee3 = float(e3.get())
        ans = ee4 * ee3
        e3.delete(0, END)

        return e3.insert(END, ans)

    def eq():
        if not len(e6.get()) == 0:
            lb.insert(1, e6.get())
            e6.delete(0, END)
        ee1 = float(e1.get())
        ee2 = float(e2.get())
        answer = float(ee2) * float(ee1)
        tk.Label(frm1, text="----Answer----").grid(row=3, column=1)
        return e6.insert(END, answer)

    eqbtn1 = tk.Button(
        frm1,
        text="  =  ",
        bd=5,
        bg="AntiqueWhite2",
        font=("URW Chancery L", 15, "bold"),
        command=eq,
    )
    eqbtn1.grid(row=1, column=0)


def div(n=1):
    if n == 1:
        if not len(e4.get()) == 0:
            lb.insert(1, e4.get())
            e4.delete(0, END)
        if not len(e3.get()) == 0:
            e4.insert(END, e3.get())
            e3.delete(0, END)
        if not len(e2.get()) == 0:
            e3.insert(END, e2.get())
            e2.delete(0, END)
        ee1 = e1.get()
        e2.insert(END, ee1)
        ee2 = e2.get()
        e1.delete(0, END)
    elif n == 2:

        ee4 = float(e4.get())
        ee3 = float(e3.get())

        if ee4 == 0:
            e6.insert(END, "Undefined")
            tk.Label(frm1, text="-----Infinite-----").grid(row=2, column=1)
            tk.Label(frm1, text="-------Value------").grid(row=3, column=1)
        else:

            answer = float(ee3) / float(ee4)
            tk.Label(frm1, text="----Answer----").grid(row=3, column=1)
            e3.delete(0, END)
            return e3.insert(END, answer)

    def eq():
        if not len(e6.get()) == 0:
            lb.insert(1, e6.get())
            e6.delete(0, END)
        ee1 = float(e1.get())
        ee2 = float(e2.get())

        if ee1 == 0:
            e6.insert(END, "Undefined")
            tk.Label(frm1, text="-----Infinite-----").grid(row=2, column=1)
            tk.Label(frm1, text="-------Value------").grid(row=3, column=1)
        else:

            answer = float(ee2) / float(ee1)
            tk.Label(frm1, text="----Answer----").grid(row=3, column=1)
            return e6.insert(END, answer)

    eqbtn1 = tk.Button(
        frm1,
        text="  =  ",
        bd=5,
        bg="AntiqueWhite3",
        font=("URW Chancery L", 15, "bold"),
        command=eq,
    )
    eqbtn1.grid(row=1, column=0)


def cmd():
    pass


def one(cls):
    e1.insert(END, 1)

    return 1


def two():
    e1.insert(END, 2)

    return 2


def three():
    e1.insert(END, 3)

    return 3


def four():
    e1.insert(END, 4)
    return 4


def five():
    e1.insert(END, 5)

    return 5


def six():
    e1.insert(END, 6)

    return 6


def seven():
    e1.insert(END, 7)

    return 7


def eight():
    e1.insert(END, 8)

    return 8


def nine():
    e1.insert(END, 9)

    return 9


def zero():
    e1.insert(END, 0)

    return 0


def clearall():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e6.delete(0, END)
    tk.Label(frm1, text="                         ").grid(row=2, column=1)
    tk.Label(frm1, text="                         ").grid(row=3, column=1)


def clear1():
    e1.delete(0, END)


def clear2():
    e2.delete(0, END)


def clear3():
    e3.delete(0, END)


def clear4():
    e4.delete(0, END)


def clear6():
    e6.delete(0, END)
    tk.Label(frm1, text="                      ").grid(row=2, column=1)
    tk.Label(frm1, text="                       ").grid(row=3, column=1)


def clrmem():
    lb.delete(0, END)


def recall_mem(event=None):
    try:
        mc = lb.curselection()[0]
        ee5 = lb.get(mc)
        e1.insert(END, ee5)
    except Exception as ex:
        print(ex)

lb.bind("<Double-Button-1>", recall_mem)
lb.bind("<<ListboxSelect>>", recall_mem)


def sto1():
    ee1 = e1.get()
    lb.insert(1, ee1)
    e1.delete(0, END)


def stoans():
    lb.insert(1, e6.get())
    e6.delete(0, END)


def shift4():
    ee4 = e4.get()
    lb.insert(END, ee4)
    e4.delete(0, END)


def shift3():
    ee3 = e3.get()
    e4.insert(END, ee3)
    e3.delete(0, END)


def shift2():
    ee2 = e2.get()
    e3.insert(END, ee2)
    e2.delete(0, END)


def shift1():
    ee1 = e1.get()
    e2.insert(END, ee1)
    e1.delete(0, END)

def shift4to3():
    ee3 = e4.get()
    lb.insert(END, ee3)
    e3.insert(END, ee3)
    e4.delete(0, END)


def shift3to2():
    ee3 = e3.get()
    lb.insert(END, e2)
    e2.insert(END, ee3)
    e3.delete(0, END)


def shift2to1():
    ee2 = e2.get()
    ee1 = e1.get()
    lb.insert(END,ee1)
    e1.insert(END, ee2)
    e2.delete(0, END)


def shift1to4():
    ee1 = e1.get()
    lb.insert(END, e4)
    e4.insert(0, ee1)
    e1.delete(0, END)

def shift1_memory():
    ee1 = e1.get()
    lb.insert(END, ee1)
    e1.delete(0, END)

def shift3to1():
    ee3 = e3.get()
    lb.insert(END, e1)
    e1.insert(END, ee3)
    e3.delete(0, END)

def shift1to3():
    ee1 = e1.get()
    lb.insert(END, e3)
    e3.insert(END, ee1)
    e1.delete(0, END)
    
def decpoint():
    e1.insert(END, str('.'))
    return str('.')
  
########################################################################################################
###Sci Calc Function
#
########################################################################################################
########################################################################################################
def factorial():
    ee1 = int(e1.get())
    answer = math.factorial(ee1)
    e6.insert(END, answer)
    tk.Label(frm1, text="----Answer----").grid(row=2, column=1)


def fmod():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        e3.insert(END, e2.get())
        e2.delete(0, END)
    ee1 = float(e1.get())
    e2.insert(END, ee1)
    ee2 = float(e2.get())
    e1.delete(0, END)

    def eq():
        if not len(e6.get()) == 0:
            lb.insert(1, e6.get())
            e6.delete(0, END)
        ee1 = float(e1.get())
        ee2 = float(e2.get())
        answer = math.fmod(ee1, ee2)
        tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
        return e6.insert(END, answer)

    eqbtn1 = tk.Button(
        frm1,
        text="  =  ",
        bd=5,
        bg="ivory2",
        font=("URW Chancery L", 15, "bold"),
        command=eq,
    )
    eqbtn1.grid(row=1, column=0)

    eqbtn1 = tk.Button(
        frm1,
        text="  =  ",
        bd=5,
        bg="AntiqueWhite3",
        font=("URW Chancery L", 15, "bold"),
        command=eq,
    )
    eqbtn1.grid(row=1, column=0)


def epown():

    ee1 = float(e1.get())
    answer = math.exp(ee1)
    e6.insert(END, answer)
    tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
    return answer


def epownm1():
    ee1 = float(e1.get())
    answer = math.expm1(ee1)
    e6.insert(END, answer)
    tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
    return answer


# math.log(x[, base])
# With one argument, return the natural logarithm of x (to base e).
# With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).


def loge():
    ee1 = float(e1.get())
    answer = math.log1p(ee1)
    e6.insert(END, answer)
    tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
    return answer


def log():
    ee1 = float(e1.get())
    e2.insert(END, ee1)
    ee2 = float(e2.get())
    e1.delete(0, END)
    tk.Label(frm1, text="Enter Base").grid(row=2, column=0)

    def eq():
        if not len(e6.get()) == 0:
            lb.insert(1, e6.get())
            e6.delete(0, END)
        ee1 = float(e1.get())
        ee2 = float(e2.get())
        answer = math.log(ee1, ee2)
        e6.insert(END, answer)
        tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
        return

    eqbtn1 = tk.Button(
        frm1,
        text="  =  ",
        bd=5,
        bg="cornsilk",
        font=("URW Chancery L", 15, "bold"),
        command=eq,
    )
    eqbtn1.grid(row=1, column=0)


def log10():
    ee1 = float(e1.get())
    answer = math.log10(ee1)
    e6.insert(END, answer)
    tk.Label(frm1, text="----Answer----").grid(row=2, column=1)


def pow_of_var():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        e3.insert(END, e2.get())
        e2.delete(0, END)
    ee1 = float(e1.get())
    e2.insert(END, ee1)
    ee2 = float(e2.get())
    e1.delete(0, END)
    tk.Label(frm1, text="Enter number raised").grid(row=2, column=0)

    def eq():
        if not len(e6.get()) == 0:
            lb.insert(1, e6.get())
            e6.delete(0, END)
        ee1 = float(e1.get())
        ee2 = float(e2.get())
        answer = math.pow(ee1, ee2)
        e6.insert(END, answer)
        tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
        return

    eqbtn1 = tk.Button(
        frm1,
        text="  =  ",
        bd=5,
        bg="lavender",
        font=("URW Chancery L", 15, "bold"),
        command=eq,
    )
    eqbtn1.grid(row=1, column=0)


def sqrt():
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.sqrt(ee2)
    e6.insert(END, answer)
    return answer


def inv():
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    if ee2 == 0:
        e6.insert(END, "Undefined")
        tk.Label(frm1, text="----ERROR----").grid(row=2, column=1)

    else:
        answer = 1 / ee2
        e6.insert(END, answer)
        tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
    return


def sin():
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.sin(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
    return


def cos():
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.cos(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
    return


def tan():
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.tan(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
    return


def asin():
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.asin(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
    return


def acos():
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.acos(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
    return


def atan():
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())

    answer = math.atan(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
    return


def sinh():
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.sinh(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
    return


def cosh():
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.cosh(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
    return


def tanh():
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())

    answer = math.tanh(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
    return


def asinh():
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())

    answer = math.asinh(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
    return


def acosh():
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.acosh(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
    return


def atanh():
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())

    answer = math.tanh(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
    return


def signchr():
    ans = float(e1.get()) * -1
    e2.insert(END, ans)
    e1.delete(0, END)
    return


def hyp():
    ee1 = float(e1.get())
    e2.insert(END, ee1)
    ee2 = float(e2.get())
    e1.delete(0, END)
    tk.Label(frm1, text="").grid(row=2, column=0)

    def eq():
        if not len(e6.get()) == 0:
            lb.insert(1, e6.get())
            e6.delete(0, END)
        ee1 = float(e1.get())
        ee2 = float(e2.get())
        answer = math.hypot(ee1, ee2)
        e6.insert(END, answer)
        tk.Label(frm1, text="----Answer----").grid(row=2, column=1)
        return

    eqbtn1 = tk.Button(
        frm1,
        text="  =  ",
        bd=5,
        bg="azure",
        font=("URW Chancery L", 15, "bold"),
        command=eq,
    )
    eqbtn1.grid(row=1, column=0)


def pow2():
    ee2 = str(float(e2.get()))
    ee3 = float(ee2) ** 2
    e3.insert(END, ee3)
    e2.delete(0, END)
    e5.insert(END, "**2")


def pow3():
    ee2 = str(float(e2.get()))
    ee3 = float(ee2) ** 3
    e3.insert(END, ee3)
    e2.delete(0, END)

def pi():
    e1.insert(END, math.pi)

def pi2():
    e1.insert(END, 2 * math.pi)

def pidiv2():
    e1.insert(END, math.pi/2)

def pidiv4():
    e1.insert(END, math.pi/4)

def pidiv8():
    e1.insert(END, math.pi/8)

def pipow2():
    ee1 = math.pi
    ee2 = math.pi
    ee3 = ee1 * ee2
    e1.insert(END, ee3)
def pisq():
    e1.insert(END, math.sqrt(math.pi))
##############################################################################################################
###############################################################################################################
btn1 = tk.Button(
    frm2,
    text="Factorial",
    bd=7,
    bg="CadetBlue3",
    font=("URW Chancery L", 12, "bold"),
    command=factorial,
)
btn1.grid(row=5, column=1)
btn2 = tk.Button(
    frm2,
    text="fmod",
    bd=7,
    bg="DarkOrchid1",
    font=("URW Chancery L", 12, "bold"),
    command=fmod,
)
btn2.grid(row=6, column=1)
btn3 = tk.Button(
    frm2,
    text="epx",
    bd=7,
    bg="DarkSlateGray1",
    font=("URW Chancery L", 12, "bold"),
    command=epown,
)
btn3.grid(row=7, column=1)
btn4 = tk.Button(
    frm2,
    text="epx -1",
    bd=7,
    bg="DeepSkyBlue2",
    font=("URW Chancery L", 12, "bold"),
    command=epownm1,
)
btn4.grid(row=8, column=1)
btn5 = tk.Button(
    frm2,
    text="Log e",
    bd=7,
    bg="DodgerBlue2",
    font=("URW Chancery L", 12, "bold"),
    command=loge,
)
btn5.grid(row=9, column=1)
btn6 = tk.Button(
    frm2,
    text="Log",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=log,
)
btn6.grid(row=10, column=1)
btn7 = tk.Button(
    frm2,
    text="Log10",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=log10,
)
btn7.grid(row=11, column=1)
btn8 = tk.Button(
    frm2,
    text="power x,y",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=pow_of_var,
)
btn8.grid(row=12, column=1)
btn9 = tk.Button(
    frm2,
    text="1/X INV",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=inv,
)
btn9.grid(row=13, column=1)
btn10 = tk.Button(
    frm2,
    text="Squ Root",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=sqrt,
)
btn10.grid(row=14, column=1)
btn11 = tk.Button(
    frm2,
    text="^2",
    bd=7,
    bg="light blue",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn11.grid(row=15, column=1)
btn12 = tk.Button(
    frm2,
    text="^3",
    bd=7,
    bg="light green",
    font=("URW Chancery L", 12, "bold"),
    command=pow2,
)
btn12.grid(row=16, column=1)
btn13 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=pow3,
)
btn13.grid(row=17, column=1)
btn15 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn15.grid(row=18, column=1)


############################################################################################################

btn62 = tk.Button(
    frm2,
    text="  7  ",
    bd=7,
    bg="azure",
    font=("URW Chancery L", 12, "bold"),
    command=seven,
)
btn62.grid(row=6, column=2)
btn63 = tk.Button(
    frm2,
    text="  4  ",
    bd=7,
    bg="azure",
    font=("URW Chancery L", 12, "bold"),
    command=four,
)
btn63.grid(row=7, column=2)
btn0064 = tk.Button(
    frm2,
    text="  1  ",
    bd=7,
    bg="azure",
    font=("URW Chancery L", 12, "bold"),
    command=one,
)
btn0064.grid(row=8, column=2)

btn51 = tk.Button(
    frm2,
    text="mul 4&3",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=lambda: mul(2),
)
btn51.grid(row=9, column=2)
btn52 = tk.Button(
    frm2,
    text="div 4&3",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=lambda: div(2),
)
btn52.grid(row=10, column=2)
btn53 = tk.Button(
    frm2,
    text="add 4&3",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=lambda: add(2),
)
btn53.grid(row=11, column=2)
btn54 = tk.Button(
    frm2,
    text="sub 4&3",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=lambda: subtract(2),
)
btn54.grid(row=12, column=2)


############################################################################################################
############################################################################################################


btn108 = tk.Button(
    frm2,
    text="  8  ",
    bd=7,
    bg="azure",
    font=("URW Chancery L", 12, "bold"),
    command=eight,
)
btn108.grid(row=6, column=3)
btn109 = tk.Button(
    frm2,
    text="  5  ",
    bd=7,
    bg="azure",
    font=("URW Chancery L", 12, "bold"),
    command=five,
)
btn109.grid(row=7, column=3)
btn909 = tk.Button(
    frm2,
    text="  2  ",
    bd=7,
    bg="azure",
    font=("URW Chancery L", 12, "bold"),
    command=two,
)
btn909.grid(row=8, column=3)
btn188 = tk.Button(
    frm2,
    text=" +/-  ",
    bd=7,
    bg="light green",
    font=("URW Chancery L", 12, "bold"),
    command=signchr,
)
btn188.grid(row=9, column=3)
btn189 = tk.Button(
    frm2,
    text="  0   ",
    bd=7,
    bg="light blue",
    font=("URW Chancery L", 12, "bold"),
    command=zero,
)
btn189.grid(row=10, column=3)

############################################################################################################
############################################################################################################

btn99 = tk.Button(
    frm2,
    text=".",
    bd=7,
    bg="light blue",
    font=("URW Chancery L", 12, "bold"),
    command=decpoint,
)
btn99.grid(row=11, column=3)
btn100 = tk.Button(
    frm2,
    text="pi",
    bd=7,
    bg="light blue",
    font=("URW Chancery L", 12, "bold"),
    command=pi,
)
btn100.grid(row=12, column=3)
btn101 = tk.Button(
    frm2,
    text="2pi",
    bd=7,
    bg="light blue",
    font=("URW Chancery L", 12, "bold"),
    command=pi2,
)
btn101.grid(row=13, column=3)
btn102 = tk.Button(
    frm2,
    text="pidiv2",
    bd=7,
    bg="light blue",
    font=("URW Chancery L", 12, "bold"),
    command=pidiv2,
)
btn102.grid(row=14, column=3)
btn103 = tk.Button(
    frm2,
    text="pidiv4",
    bd=7,
    bg="light blue",
    font=("URW Chancery L", 12, "bold"),
    command=pidiv4,
)
btn103.grid(row=15, column=3)
btn104 = tk.Button(
    frm2,
    text="pidiv8",
    bd=7,
    bg="light blue",
    font=("URW Chancery L", 12, "bold"),
    command=pidiv8,
)
btn104.grid(row=16, column=3)
btn105 = tk.Button(
    frm2,
    text="pi pow2",
    bd=7,
    bg="light blue",
    font=("URW Chancery L", 12, "bold"),
    command=pipow2,
)
btn105.grid(row=17, column=3)
btn106 = tk.Button(
    frm2,
    text="pisq",
    bd=7,
    bg="light blue",
    font=("URW Chancery L", 12, "bold"),
    command=pisq,
)
btn106.grid(row=18, column=3)


############################################################################################################
############################################################################################################


btn160 = tk.Button(
    frm2,
    text="  9  ",
    bd=7,
    bg="azure",
    font=("URW Chancery L", 12, "bold"),
    command=nine,
)
btn160.grid(row=6, column=4)
btn161 = tk.Button(
    frm2,
    text="   6  ",
    bd=7,
    bg="azure",
    font=("URW Chancery L", 12, "bold"),
    command=six,
)
btn161.grid(row=7, column=4)
btn1777 = tk.Button(
    frm2,
    text="  3  ",
    bd=7,
    bg="azure",
    font=("URW Chancery L", 12, "bold"),
    command=three,
)
btn1777.grid(row=8, column=4)
btn147 = tk.Button(
    frm2,
    text="Entry 4",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn147.grid(row=9, column=4)
btn150 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn150.grid(row=10, column=4)
btn151 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn151.grid(row=11, column=4)
btn152 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn152.grid(row=12, column=4)
btn153 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn153.grid(row=13, column=4)
btn154 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn154.grid(row=14, column=4)
btn155 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn155.grid(row=15, column=4)
btn156 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn156.grid(row=16, column=4)
btn157 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn157.grid(row=17, column=4)
btn158 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn158.grid(row=18, column=4)

############################################################################################################
############################################################################################################


######################################################
btn167 = tk.Button(
    frm2, text="Btn1", bd=7, bg="cyan", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn167.grid(row=5, column=5)
btn200 = tk.Button(
    frm2,
    text="  /  ",
    bd=7,
    bg="cornsilk",
    font=("URW Chancery L", 12, "bold"),
    command=div,
)
btn200.grid(row=6, column=5)
btn1499 = tk.Button(
    frm2,
    text=" X ",
    bd=7,
    bg="lavender",
    font=("URW Chancery L", 12, "bold"),
    command=mul,
)
btn1499.grid(row=7, column=5)
btn109 = tk.Button(
    frm2,
    text="  -  ",
    bd=7,
    bg="LightPink1",
    font=("URW Chancery L", 12, "bold"),
    command=subtract,
)
btn109.grid(row=8, column=5)
btn140 = tk.Button(
    frm2,
    text="  +  ",
    bd=7,
    bg="light blue",
    font=("URW Chancery L", 12, "bold"),
    command=add,
)
btn140.grid(row=9, column=5)
############################################################################################################
############################################################################################################


btn172 = tk.Button(
    frm2, text="Btn1", bd=7, bg="cyan", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn172.grid(row=10, column=5)

btn192 = tk.Button(
    frm2, text="Btn1", bd=7, bg="cyan", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn192.grid(row=11, column=5)
btn193 = tk.Button(
    frm2, text="Btn1", bd=7, bg="cyan", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn193.grid(row=12, column=5)
btn194 = tk.Button(frm2, text="Btn1", bd=7, bg="cyan", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn194.grid(row=13, column=5)
btn195 = tk.Button(frm2, text="Btn1", bd=7, bg="cyan", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn195.grid(row=14, column=5)
btn196 = tk.Button(frm2, text="Btn1", bd=7, bg="cyan", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn196.grid(row=15, column=5)
btn197 = tk.Button(frm2, text="Btn1", bd=7, bg="cyan", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn197.grid(row=16, column=5)
btn198 = tk.Button(frm2, text="Btn1", bd=7, bg="cyan", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn198.grid(row=17, column=5)
btn199 = tk.Button(frm2, text="Btn1", bd=7, bg="cyan", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn199.grid(row=18, column=5)


############################################################################################################
############################################################################################################

btn173 = tk.Button(
    frm2, text="sin", bd=7, bg="pink", font=("URW Chancery L", 12, "bold"), command=sin
)
btn173.grid(row=5, column=6)
btn174 = tk.Button(
    frm2,
    text="cos",
    bd=7,
    bg="light blue",
    font=("URW Chancery L", 12, "bold"),
    command=cos,
)
btn174.grid(row=6, column=6)
btn175 = tk.Button(
    frm2,
    text="tan",
    bd=7,
    bg="light yellow",
    font=("URW Chancery L", 12, "bold"),
    command=tan,
)
btn175.grid(row=7, column=6)
btn176 = tk.Button(
    frm2,
    text="asin",
    bd=7,
    bg="light green",
    font=("URW Chancery L", 12, "bold"),
    command=asin,
)
btn176.grid(row=8, column=6)
btn177 = tk.Button(
    frm2,
    text="acos",
    bd=7,
    bg="pink",
    font=("URW Chancery L", 12, "bold"),
    command=acos,
)
btn177.grid(row=9, column=6)
btn178 = tk.Button(
    frm2,
    text="atan",
    bd=7,
    bg="cyan",
    font=("URW Chancery L", 12, "bold"),
    command=atan,
)
btn178.grid(row=10, column=6)
btn179 = tk.Button(
    frm2,
    text="sinh",
    bd=7,
    bg="violet",
    font=("URW Chancery L", 12, "bold"),
    command=sinh,
)
btn179.grid(row=11, column=6)
btn180 = tk.Button(
    frm2,
    text="cosh",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cosh,
)
btn180.grid(row=12, column=6)
btn181 = tk.Button(
    frm2,
    text="tanh",
    bd=7,
    bg="lavender",
    font=("URW Chancery L", 12, "bold"),
    command=tanh,
)
btn181.grid(row=13, column=6)
btn182 = tk.Button(
    frm2,
    text="asinh",
    bd=7,
    bg="seashell",
    font=("URW Chancery L", 12, "bold"),
    command=asinh,
)
btn182.grid(row=14, column=6)
btn183 = tk.Button(
    frm2,
    text="acosh",
    bd=7,
    bg="seagreen",
    font=("URW Chancery L", 12, "bold"),
    command=acosh,
)
btn183.grid(row=15, column=6)
btn184 = tk.Button(
    frm2,
    text="atanh",
    bd=7,
    bg="cornsilk",
    font=("URW Chancery L", 12, "bold"),
    command=atanh,
)
btn184.grid(row=16, column=6)
btn185 = tk.Button(
    frm2, text="hyp", bd=7, bg="linen", font=("URW Chancery L", 12, "bold"), command=hyp
)
btn185.grid(row=17, column=6)
btn186 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn186.grid(row=18, column=6)

###########################################################################################################
############################################################################################################


btn110 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn110.grid(row=5, column=7)
btn111 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn111.grid(row=6, column=7)
btn112 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn112.grid(row=7, column=7)
btn113 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn113.grid(row=8, column=7)
btn114 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn114.grid(row=9, column=7)
btn115 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn115.grid(row=10, column=7)
btn116 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn116.grid(row=11, column=7)
btn117 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn117.grid(row=12, column=7)
btn118 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn118.grid(row=13, column=7)
btn119 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn119.grid(row=14, column=7)
btn120 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn120.grid(row=15, column=7)

btn121 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn121.grid(row=16, column=7)
btn122 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn122.grid(row=17, column=7)
btn123 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn123.grid(row=18, column=7)
############################################################################################################
############################################################################################################


gg243 = tk.Button(
    frm2,
    text="CLR ALL",
    bd=7,
    bg="#cbcdd8",
    font=("URW Chancery L", 12, "bold"),
    command=clearall,
)
gg243.grid(row=5, column=8)
gg244 = tk.Button(
    frm2,
    text="CE1",
    bd=7,
    bg="#cbcdd8",
    font=("URW Chancery L", 12, "bold"),
    command=clear1,
)
gg244.grid(row=6, column=8)
gg245 = tk.Button(
    frm2,
    text="CE2",
    bd=7,
    bg="#cbcdd8",
    font=("URW Chancery L", 12, "bold"),
    command=clear2,
)
gg245.grid(row=7, column=8)
gg246 = tk.Button(
    frm2,
    text="CE3",
    bd=7,
    bg="#cbcdd8",
    font=("URW Chancery L", 12, "bold"),
    command=clear3,
)
gg246.grid(row=8, column=8)
gg247 = tk.Button(
    frm2,
    text="CE4",
    bd=7,
    bg="#cbcdd8",
    font=("URW Chancery L", 12, "bold"),
    command=clear4,
)
gg247.grid(row=9, column=8)
gg250 = tk.Button(
    frm2,
    text="CLR ANS",
    bd=7,
    bg="DarkOrchid1",
    font=("URW Chancery L", 12, "bold"),
    command=clear6,
)
gg250.grid(row=10, column=8)
gg251 = tk.Button(
    frm2,
    text="CLR MEM",
    bd=7,
    bg="DeepSkyBlue2",
    font=("URW Chancery L", 12, "bold"),
    command=clrmem,
)
gg251.grid(row=11, column=8)
gg252 = tk.Button(
    frm2,
    text="MEM ENTRY",
    bd=7,
    bg="LightGoldenrod1",
    font=("URW Chancery L", 12, "bold"),
    command=sto1,
)
gg252.grid(row=12, column=8)
gg253 = tk.Button(
    frm2,
    text="MEM ANS",
    bd=7,
    bg="light yellow",
    font=("URW Chancery L", 12, "bold"),
    command=stoans,
)
gg253.grid(row=13, column=8)
gg254 = tk.Button(
    frm2,
    text="RECALL",
    bd=7,
    bg="ivory2",
    font=("URW Chancery L", 12, "bold"),
    command=recall_mem,
)
gg254.grid(row=14, column=8)
gg255 = tk.Button(
    frm2,
    text="Shift1-2",
    bd=7,
    bg="ivory3",
    font=("URW Chancery L", 12, "bold"),
    command=shift1,
)
gg255.grid(row=15, column=8)
gg256 = tk.Button(
    frm2,
    text="Shift2-3",
    bd=7,
    bg="pink",
    font=("URW Chancery L", 12, "bold"),
    command=shift2,
)
gg256.grid(row=16, column=8)
gg257 = tk.Button(
    frm2,
    text="Shift3-4",
    bd=7,
    bg="yellow",
    font=("URW Chancery L", 12, "bold"),
    command=shift3,
)
gg257.grid(row=17, column=8)
gg258 = tk.Button(
    frm2,
    text="Shift4-Mem",
    bd=7,
    bg="violet",
    font=("URW Chancery L", 12, "bold"),
    command=shift4,
)
gg258.grid(row=18, column=8)


############################################################################################################
############################################################################################################
btn30 = tk.Button(
    frm2,
    text="Shift4to3",
    bd=7,
    bg="light green",
    font=("URW Chancery L", 12, "bold"),
    command=shift4to3,
)
btn30.grid(row=5, column=9)
btn31 = tk.Button(
    frm2,
    text="Shift3to2",
    bd=7, bg="light blue",
    font=("URW Chancery L", 12, "bold"),
    command=shift3to2
)
btn31.grid(row=6, column=9)
btn32 = tk.Button(
    frm2,
    text="Shift2to1",
    bd=7,
    bg="violet",
    font=("URW Chancery L", 12, "bold"),
    command=shift2to1
)
btn32.grid(row=7, column=9)
btn33 = tk.Button(
    frm2,
    text="Shift1to4",
    bd=7, bg="pink",
    font=("URW Chancery L",
          12, "bold"),
    command=shift1to4
)
btn33.grid(row=8, column=9)
btn34 = tk.Button(
    frm2,
    text="Shift1to3",
    bd=7, bg="pink",
    font=("URW Chancery L", 12, "bold"),
    command=shift1to3
)
btn34.grid(row=9, column=9)
btn35 = tk.Button(
    frm2,
    text="Shift3to1",
    bd=7,
    bg="pink",
    font=("URW Chancery L", 12, "bold"),
    command=shift3to1
)
btn35.grid(row=10, column=9)
btn36 = tk.Button(
    frm2,
    text="shift 1 to Memory",
    bd=7,
    bg="lawngreen",
    font=("URW Chancery L", 12, "bold"),
    command=shift1_memory
)
btn36.grid(row=11, column=9)
btn37 = tk.Button(
    frm2, text="Btn1", bd=7, bg="pink", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn37.grid(row=12, column=9)
btn38 = tk.Button(
    frm2, text="Btn1", bd=7, bg="pink", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn38.grid(row=13, column=9)
btn39 = tk.Button(
    frm2, text="Btn1", bd=7, bg="pink", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn39.grid(row=14, column=9)
btn40 = tk.Button(
    frm2, text="Btn1", bd=7, bg="pink", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn40.grid(row=15, column=9)
btn41 = tk.Button(
    frm2, text="Btn1", bd=7, bg="pink", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn41.grid(row=16, column=9)
btn42 = tk.Button(
    frm2, text="Btn1", bd=7, bg="pink", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn42.grid(row=17, column=9)
btn43 = tk.Button(
    frm2, text="Btn1", bd=7, bg="pink", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn43.grid(row=18, column=9)
############################################################################################################
############################################################################################################
btn21 = tk.Button(
    frm2, text="Btn1", bd=7, bg="pink", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn21.grid(row=5, column=10)
btn22 = tk.Button(
    frm2, text="Btn1", bd=7, bg="pink", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn22.grid(row=6, column=10)
btn23 = tk.Button(
    frm2, text="Btn1", bd=7, bg="pink", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn23.grid(row=7, column=10)
btn24 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="purple",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn24.grid(row=8, column=10)
btn25 = tk.Button(
    frm2, text="Btn1", bd=7, bg="pink", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn25.grid(row=9, column=10)
btn26 = tk.Button(
    frm2,
    text="Btn1",
    bd=7,
    bg="purple",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn26.grid(row=10, column=10)
btn27 = tk.Button(
    frm2, text="Btn1", bd=7, bg="pink", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn27.grid(row=11, column=10)
btn28 = tk.Button(
    frm2, text="Btn1", bd=7, bg="blue", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn28.grid(row=12, column=10)
btn29 = tk.Button(
    frm2, text="F", bd=7, bg="pink", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn29.grid(row=13, column=10)
btn79 = tk.Button(
    frm2, text="E", bd=7, bg="cyan", font=("URW Chancery L", 12, "bold"), command=cmd
)
btn79.grid(row=14, column=10)
btn80 = tk.Button(
    frm2,
    text="D",
    bd=7,
    bg="yellow",
    font=("URW Chancery L", 12, "bold"),
    command=cmd,
)
btn80.grid(row=15, column=10)
btn81 = tk.Button(
    frm2,
    text="  C ",
    bd=7,
    bg="orange",
    font=("URW Chancery L", 12, "bold"),
    command=seven,
)
btn81.grid(row=16, column=10)
btn82 = tk.Button(
    frm2,
    text="  B  ",
    bd=7,
    bg="red",
    font=("URW Chancery L", 12, "bold"),
    command=four,
)
btn82.grid(row=17, column=10)
btn83 = tk.Button(
    frm2,
    text="  A ",
    bd=7,
    bg="cyan",
    font=("URW Chancery L", 12, "bold"),
    command=one,
)
btn83.grid(row=18, column=10)

####################Frame#####Tab1

f1 = ttk.Frame(notebook)
notebook.add(f1, text="BaseNumberCalc")

        



def decimal_to_any(num: int, base: int) -> str:
   
  
  
    if isinstance(num, float):
        raise TypeError("int() can't convert non-string with explicit base")
    if num < 0:
        raise ValueError("parameter must be positive int")
    if isinstance(base, str):
        raise TypeError("'str' object cannot be interpreted as an integer")
    if isinstance(base, float):
        raise TypeError("'float' object cannot be interpreted as an integer")
    if base in (0, 1):
        raise ValueError("base must be >= 2")
    if base > 36:
        raise ValueError("base must be <= 36")
    # fmt: off
    ALPHABET_VALUES = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F',
                       '16': 'G', '17': 'H', '18': 'I', '19': 'J', '20': 'K', '21': 'L',
                       '22': 'M', '23': 'N', '24': 'O', '25': 'P', '26': 'Q', '27': 'R',
                       '28': 'S', '29': 'T', '30': 'U', '31': 'V', '32': 'W', '33': 'X',
                       '34': 'Y', '35': 'Z'}
    # fmt: on
    new_value = ""
    mod = 0
    div = 0
    while div != 1:
        div, mod = divmod(num, base)
        if base >= 11 and 9 < mod < 36:
            actual_value = ALPHABET_VALUES[str(mod)]
            mod = actual_value
        new_value += str(mod)
        div = num // base
        num = div
        
        if div == 0:
            lboxx3.insert(END, str(new_value[::-1]))
            return str(new_value[::-1])
            
        elif div == 1:
            new_value += str(div)
            
            lboxx3.insert(END, str(new_value[::-1]))
            return str(new_value[::-1])
       
    return new_value[::-1]


    for base in range(2, 37):
        for num in range(1000):
            assert int(decimal_to_any(num, base), base) == num, (
                num,
                base,
                decimal_to_any(num, base),
                int(decimal_to_any(num, base), base) )
            lboxx3.delete(0, END)
            


def clearlist():
    lboxx1.delete(0, END)
    lboxx2.delete(0, END)
    lboxx3.delete(0, END)

def nothing():
    pass
label1 = tk.Label(f1, text="Input Whole Number:")
label1.grid(row=2, column=1)
label1 = tk.Label(f1, text="Select the Base (2-36):")
label1.grid(row=2, column=2)   
tk.Label(f1, text=" Decimal to Selected Base Converter").grid(row=2, column=3)
en1 = tk.Entry(f1, bg="wheat", bd=7)
en1.grid(row=5, column=1)
sp = tk.Spinbox(f1, from_= 2, to = 36, increment=1, font=('sans-serif', 10))
sp.grid(row=5, column=2)               
               

lboxx1 = tk.Listbox(f1, bd=7)
lboxx1.grid(row=2, column=3)
lboxx2 = tk.Listbox(f1, bd=7)
lboxx2.grid(row=2, column=4)
labeltwo = tk.Label(f1, text="Selected Base").grid(row=1,column=4)
lboxx3 = tk.Listbox(f1, bd=7)
lboxx3.grid(row=2, column=5)
labelone= tk.Label(f1,text="Converted base number").grid(row=1,column=5)
def from_entry(num, base):
    
    try:
        num = int(en1.get())
        base = int(sp.get())
        lboxx1.insert(END, num)
        lboxx2.insert(END, base)
        print(num, base)
        decimal_to_any(num, base)
        
    # except block 
    except ValueError as ex:
        print(ex)

b1 = tk.Button(f1, text="Convert", bd=7, command=lambda: from_entry(en1.get(), sp.get())) 
b1.grid(row=4, column=3)
def from_entry(num, base):
    
    try:
        num = int(en1.get())
        base = int(sp.get())
        lboxx1.insert(END, num)
        lboxx2.insert(END, base)
        print(num, base)
        decimal_to_any(num, base)
        
    # except block 
    except ValueError as ex:
        print(ex)

b2 = tk.Button(f1, text="Clear", bd=7, command=clearlist)
b2.grid(row=5, column=3) 
b3 = tk.Button(f1, text="feature", bd=7, command=nothing)
b3.grid(row=6, column=3) 

   
       




   
    
































































































        
##        import doctest
##
##        doctest.testmod()
##
##        for base in range(2, 37):
##            for num in range(1000):
##                assert int(decimal_to_any(num, base), base) == num, (
##                    num,
##                    base,
##                    decimal_to_any(num, base),
##                    int(decimal_to_any(num, base), base) )
##                lboxx3.delete(0, END)
##                
##
##
##    def clearlist():
##        lboxx1.delete(0, END)
##        lboxx2.delete(0, END)
##        lboxx3.delete(0, END)
##
##    def nothing():
##        pass
##    label1 = tk.Label(f1, text="Input Whole Number:")
##    label1.grid(row=2, column=1)
##    label1 = tk.Label(f1, text="Select the Base (2-36):")
##    label1.grid(row=2, column=2)   
##    tk.Label(f1, text=" Decimal to Selected Base Converter").grid(row=2, column=3)
##    en1 = tk.Entry(f1, bg="wheat", bd=7)
##    en1.grid(row=5, column=1)
##    sp = tk.Spinbox(f1, from_= 2, to = 36, increment=1, font=('sans-serif', 10))
##    sp.grid(row=5, column=2)               
##                   
##
##    lboxx1 = tk.Listbox(f1, bd=7)
##    lboxx1.grid(row=16, column=3)
##    lboxx2 = tk.Listbox(f1, bd=7)
##    lboxx2.grid(row=16, column=4)
##    labeltwo = tk.Label(f1, text="Selected Base").grid(row=15,column=4)
##
##    b1 = tk.Button(f1, text="Convert", bd=7, command=lambda: from_entry(en1.get(), sp.get())) 
##    b1.grid(row=20, column=1)
##    b2 = tk.Button(f1, text="Clear", bd=7, command=clearlist)
##    b2.grid(row=20, column=2) 
##    b3 = tk.Button(f1, text="feature", bd=7, command=nothing)
##    b3.grid(row=20, column=3) 
##            
##
##
##









    

















































































if __name__ == "__main__":
























    root.mainloop()




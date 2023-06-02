import tkinter as tk
import tkinter.font
from tkinter import *
from tkinter import ttk
import math

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Scientific Calculator")
        self.root.resizable(1, 1)
        self.root.geometry("1200x800")
        self.equation = StringVar()
        self.expression = ""
        self.value = ""
        self.ans = ""

        self.create_gui()

    def create_gui(self):
##        self.f1 = Frame(self.root)
##        self.f1.grid()
##        self.f1.configure(bg="burlywood4")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(row=0, column=1)
        self.f1 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f1.grid(row=0, column=1)

        self.notebook.add(self.f1, text="TAB1")

        self.f2 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f2.grid(row=0, column=1)

        self.notebook.add(self.f2, text="TAB")
        self.f3 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f4 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f5 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f6 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f7 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f8 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f9 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f10 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f11 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f12 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f13 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f14 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f15 = ttk.Frame(self.notebook, width=1900, height=1080)

        self.f3.grid(row=0, column=1)
        self.f4.grid(row=0, column=1)
       
        self.f5.grid(row=0, column=1)
        self.f6.grid(row=0, column=1)
        self.f7.grid(row=0, column=1)
        self.f8.grid(row=0, column=1)
        self.f9.grid(row=0, column=1)
        self.f10.grid(row=0, column=1)
        self.f11.grid(row=0, column=1)
        self.f12.grid(row=0, column=1)
        self.f13.grid(row=0, column=1)
        self.f14.grid(row=0, column=1)
        self.f15.grid(row=0, column=1)
        self.notebook.add(self.f1, text="CALCULATOR")
        self.notebook.add(self.f2, text="MEMORY")
        self.notebook.add(self.f3, text="MORE SCI")
        self.notebook.add(self.f4, text="TAB4")
        self.notebook.add(self.f5, text="TAB5")
        self.notebook.add(self.f6, text="TAB6")
        self.notebook.add(self.f7, text="TAB7")
        self.notebook.add(self.f8, text="TAB8")
        self.notebook.add(self.f9, text="TAB9")
        self.notebook.add(self.f10, text="10")
        self.notebook.add(self.f11,  text="11")
        self.notebook.add(self.f12,  text="12")
        self.notebook.add(self.f13, text="13")
        self.notebook.add(self.f14, text="14")
        self.notebook.add(self.f15, text= "15")
              
        self.frm1 = ttk.Frame(self.f1, height=20, width=200)
        self.frm1.grid(row=0, column=1, columnspan=2)

        self.fff = tk.Canvas(self.f3, height=100, width=110, background="Ivory3")
        self.fff.grid(row=3, column=0, columnspan=4)

        self.frm3 = tk.Canvas(self.f2, height=100, width=200, background="azure")
        self.frm3.grid(row=6, column=6)
        tk.Label(self.frm3, text="Memory").grid(row=1, column=1)
        tk.Label(self.frm3, text="History").grid(row=1, column=3)
        self.lb = tk.Listbox(self.frm3)
        self.lb.grid(row=3, column=1, rowspan=4)
        self.lb2 = tk.Listbox(self.frm3)
        self.lb2.grid(row=3, column=3, rowspan=4)
        self.e1 = Entry(
            self.f1,
            textvariable=self.equation,
            width=60,
            font=("Comic Sans MS", 15),
            bd=15,
            bg="azure2",
            justify=LEFT,
            disabledbackground="wheat",
            disabledforeground="black",
        )

        self.e1.grid(row=0, columnspan=8)
        self.e2 = Entry(
            self.f3,
            textvariable=self.equation,
            width=60,
            font=("Comic Sans MS", 15),
            bd=15,
            bg="azure2",
            justify=LEFT,
            disabledbackground="wheat",
            disabledforeground="black",
        )
   
        self.e2.grid(row=0, columnspan=8)
        self.e3= Entry(
            self.f3,
            textvariable=None,
            width=60,
            font=("Comic Sans MS", 15),
            bd=15,
            bg="azure2",
            justify=LEFT,
            disabledbackground="wheat",
            disabledforeground="black",
        )
      
        self.e3.grid(row=3, column=2, columnspan=10)

        

        self.create_menu()

        self.create_number_buttons()
        self.create_operator_buttons()
        self.tab3_buttons()
        self.root.mainloop()
        
    def create_menu(self):
        self.menubar = Menu(self.notebook)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Standard", command=self.standard)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Scientific", command=self.scientific)
        self.root.config(menu=self.menubar)

    def create_number_buttons(self):
        font = tkinter.font.Font(
            size=12,
            weight="bold",
            family="URW Chancery L",
        )
        h = 2
        w = 7
        actvbgnd = "white"
        bg1 = "light blue"
        fg2 = "black"

        numberpad = [7, 8, 9, 4, 5, 6, 1, 2, 3]
        i = 0
        for j in range(3):
            for k in range(3):
                Button(
                    self.f1,
                    command=lambda x=str(numberpad[i]): self.pressbtn(x),
                    text=str(numberpad[i]),
                    bg=bg1,
                    fg=fg2,
                    activebackground=actvbgnd,
                    height=h,
                    width=w,
                    font=font,
                ).grid(row=j + 2, column=k)
                i += 1

        r = 5
        c = 7
        Button(
            self.f1,
            command=lambda: self.pressbtn("0"),
            text="0",
            bg=bg1,
            fg=fg2,
            activebackground=actvbgnd,
            height=h,
            width=w,
            font=font,
        ).grid(row=r, column=c - 7)
        Button(
            self.f1,
            command=lambda: self.pressbtn("00"),
            text="00",
            bg=bg1,
            fg=fg2,
            activebackground=actvbgnd,
            height=h,
            width=w,
            font=font,
        ).grid(row=r, column=c - 6)
        Button(
            self.f1,
            command=lambda: self.recall("00"),
            text="00",
            bg=bg1,
            fg=fg2,
            activebackground=actvbgnd,
            height=h,
            width=w,
            font=font,
        ).grid(row=r, column=c - 6)
    def create_operator_buttons(self):
        h = 2
        w = 7
        actvbgnd = "seashell"
        bg1 = "skyblue"
        bg3 = "limegreen"
        bg2 = "cornsilk3"
        bg4=   "plum3"
        bg5 = "orange2"
        fg2 = "black"

        list1 = [
            "(",
            ")",
            "%",
            "asin",
            "sin",
            "log",
            "x^2",
            "acos",
            "cos",
            "ln",
            "x^3",
            "atan",
            "tan",
            "e^x",
            "1/x",
            "x^y",
            "e",
            "π",
            "√x",
            "sgn",
        ]
        list2 = [
            "(",
            ")",
            "%",
            "asin(",
            "sin(",
            "log(",
            "^2",
            "acos(",
            "cos(",
            "ln(",
            "^3",
            "atan(",
            "tan(",
            "e^",
            "1/",
            "^",
            "e",
            "π",
            "√(",
            "sgn(",
        ]
        i = 0
        for j in range(5):
            for k in range(4):
                Button(
                    self.f1,
                    command=lambda x=list2[i]: self.pressbtn(x),
                    text=list1[i],
                    bg=bg1 if i < 4 else bg3 if i < 14 else bg2,
                    fg=fg2,
                    activebackground=actvbgnd,
                    height=h,
                    width=w,
                    font=("URW Chancery L", 14, "bold"),
                ).grid(row=j+1, column=k + 4)
                i += 1

        r = 5
        c = 7
        Button(
            self.f1,
            command=lambda: self.pressbtn("."),
            text="•",
            bg=bg3,
            fg=fg2,
            activebackground=actvbgnd,
            height=h,
            width=w,
            font=("URW Chancery L", 14, "bold"),
        ).grid(row=r, column=c - 5)
        Button(
            self.f1,
            command=lambda: self.pressbtn("+"),
            text="+",
            bg=bg3,
            fg=fg2,
            activebackground=actvbgnd,
            height=h,
            width=w,
            font=("URW Chancery L", 14, "bold"),
        ).grid(row=r - 2, column=c - 4)
        Button(
            self.f1,
            command=lambda: self.pressbtn("-"),
            text="–",
            bg=bg3,
            fg=fg2,
            activebackground=actvbgnd,
            height=h,
            width=w,
            font=("URW Chancery L", 14, "bold"),
        ).grid(row=r - 3, column=c - 4)
        Button(
            self.f1,
            command=lambda: self.pressbtn("/"),
            text="/",
            bg=bg3,
            fg=fg2,
            activebackground=actvbgnd,
            height=h,
            width=w,
            font=("URW Chancery L", 14, "bold"),
        ).grid(row=r - 4, column=c - 5)
        Button(
            self.f1,
            command=lambda: self.pressbtn("*"),
            text="✶",
            bg=bg3,
            fg=fg2,
            activebackground=actvbgnd,
            height=h,
            width=w,
            font=("URW Chancery L", 14, "bold"),
        ).grid(row=r - 4, column=c - 4)
        Button(
            self.f1,
            command=self.equal,
            text="=",
            bg=bg2,
            fg=fg2,
            activebackground=actvbgnd,
            height=h,
            width=w,
            font=("URW Chancery L", 14, "bold"),
            pady=10,
        ).grid(
            row=r +2,
            column=c + 3,
            rowspan=2,
        )
        Button(
            self.f1,
            command=self.memory,
            text="Memory",
            bg=bg2,
            fg=fg2,
            activebackground=actvbgnd,
            height=h,
            width=w,
            font=("URW Chancery L", 14, "bold"),
            pady=10,
        ).grid(
            row=r +1,
            column=c - -8,
            rowspan=2,
        )
        Button(
            self.f1,
            command=self.clear,
            text="Clear",
            bg="lavender",
            fg=fg2,
            activebackground=actvbgnd,
            height=h,
            width=w,
            font=("URW Chancery L", 14, "bold"),
            pady=10,
        ).grid(
            row=r - 2,
            column=c - -8,
            rowspan=2,
        )
        Button(
            self.f1,
            command=self.recall_mem,
            text="Recall",
            bg="lavender",
            fg=fg2,
            activebackground=actvbgnd,
            height=h,
            width=w,
            font=("URW Chancery L", 14, "bold"),
            pady=10,
        ).grid(
            row=r - 3,
            column=c - -8,
            rowspan=2,
        )
###################################
        

    ##############################################################

    def binding(self):
        self.lb.bind("<Double-Button-1>", self.recall_mem)
        self.lb.bind("<<ListboxSelect>>", self.recall_mem)


    def standard(self):
        self.root.geometry("361x350")
        self.e1["width"] = 28
        self.e1.grid(row=0, columnspan=4, sticky=EW)
        self.root.title("Standard Calculator")

    def scientific(self):
        self.root.geometry("742x350")
        self.e1["width"] = 60
        self.e1.grid(row=0, columnspan=8)
        self.root.title("Scientific Calculator")

    def pressbtn(self, num):
        self.expression = self.expression + str(num)
        self.equation.set(self.expression)
     
        if num in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "(", ")", "00"]:
            self.value += num
            try:
                self.ans = str(eval(self.value))
            except:
                self.ans = "Invalid Expression"

        elif num in ["+", "-", "/", "*", ".", "1/", "sgn("]:
            self.value += num

        elif num in ["asin(", "acos(", "atan(", "sin(", "cos(", "tan("]:
            self.value += "math." + num

        elif num == "^":
            self.value += "**"

        elif num == "%":
            self.value += "/100"
            try:
                self.ans = str(eval(self.value))
            except:
                self.ans = "Invalid Expression"
        elif num == "^2":
            self.value += "**2"
            try:
                self.ans = str(eval(self.value))
            except:
                self.ans = "Invalid Expression"
        elif num == "^3":
            self.value += "**3"
            try:
                self.ans = str(eval(self.value))
            except:
                self.ans = "Invalid Expression"

        elif num == "√(":
            self.value += "math.sqrt("

        elif num == "e":
            self.value += "math.e"
            try:
                self.ans = str(eval(self.value))
            except:
                self.ans = "Invalid Expression"
        elif num == "π":
            self.value += "math.pi"
            try:
                self.ans = str(eval(self.value))
            except:
                self.ans = "Invalid Expression"
        elif num == "log(":
            self.value += "math.log10("
        elif num == "ln(":
            self.value += "math.log("
        elif num == "e^":
            self.value += "math.e**"
#################################################################
    def tab3_buttons(self):


      
       
        self.btn6 = tk.Button(
            self.f3,
            text="asin",
            bd=7,
            bg="light green",
            font=("URW Chancery L", 12, "bold"),
            command=lambda:self.asin()
        )

        self.btn6.grid(row=8, column=6)
        self.btn7 = tk.Button(
            self.f3,
            text="acos",
            bd=7,
            bg="pink",
            font=("URW Chancery L", 12, "bold"),
                  command=lambda:self.acos())
        self.btn7.grid(row=9, column=6)

        self.btn8 = tk.Button(
            self.f3,
            text="atan",
            bd=7,
            bg="cyan",
            font=("URW Chancery L", 12, "bold"),
            command=lambda:self.atan()
        )
        self.btn8.grid(row=10, column=6)
        self.btn9 = tk.Button(
            self.f3,
            text="sinh",
            bd=7,
            bg="violet",
            font=("URW Chancery L", 12, "bold"),
            command=lambda:self.sinh,
        )
        self.btn9.grid(row=11, column=6)
        self.btn10 = tk.Button(
            self.f3,
            text="cosh",
            bd=7,
            bg="orange",
            font=("URW Chancery L", 12, "bold"),
            command=lambda:self.cosh()
        )
        self.btn10.grid(row=12, column=6)
        self.btn11 = tk.Button(
            self.f3,
            text="tanh",
            bd=7,
            bg="lavender",
            font=("URW Chancery L", 12, "bold"),
            command=lambda:self.tanh()
        )
        self.btn11.grid(row=13, column=6)
        self.btn12 = tk.Button(
            self.f3,
            text="asinh",
            bd=7,
            bg="seashell",
            font=("URW Chancery L", 12, "bold"),
            command=lambda:self.asinh()
        )
        self.btn12.grid(row=14, column=6)
        self.btn13 = tk.Button(
            self.f3,
            text="acosh",
            bd=7,
            bg="seagreen",
            font=("URW Chancery L", 12, "bold"),
            command=lambda:self.acosh()
        )
        self.btn13.grid(row=15, column=6)
        self.btn14 = tk.Button(
            self.f3,
            text="atanh",
            bd=7,
            bg="cornsilk",
            font=("URW Chancery L", 12, "bold"),
            command=lambda:self.atanh()
        )
        self.btn14.grid(row=16, column=6)
        self.btn15 = tk.Button(
            self.f3, text="hyp", bd=7, bg="linen", font=("URW Chancery L", 12, "bold"), command=lambda:self.hyp()
        )
        self.btn15.grid(row=17, column=6)



##############################################################

    def binding(self):
        self.lb.bind("<Double-Button-1>", self.recall_mem)
        self.lb.bind("<<ListboxSelect>>", self.recall_mem)


    def standard(self):
        self.root.geometry("361x350")
        self.e1["width"] = 28
        self.e1.grid(row=0, columnspan=4, sticky=EW)
        self.root.title("Standard Calculator")

    def scientific(self):
        self.root.geometry("742x350")
        self.e1["width"] = 60
        self.e1.grid(row=0, columnspan=8)
        self.root.title("Scientific Calculator")

    def pressbtn(self, num):
        self.expression = self.expression + str(num)
        self.equation.set(self.expression)
     
        if num in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "(", ")", "00"]:
            self.value += num
            try:
                self.ans = str(eval(self.value))
            except:
                self.ans = "Invalid Expression"

        elif num in ["+", "-", "/", "*", ".", "1/", "sgn("]:
            self.value += num

        elif num in ["asin(", "acos(", "atan(", "sin(", "cos(", "tan("]:
            self.value += "math." + num

        elif num == "^":
            self.value += "**"

        elif num == "%":
            self.value += "/100"
            try:
                self.ans = str(eval(self.value))
            except:
                self.ans = "Invalid Expression"
        elif num == "^2":
            self.value += "**2"
            try:
                self.ans = str(eval(self.value))
            except:
                self.ans = "Invalid Expression"
        elif num == "^3":
            self.value += "**3"
            try:
                self.ans = str(eval(self.value))
            except:
                self.ans = "Invalid Expression"

        elif num == "√(":
            self.value += "math.sqrt("

        elif num == "e":
            self.value += "math.e"
            try:
                self.ans = str(eval(self.value))
            except:
                self.ans = "Invalid Expression"
        elif num == "π":
            self.value += "math.pi"
            try:
                self.ans = str(eval(self.value))
            except:
                self.ans = "Invalid Expression"
        elif num == "log(":
            self.value += "math.log10("
        elif num == "ln(":
            self.value += "math.log("
        elif num == "e^":
            self.value += "math.e**"
        


     

    def equal(self):
        if self.value == "":
            self.ans = ""
        self.equation.set(self.ans)
        self.ans = ""
        self.value = ""
        self.expression = ""
        self.lb2.insert("end", str(self.expression) + str(self.value) + str(self.ans))



    def memory(self):
        self.lb.insert("end", self.e1.get())


    def clear(self):
        self.e1.delete(0, "end")

    def recall_mem(self, event=None):
        self.ans = ""
        self.value = ""
        self.expression = ""
        self.lb2.insert("end", str(self.expression) + str(self.value) + str(self.ans))



    def memory(self):
        self.lb.insert("end", self.e1.get())


    def clear(self):
        self.e1.delete(0, "end")

    def recall_mem(self, event=None):
        mc = self.lb.curselection()[0]
        self.ee1 = self.lb.get(mc)
        self.e1.insert(END, self.ee5)

    def factorial(self):
        self.ee1 = int(self.e1.get())
        self.answer = math.factorial(self.ee1)
        self.e3.insert(END, self.answer)
       


    def fmod(self):
        if not len(self.e4.get()) == 0:
            self.lb.insert(1, self.e4.get())
            self.e4.delete(0, END)
        if not len(self.e3.get()) == 0:
            self.e4.insert(END, self.e3.get())
            self.e3.delete(0, END)
        if not len(self.e2.get()) == 0:
            self.e3.insert(END, self.e2.get())
            self.e2.delete(0, END)
        self.ee1 = float(self.e1.get())
        self.e2.insert(END, self.ee1)
        self.ee2 = float(self.e2.get())
        self.e1.delete(0, END)
    def epownm1(self):
        self.ee1 = float(self.e1.get())
        self.answer = math.expm1(self.ee1)
        self.e3.insert(END, self.answer)
        tk.Label(self.frm1, text="----answer----").grid(row=2, column=1)
      

    def pow_of_var(self):

        self.ee1 = float(self.e1.get())
        self.e1.delete(0, END)
        
        self.ee2 = float(self.e21.get())
        self.e1.delete(0, END)
        tk.Label(self.frm1, text="Enter number raised").grid(row=2, column=0)
    def asin(self):
        self.e2.delete(0, "end")
        self.e2.insert(END, float(self.e1.get()))
        
        self.ee2 = float(self.e2.get())
        self.answer = math.asin(self.ee2)
        self.e3.insert(END, self.answer)
     
    


    def acos(self):
        self.e2.delete(0, "end")
        self.e2.insert(END, float(self.e1.get()))
        self.ee2 = float(self.e2.get())
        self.answer = math.acos(self.ee2)
        self.e3.insert(END, self.answer)
      

    def atan(self):
        self.e2.delete(0, "end")
        self.e2.insert(END, float(self.e1.get()))
       
        self.ee2 = float(self.e2.get())

        self.answer = math.atan(self.ee2)
        self.e3.insert(END, self.answer)
     


    def sinh(self):
        self.e2.delete(0, "end")
        self.e2.insert(END, float(self.e1.get()))
       
        self.ee2 = float(self.e2.get())
        self.answer = math.sinh(self.ee2)
        self.e3.delete(0,"end")
        self.e3.insert(END, self.answer)
      

    def cosh(self):
        self.e2.delete(0, "end")
        self.e2.insert(END, float(self.e1.get()))
       
        self.ee2 = float(self.e2.get())
        self.answer = math.cosh(self.ee2)
        self.e3.delete(0,"end")
        self.e3.insert(END, self.answer)
       
    def tanh(self):
        self.e2.delete(0, "end")
        self.e2.insert(END, float(self.e1.get()))
       
        self.ee2 = float(self.e2.get())

        self.answer = math.tanh(self.ee2)
        self.e3.delete(0,"end")
        self.e3.insert(END, self.answer)
       
        return


    def asinh(self):
        self.e2.delete(0, "end")
        self.e2.insert(END, float(self.e1.get()))
        self.e1.delete(0, END)
        self.ee2 = float(self.e2.get())

        self.answer = math.asinh(self.ee2)
        self.e3.delete(0,"end")
        self.e3.insert(END, self.answer)

        return


    def acosh(self):
        self.e2.delete(0, "end")
        self.e2.insert(END, float(self.e1.get()))
        self.e1.delete(0, END)
        self.ee2 = float(self.e2.get())
        self.answer = math.acosh(self.ee2)
        self.e3.delete(0,"end")
        self.e3.insert(END, self.answer)
        
        return


    def atanh(self):
        self.e2.delete(0, "end")
        self.e2.insert(END, float(self.e1.get()))
       
        self.ee2 = float(self.e2.get())

        self.answer = math.tanh(self.ee2)
        self.e3.delete(0,"end")
        self.e3.insert(END, self.answer)
      
        return


    def signchr(self):
        self.e2.delete(0, "end")
        ans = float(self.e1.get()) * -1
        self.e2.insert(END, ans)
        self.e3.delete(0,"end")
        self.e1.delete(0, END)
        return


    def hyp(self):
        pass
        self.ee1 = float(self.e1.get())
        
        self.ee2 = float(self.e2.get())
        self.e3.delete(0,"end")
       



    def pi(self):
        self.e3.insert(END, math.pi)
        
    def pi2(self):
        self.e3.insert(END, 2 * math.pi)

    def pidiv2(self):
        self.e3.insert(END, math.pi/2)

    def pidiv4(self):
        self.e3.insert(END, math.pi/4)

    def pidiv8(self):
        self.e3.insert(END, math.pi/8)

    def pipow2(self):
        self.ee1 = math.pi
        self.ee2 = math.pi
        self.ee3 = self.ee1 * self.ee2
        self.e1.insert(END, self.ee3)
    def pisq(self):
        self.e3.insert(END, math.sqrt(math.pi))



    def shift_to_entry(self):
        ee3= self.e3.get()
        self.e1.delete(0, "end")
        self.e1.insert(END, ee3)
        




calc = Calculator()

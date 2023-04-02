import math
from tkinter import *


root = Tk()
root.title("Calculator")

#setting up the screen field

field = Entry(root, width=60, borderwidth=5)
field.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

#Numbers appear on screen
def btn_onClick(number):
        currentNumber = field.get()
        field.delete(0, END)
        field.insert(0, str(currentNumber) + str(number))

#Clears the calculator
def clrBtn():
    field.delete(0, END)


#Calculating Buttons
def sumBtn():
    global firstNum
    global calculator

    firstNumber = field.get()
    firstNum = float(firstNumber)
    calculator = "+"
    field.delete(0, END)

def minusBtn():
    global firstNum
    global calculator

    firstNumber = field.get()
    firstNum = float(firstNumber)
    calculator = "-"
    field.delete(0, END)


def multiBtn():
    global firstNum
    global calculator

    firstNumber = field.get()
    firstNum = float(firstNumber)
    calculator = "*"
    field.delete(0, END)


def divBtn():
    global firstNum
    global calculator

    firstNumber = field.get()
    firstNum = float(firstNumber)
    calculator = "/"
    field.delete(0, END)

def sqrBtn():
    global firstNum
    global calculator

    firstNumber = field.get()
    firstNum = float(firstNumber)
    calculator = "sqr"
    field.delete(0, END)

def pwrBtn():
    global firstNum
    global calculator

    firstNumber = field.get()
    firstNum = float(firstNumber)
    calculator = "pwr"
    field.delete(0,END)

def rootBtn():
    global firstNum
    global calculator

    firstNummber = field.get()
    firstNum = float(firstNummber)
    calculator = "root"
    field.delete(0, END)

def eqlBtn():
    secondNum = field.get()
    field.delete(0,END)

    if calculator == "+":
        field.insert(0, firstNum + float(secondNum))
    elif calculator == "-":
        field.insert(0, firstNum - float(secondNum))
    elif calculator == "*":
        field.insert(0, firstNum * float(secondNum))
    elif calculator == "/":
        field.insert(0, firstNum / float(secondNum))
    elif calculator == "sqr":
        field.insert(0, firstNum * firstNum)
    elif calculator == "pwr":
        pwr = 1
        for i in range(int(secondNum)):
            pwr = pwr * firstNum
        field.insert(0, pwr)
    elif calculator == "root":
        field.insert(0, math.sqrt(firstNum))



#Define Btns

button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: btn_onClick(0))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: btn_onClick(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: btn_onClick(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: btn_onClick(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: btn_onClick(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: btn_onClick(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: btn_onClick(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: btn_onClick(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: btn_onClick(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: btn_onClick(9))
button_point = Button(root, text=".", padx=40, pady=20, command=lambda: btn_onClick("."))

button_plus = Button(root, text="+", padx=40, pady=20, command=lambda: sumBtn())
button_minus = Button(root, text="-", padx=40, pady=20, command=lambda: minusBtn())
button_multi = Button(root, text="*", padx=40, pady=20, command=lambda: multiBtn())
button_div = Button(root, text="/", padx=40, pady=20, command=lambda: divBtn())
button_sqr = Button(root, text="sqr", padx=40, pady=20, command=lambda: sqrBtn())
button_pwr = Button(root, text="pwr", padx=40, pady=20, command=lambda: pwrBtn())
button_root = Button(root, text="root", padx=40, pady=20, command=lambda: rootBtn())

button_clr = Button(root, text="C", padx=40, pady=20, command=lambda: clrBtn())
button_eql = Button(root, text="=", padx=40, pady=20, command=lambda: eqlBtn())

#Btns on screen
button_0.grid(row=5, column=0)
button_point.grid(row=5, column=1)
button_eql.grid(row=5, column=2)
button_plus.grid(row=5, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_minus.grid(row=4, column=3)


button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_multi.grid(row=3, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_div.grid(row=2, column=3)

button_sqr.grid(row=1, column=0)
button_pwr.grid(row=1, column=1)
button_root.grid(row=1, column=2)
button_clr.grid(row=1, column=3)

root.mainloop()

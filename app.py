#! /usr/bin/python

import tkinter as gui

calc = gui.Tk()
calc.geometry("200x250")
calc.title("Calculator")

operation = 0
var_1 = 0
var_2 = 0

def assign_value(key):
        global var_1
        global var_2
        if operation == 0:
                var_1 = key
                Output.delete('1.0')
                Output.insert('1.0', var_1)
        else:
                var_2 = key
                Output.delete('3.0')
                Output.insert('3.0', var_2)

def B1CallBack():
        assign_value(1)

def B2CallBack():
        assign_value(2)

def B3CallBack():
        assign_value(3)

def B4CallBack():
        assign_value(4)

def B5CallBack():
        assign_value(5)

def B6CallBack():
        assign_value(6)

def B7CallBack():
        assign_value(7)

def B8CallBack():
        assign_value(8)

def B9CallBack():
        assign_value(9)

def B0CallBack():
        assign_value(0)

def BSCallBack():
        global operation
        operation = 1
        Output.delete('2.0')
        Output.insert('2.0', "+")

def BDCallBack():
        global operation
        operation = 2
        Output.delete('2.0')
        Output.insert('2.0', "-")

def BPCallBack():
        global operation
        operation = 3
        Output.delete('2.0')
        Output.insert('2.0', "x")

def BQCallBack():
        global operation
        operation = 4
        Output.delete('2.0')
        Output.insert('2.0', "/")

def BECallBack():
        global var_1
        global var_2
        global operation
        Output.delete('4.0')
        Output.insert('4.0', "=")
        Output.delete('5.0')
        if operation == 1:
                Output.insert('4.0', (var_1+var_2))
        elif operation == 2:
                Output.insert('4.0', (var_1-var_2))
        elif operation == 3:
                Output.insert('4.0', (var_1*var_2))
        elif operation == 4:
                Output.insert('4.0', (var_1/var_2))
        else:
                print ("Invalid operation")
        operation = 0
        var_1 = 0
        var_2 = 0

def CLRCallBack():
        Output.delete('1.0','5.0')

button1 = gui.Button (calc, text = "1", command = B1CallBack)
button2 = gui.Button (calc, text = "2", command = B2CallBack)
button3 = gui.Button (calc, text = "3", command = B3CallBack)
button4 = gui.Button (calc, text = "4", command = B4CallBack)
button5 = gui.Button (calc, text = "5", command = B5CallBack)
button6 = gui.Button (calc, text = "6", command = B6CallBack)
button7 = gui.Button (calc, text = "7", command = B7CallBack)
button8 = gui.Button (calc, text = "8", command = B8CallBack)
button9 = gui.Button (calc, text = "9", command = B9CallBack)
button0 = gui.Button (calc, text = "0", command = B0CallBack)
buttonS = gui.Button (calc, text = "+", command = BSCallBack)
buttonD = gui.Button (calc, text = "-", command = BDCallBack)
buttonP = gui.Button (calc, text = "x", command = BPCallBack)
buttonQ = gui.Button (calc, text = "/", command = BQCallBack)
buttonE = gui.Button (calc, text = "=", command = BECallBack)
buttonC = gui.Button (calc, text = "C", command = CLRCallBack)
Output = gui.Text(calc)

button1.place(height = 50, width = 50, x = 0  , y = 50)
button2.place(height = 50, width = 50, x = 50 , y = 50)
button3.place(height = 50, width = 50, x = 100, y = 50)
button4.place(height = 50, width = 50, x = 0  , y = 100)
button5.place(height = 50, width = 50, x = 50 , y = 100)
button6.place(height = 50, width = 50, x = 100, y = 100)
button7.place(height = 50, width = 50, x = 0  , y = 150)
button8.place(height = 50, width = 50, x = 50 , y = 150)
button9.place(height = 50, width = 50, x = 100, y = 150)
button0.place(height = 50, width = 50, x = 0  , y = 200)
buttonS.place(height = 50, width = 50, x = 150 , y = 50)
buttonD.place(height = 50, width = 50, x = 150, y = 100)
buttonP.place(height = 50, width = 50, x = 150, y = 150)
buttonQ.place(height = 50, width = 50, x = 50, y = 200)
buttonE.place(height = 50, width = 50, x = 100, y = 200)
buttonC.place(height = 50, width = 50, x = 150, y = 200)
Output.place(height = 50, width = 200, x = 0, y = 0)

calc.mainloop()

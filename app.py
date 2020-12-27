#! /usr/bin/python

import tkinter as gui

calc = gui.Tk()

def B1CallBack():
	print ("Button 1 Pressed")

def B2CallBack():
	print ("Button 2 Pressed")

def B3CallBack():
	print ("Button 3 Pressed")

def B4CallBack():
	print ("Button 4 Pressed")

def B5CallBack():
        print ("Button 5 Pressed")

def B6CallBack():
        print ("Button 6 Pressed")

def B7CallBack():
        print ("Button 7 Pressed")

def B8CallBack():
        print ("Button 8 Pressed")

def B9CallBack():
        print ("Button 9 Pressed")

def B0CallBack():
        print ("Button 0 Pressed")

def BSCallBack():
        print ("Button Add Pressed")

def BDCallBack():
        print ("Button Subtraction Pressed")

def BPCallBack():
        print ("Button Multiplication Pressed")

def BQCallBack():
        print ("Button Division Pressed")

def BECallBack():
        print ("Button Equal Pressed")

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

button1.place(height = 50, width = 50, x = 0  , y = 0)
button2.place(height = 50, width = 50, x = 50 , y = 0)
button3.place(height = 50, width = 50, x = 100, y = 0)
button4.place(height = 50, width = 50, x = 0  , y = 50)
button5.place(height = 50, width = 50, x = 50 , y = 50)
button6.place(height = 50, width = 50, x = 100, y = 50)
button7.place(height = 50, width = 50, x = 0  , y = 100)
button8.place(height = 50, width = 50, x = 50 , y = 100)
button9.place(height = 50, width = 50, x = 100, y = 100)
button0.place(height = 50, width = 50, x = 0  , y = 150)
buttonS.place(height = 50, width = 50, x = 150 , y = 0)
buttonD.place(height = 50, width = 50, x = 150, y = 50)
buttonP.place(height = 50, width = 50, x = 150, y = 100)
buttonQ.place(height = 50, width = 50, x = 50, y = 150)
buttonE.place(height = 50, width = 50, x = 100, y = 150)

calc.mainloop()

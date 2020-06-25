import serial
import time
from tkinter import *
from tkinter import messagebox


ser = serial.Serial('COM7', 9600)   # check your com port
time.sleep(2)

def on():
    ser.write(b'1')

def off():
    ser.write(b'0')

def exit():
    ser.close() # close serial port
    quit()

window = Tk()
window.title("ARDUINO CONTROL BY PYTHON GUI")
window.geometry('640x480')
lbl = Label(window, text="ARDUINO PYTHON GUI",fg='black',font=(None, 9))
lbl.place(relx=0.30, rely=0.10, height=50, width=250)
bo = Button(window, text="LED ON", width=10 ,bg='red' ,command=on)
bo.place(relx=0.34, rely=0.30, height=40, width=200)
cb = Button(window, text="LED OFF", width=10, bg='green' ,command=off)
cb.place(relx=0.34, rely=0.40, height=40, width=200)
ext = Button(window, text="Exit", width=10, bg='white', command=exit)
ext.place(relx=0.34, rely=0.50, height=40, width=200)
window.mainloop()

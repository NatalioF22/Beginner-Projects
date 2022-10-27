
from tkinter import*
from  time import *
from turtle import color

def update():
    time_string = strftime("%I : %M : %S %p")
    time_label.config(text=time_string)
    time_label.after(1000,update)

    day_string = strftime("%A")
    day_label.config(text=day_string)

   

window = Tk()
window.title("Digital Clock")
window.geometry("400x200")
window.configure(bg="#00FFFF")

day_label = Label(window,width = 10,height=5,bg = "#00FFFF")
day_label.pack()

time_label = Label(window,width = 10,height=2,bg = "#00FFFF")
time_label.pack()



update()

window.mainloop()

from tkinter import *
app = Tk()
app.title("Leal Year")
app.geometry("500x200")
app.minsize(500,200)
app.maxsize(500,200)
welcome = Label(app, text = "Welcome to Leap It\nEnter a year and we'll tell you if it's Leap year or not.")
welcome.pack()

year = Entry(app)
year.pack()

def Leap():
    #Check error missing
    info.delete('0',END)
    value =  int(year.get())
    if (value %4) ==0:
        if value %100==0:
            if value%400==0:
                info.insert(INSERT,'Leap')
            else:
                info.insert(INSERT,'Not Leap')
        else:
            info.insert(INSERT,'Leap')
    else:
        info.insert(INSERT,'Not Leap') 
    
Check = Button(app, text = "Check", command = Leap)
Check.pack()

info = Entry(app)
info.pack()



app.mainloop()

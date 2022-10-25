from tkinter import *
from datetime import date

app = Tk()
app.title("Age Calculator")
app.geometry('370x300')
app.minsize(370,300)
app.maxsize(370,300)


welcome = Label(app, text = "Calculate your age",pady = 20,padx = 20)
welcome.grid(row=0, column = 1,columnspan=2)

year = Label(app,text = "Birth Year",padx = 20)
year.grid(row = 1, column = 0)

month = Label(app,text = "Birth Month")
month.grid(row = 2, column = 0)

day = Label(app,text = "Birth Day")
day.grid(row = 3, column = 0)


#Entries
year_entry = Entry(app, )
year_entry.grid(row = 1, column = 1)

month_entry = Entry(app)
month_entry.grid(row = 2, column = 1)

day_entry = Entry(app)
day_entry.grid(row = 3, column = 1)

show = Text(app,width = 4, height=1, font = ('arial',40))
show.grid(row = 5, column = 1, columnspan=2)

#Buttom
def calculate():
    show.delete('1.0',END)
    today = date.today()
    year = int(year_entry.get())
    month = int(month_entry.get())
    day = int(day_entry.get())
    AGE  = today.year - year -((today.month,month)<( today.day,day))
    show.insert(INSERT,AGE)

#definbe a function to check the error missing
    

Calculate = Button(app,text = "Calculate", command = calculate)
Calculate.grid(row = 4, column = 1, columnspan=2)
app.mainloop()

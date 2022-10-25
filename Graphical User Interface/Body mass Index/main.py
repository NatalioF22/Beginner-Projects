from tkinter import *
app = Tk()
app.geometry("700x500")
welcome = Label(app,text = "Welcome to body mass index Calculator",pady = 20, padx = 20)
welcome.grid(row = 0, column = 0, columnspan = 2)

w = Label(app, text = "Weitgh in Kilograms",pady = 20, padx = 20)
w.grid(row = 1, column = 0)

h = Label(app, text = "Height in meters",pady = 20, padx = 20)
h.grid(row = 2, column = 0)

#ENTRIES
w_entry = Entry(app)
w_entry.grid(row = 1, column = 2)

h_entry = Entry(app)
h_entry.grid(row = 2, column = 2)
def calculate_bmi():
    show_result.delete(0,END)
    heitgh = float(h_entry.get())
    weight = float(w_entry.get())
    bmi = weight/heitgh**2
    if bmi < 18.5:
        show_result.insert(INSERT,"UNDERWEIGHT")
    elif bmi >18.5 and bmi < 24.9:
        show_result.insert(INSERT,"IDEAL SHAPE")
    else:
        show_result.insert(INSERT,"OVERWEIGHT")


calculate_button = Button(app, text = "Calculate BMI", command = calculate_bmi)
calculate_button.grid(row = 3, column = 1, columnspan = 2)

show_result = Entry(app,width = 30)
show_result.grid(row = 4, column =1, columnspan = 2)



app.mainloop()

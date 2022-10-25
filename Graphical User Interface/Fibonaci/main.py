from tkinter import *
from tkinter import messagebox
app = Tk()
app.geometry('1100x500')
welcome = Label(app, text = 'Welome to Find out Fibonacci', padx = 30,pady = 30)
welcome.grid(row = 0, column = 1)

check_lbl = Label(app, text = "Enter the numbers of terms you would like to display: ", padx = 10,pady = 5)
check_lbl.grid(row = 1, column =0)

check_entry = Entry(app,width = 20)
check_entry.grid(row = 1, column = 1)


num_frame = Frame(app)
num_frame.grid(row = 1, column = 2)

num_lst = Listbox(num_frame,
        font = 'arial',
        width = 30,
        height = 15,
        bg = 'SystemButtonFace',
        bd = 1,
        fg = '#464646',
        highlightthickness = 1,
        selectbackground='green',
        activestyle='none')
num_lst.grid(row =1, column = 2,padx = 5,pady = 5)

my_scrollbar = Scrollbar(num_frame)
my_scrollbar.grid( row = 1, column = 3,sticky=N+S+E)

num_lst.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command = num_lst.yview)
def fibonacci():
    num_lst.delete('0', END)
    nterms = int(check_entry.get())
    a,b = 0,1
    count = 0

    if nterms<=0:
        messagebox.showinfo("Find Out Fibonacci","Please Enter a number greater than 0")
    elif nterms ==1:
        num_lst.insert(INSERT,b)
    else:
        while count<nterms:
            num_lst.insert(END,a)
            print(a)
            nth = a +b
            a = b
            b = nth
            count+=1

check_button = Button(app, text = "Check", command = fibonacci, width = 20, padx = 0)
check_button.grid(row = 2, column = 0,columnspan = 2, rowspan = 2)
app.mainloop()


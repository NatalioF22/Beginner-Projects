from cmath import exp
import pickle
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from tkinter import filedialog

#Create a tkinter window
app = Tk()
app.title("To Do Application")
icon = PhotoImage(file = "C:/Users/natal/Desktop/Projects/To Do List/tasks.png")
app.iconphoto(False,icon)
app.geometry("800x500")
app.maxsize(1000,500)
app.minsize(1000,500)

#Define our font
my_font = Font(
    family="ADMIRATION PAINS",
    size = 30,
    weight="bold")

#create frame
my_frame = Frame(app,width=1000,bg="black")

my_frame.pack(pady=10,padx=10)
#create listbox
my_list = Listbox(my_frame,
font = my_font,
width=25,
height=5,
bg = "SystemButtonFace",
bd = 0,
fg="#464646",
highlightthickness=0,
selectbackground="#a6a6a6",
activestyle="none")
my_list.pack(side=LEFT,fil = BOTH,pady=20)


#Create a scroll bar
my_scrollbar = Scrollbar(my_frame,background="#000000")
my_scrollbar.pack(side=RIGHT,fill=BOTH)
#Add scroll bar into the mylist
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#Entry box
my_entry  = Entry(app,font=("Helvetica",24))
my_entry.pack(pady=20)

button_frame = Frame(app)
button_frame.pack(pady=20)


def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir=("C:/Users/natal/Desktop/Projects"),title="Save File",
        filetypes=(("Dat Files","*dat"),("All Files","*")))
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f"{file_name}.dat"
            #delete crossed items before saving
            count = 0
            while count<my_list.size():
                if my_list.itemcget(count,"fg") == "#dedede":
                    my_list.delete(my_list.index(count))
                else:
                    count+=1
            #grab everything from the list
            stuff = my_list.get(0,END)
            #open the file
            output_file = open(file_name,'wb')#write to binary
            #add stuff to the file
            pickle.dump(stuff,output_file)

def open_list():
    file_name = filedialog.askopenfilename(
        initialdir=("C:/Users/natal/Desktop/Projects"),title="Open File",
        filetypes=(("Dat Files","*dat"),("All Files","*")))
    if file_name:
        #delete currently oepn list
        my_list.delete(0,END)
        #open the file
        input_file = open(file_name,'rb') # read binary

        #load the date from the file
        stuff = pickle.load(input_file)

        #outputstuff to the screen
        for item in stuff:
            my_list.insert(END,item)

def delete_list():
    my_list.delete(0,END)



def delete_item():
    my_list.delete(ANCHOR)
def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0,END)
def cross_item():
    try:
    #Cross off item
        my_list.itemconfig(
            my_list.curselection(),
            fg="#dedede")
            #Get rid of selection bar
        my_list.select_clear(0,END)
    except TclError:
        messagebox.showerror("Empty Selection","Must select an item in order to cross them")
def uncross_item():
    try:
        #Cross off item
        my_list.itemconfig(
            my_list.curselection(),
            fg="#464646")
            #Get rid of selection bar
        my_list.select_clear(0,END)
    except TclError:
        messagebox.showerror("Empty Selection","Must select a cross item in order to uncross them")

def delete_crossed():
    count = 0
    while count<my_list.size():
        if my_list.itemcget(count,"fg") == "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count+=1
my_menu=Menu(app)
app.config(menu=my_menu)

file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label = "File", menu = file_menu)

file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=delete_list)


delete_button = Button(button_frame, text="Delete Item", command=delete_item,bg="#FF0000")
add_button = Button(button_frame, text="Add Item", command=add_item,bg="#39FF14")
cross_button = Button(button_frame, text="Cross Item", command=cross_item,bg = "#00FFFF")
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item,bg="#E44D2E")
delete_cross_button = Button(button_frame, text="Delete Crossed Items", command=delete_crossed,bg="#00FFFF")

delete_button.grid(row = 0,column=0,padx = 20)
add_button.grid(row = 0,column=1,padx = 20)
cross_button.grid(row = 0,column=2,padx = 20)
uncross_button.grid(row = 0,column=3,padx = 20)
delete_cross_button.grid(row = 0,column=4,padx = 20)

app.mainloop()

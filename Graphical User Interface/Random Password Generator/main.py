from tkinter import *
import random
import string
app = Tk()
app.title("Password Generator")
welcome = Label(text = 'Welcome to Password Generator')
welcome.pack()
def generate_password():
    Show_pass.delete(0,END)
    characters = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    password = ''.join(random.choice(characters)for i in range(1,13))
    Show_pass.insert(0,password)
generate_Button = Button(app, text = "Generate Password",command = generate_password)
generate_Button.pack()

Show_pass = Entry(app)
Show_pass.pack(padx=10,pady = 10)
app.geometry("500x175")
app.minsize(500,175)
app.maxsize(500,175)
app.mainloop()

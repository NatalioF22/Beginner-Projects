from pytube import YouTube
from tkinter import *
from tkinter import messagebox

app = Tk()
app.title("YouTube Downloader")
app.geometry("1250x700")
app.minsize(1250,700)
app.maxsize(1250,700)
title = Label(app, text = "YouTube Downloader")
title.grid(row = 0, column = 1, columnspan = 3)

description_lbl = Label(app, text = "Please enter the url below and choose the quality of de video you would like to download! ")
description_lbl.grid(row = 1, column = 1, columnspan = 3)

url = Entry(app, width = 40)
url.grid(row = 2, column = 1, columnspan = 3, padx = 10, pady = 10)

def vid_search():
    video_title.delete(0, END)
    views_entry.delete(0,END)

    vid_url = url.get()
    video = YouTube(vid_url)

    vid_title = video.title
    vid_views = video.views
    author = video.author
    desciption = video.description

    video_title.insert(INSERT, vid_title)
    views_entry.insert(INSERT, vid_views)
    video_author.insert(INSERT,author)
    disc.insert(INSERT, desciption)

def get_lower_quality():
    vid_url = url.get()
    video = YouTube(vid_url)
    video = video.streams.get_lowest_resolution()
    video.download()
    messagebox.showinfo('Download Info', "Download Completed")



def get_higher_quality():
    vid_url = url.get()
    video = YouTube(vid_url)
    video = video.streams.get_highest_resolution()
    video.download()
    messagebox.showinfo('Download Info',"Download Completed")


search = Button(app, text = "Search", width = 25, command = vid_search)
search.grid(row = 2, column = 3, columnspan = 2, padx = 10, pady = 10)

video_title_lbl = Label(text = "Video Title:")
video_title_lbl.grid(row =3, column =2, columnspan = 2, padx = 10, pady = 10)


video_title = Entry(app, width = 70)
video_title.grid(row = 4, column = 2, columnspan = 2, padx = 10, pady = 10)

video_author_lbl = Label(text = "Author:")
video_author_lbl.grid(row =3, column =1, columnspan = 1, padx = 10, pady = 10)


video_author = Entry(app, width = 20)
video_author.grid(row = 4, column = 1, columnspan = 1, padx = 10, pady = 10)

views_lbl = Label(text = "Views:")
views_lbl.grid(row =5, column =1, columnspan = 1, padx = 10, pady = 10)


views_entry = Entry(app, width = 15)
views_entry.grid(row = 6, column = 1, columnspan = 1, padx = 10, pady = 10)

lower_quality_btn = Button(text = "Download Lower Quality", command = get_lower_quality)
lower_quality_btn.grid(row =5, column =2, columnspan = 2, padx = 10, pady = 10)



higher_quality_btn = Button(text = " Download Higher Quality",command = get_higher_quality)
higher_quality_btn.grid(row =6, column =2, columnspan = 2, padx = 10, pady = 10)

disc_lbl = Label(app, text = "Description")
disc_lbl.grid(row =7, column = 1, columnspan = 3, padx = 10, pady = 10)

disc = Text(app, width = 100, height = 10)
disc.grid(row =8, column = 1, columnspan = 3, padx = 10, pady = 10)
app.configure(bg="#e5e4e2")
app.mainloop()

from pytube import YouTube
from colorama import Fore
from tkinter import *
from tkinter import filedialog
from tkinter import Radiobutton
from tkinter import *
from tkinter.ttk import *
import threading

"""
author: Jason G.
name: Youtube Audio Downloader
TODO: 
1. playlist audio

"""
filename = " "
video = " "
file_size=0
pbnumber = 0


def decide(url,radio, location):
    print(Fore.BLUE + "[INFO] Deciding...")
    if radio==1:
        Download_Audio(url, location)
    elif radio==2:
        download_playlist_audio(url, location)

def Download_Audio(url, location):
    global file_size
    print(Fore.BLUE + "[INFO] Downloading Audio...")
    video_type = YouTube(url,on_progress_callback=progress_function).streams.filter(only_audio=True).first()
    file_size = video_type.filesize
    video_type.download(location)
    print(Fore.BLUE + "[INFO] Done Downloading Audio")

def download_playlist_audio(url,location):
    print("doing stuff...")

def progress_function(stream = None, chunk = None, file_handle = None, remaining = None):
    #Gets the percentage of the file that has been downloaded.
    global pbnumber
    global progress
    pbnumber = int((100*(file_size-remaining))/file_size)
    # progress["value"] = pbnumber
    print("{:00.0f}% downloaded".format(pbnumber))



r = Tk()
r.geometry('500x400')
labelfont = ('times', 20, 'bold')

r.title('Download youtube Video')
title = Label(r, text="Download Audio From YouTube")
title.config(font=labelfont)
title.grid(row=0,column=0, columnspan=2, sticky="n", pady=(5,15))


#asks if you want to download audio or video
v = IntVar()
pbmove = IntVar()
pbmove.set('')



rb1 = Radiobutton(r, text='[Video] Audio', variable=v, value=1)#.grid(row=0, column=0)#.pack()
rb2 = Radiobutton(r, text='[Playlist] Audio', variable=v, value=2)#.grid(row=0, column=0)#.pack()

rb1.grid(row=1, column=0,columnspan=2, sticky="N")
rb2.grid(row=2, column=0,columnspan=2, sticky="N", pady=(0,15))


def browse_button():
    global filename
    filename = filedialog.askdirectory()


def clicked():
    content = link.get()
    radioButtonClicked = v.get()
    decide(content,radioButtonClicked, filename)


label2 = Label(r, text="Location to Download: ").grid(sticky="W",row=3, column=0)
button2 = Button(text="Browse", command=browse_button).grid(row=3, column=1, sticky="w")

label1 = Label(r, text="Youtube Video or playlist link: ").grid(sticky="W",row=4, column=0)


link = Entry(r)
link.grid(sticky="W",row=4, column=1)
#progress = Progressbar(r, orient=HORIZONTAL, length=300, mode='determinate',maximum=100, value=pbnumber).grid(row=6, column=0, columnspan=2,pady=(10, 10))
button = Button(r, text='Download', width=25, command=clicked).grid(row=5,column=0, columnspan=2)





r.mainloop()

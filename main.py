from pytube import YouTube
from colorama import Fore
from tkinter import *
import subprocess

"""
author: Jason G.
Todo:
1. when downloading video, needs to merge downloaded audio and video
2. channel crawling to determine when a channel uploads a new video
    a. sends user a notifcation to download new video automatically
3. work on GUI


"""



#test link: https://www.youtube.com/watch?v=ByEfLtLda64
def decide(url,radio):
    print(Fore.BLUE + "[INFO] Deciding...")
    print("[INFO] You clicked: ", radio)
    if radio==1:
        Download_Audio(url)
        print()
    elif radio==2:
        Download_Video(url)
        print()
    elif radio ==3:
        download_Playlist_video(url)
        print()
    elif radio ==4:
        download_playlist_audio(url)
        print()


def Download_Audio(url):
    print(Fore.BLUE + "[INFO] Downloading Audio...")
    YouTube(url).streams.filter(only_audio=True).first().download()
    print(Fore.BLUE + "[INFO] Done Downloading Audio")

    audio = "audio.mp4"
    try:
        return audio
    except:
        print()

def Download_Video(url):
    yt = YouTube(url)
    # #used to list opetions to download
    # #streams = yt.streams.filter(mime_type="video/mp4",res="1080p").all()
    # streams=yt.streams.filter().order_by('resolution').desc().all()
    #
    # for i in range(len(streams)):
    #     print(streams[i])

    print(Fore.BLUE + "[INFO] Downloading Video...")
    yt.streams.filter(res="1080p",mime_type="video/mp4").order_by('resolution').desc().first().download()
    print(Fore.BLUE + "[INFO] Done Downloading Video")
    audio_name = Download_Audio(url)


def download_Playlist_video(url):
    print("doing stuff...")

def download_playlist_audio(url):
    print("doing stuff...")


r = Tk()
r.geometry('350x200')

r.title('Download youtube Video')

#asks if you want to download audio or video
v = IntVar()
Radiobutton(r, text='[Video] Audio', variable=v, value=1).pack(anchor=W)
Radiobutton(r, text='[Video] Video', variable=v, value=2).pack(anchor=W)
Radiobutton(r, text='[Playlist] Video', variable=v, value=3).pack(anchor=W)
Radiobutton(r, text='[Playlist] Audio', variable=v, value=4).pack(anchor=W)


label1 = Label(r, text="Youtube Video or playlist link:").pack()
#asks for the link of the video
link = Entry(r)
link.pack()
link.focus_set()

def clicked():
    radioButtonClicked = v.get()
    string = link.get()
    print(string,radioButtonClicked)
    decide(string,radioButtonClicked)


button = Button(r, text='Download', width=25, command=clicked)
button.pack()

r.mainloop()

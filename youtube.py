import pywhatkit
from tkinter import *
from PIL import Image, ImageTk


def playsong():
    song=song_text.get()
    pywhatkit.playonyt(song)


root = Tk()
root.title("YouTube Songs")
root.geometry("250x150")
bg = ImageTk.PhotoImage(file="bg.jpg")
bgImage = Label(root, image=bg)
bgImage.place(x=0, y=0, relwidth=1, relheight=1)

song_text=StringVar()
song_entry=Entry(root,textvariable=song_text,bd=3)
song_entry.place(x=70,y=20)
button=Button(root,text="Listen to Song",height=1,width=10,command=playsong)
button.place(x=85,y=50)
root.mainloop()

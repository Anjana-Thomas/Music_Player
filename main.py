from cProfile import label
import tkinter as tk
from tkinter import *
import os
import fnmatch
from pygame import mixer
import pygame

#making canvas

canvas=tk.Tk()
canvas.title("Music Player from Anjana's Playlist")
canvas.geometry("900x900")
canvas.config(bg='black')

rootpath="D:\\MUSIC"
pattern="*.mp3"
root=Tk()
mixer.init()

prev_img=tk.PhotoImage(file="C:\\Users\Dell\Downloads\prev_img.png")
stop_img=tk.PhotoImage(file="C:\\Users\Dell\Downloads\stop_img.png")
play_img=tk.PhotoImage(file="C:\\Users\Dell\Downloads\play_img.png")
pause_img=tk.PhotoImage(file="C:\\Users\Dell\Downloads\pause_img.png")
next_img=tk.PhotoImage(file="C:\\Users\Dell\Downloads\ext_img.png")

#For displaying list of songs create a box 
listbox=tk.Listbox(canvas,fg="cyan",bg="black",width=100,font=('DS-Digital',14))
listbox.pack(padx=15,pady=15)
label=tk.Label(canvas,text='',bg='black',fg='yellow',font=('DS-Digital',18))
label.pack(pady=15)

#For play button
def select():
    label.config(text=listbox.get("anchor"))
    mixer.music.load(rootpath+"\\"+listbox.get("anchor"))
    mixer.music.play()
    
#For stop button
def stop():
    mixer.music.stop()
    listbox.select_clear('active')
    
#For playing next song
def next():
    next_song=listbox.curselection()
    next_song=next_song[0]+1
    next_song_name=listbox.get(next_song)
    label.config(text=next_song_name)
    
    mixer.music.load(rootpath+"\\"+next_song_name)
    mixer.music.play()
    
    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)
    
#For playing previoussong
def prev():
    next_song=listbox.curselection()
    next_song=next_song[0]-1
    next_song_name=listbox.get(next_song)
    label.config(text=next_song_name)
    
    mixer.music.load(rootpath+"\\"+next_song_name)
    mixer.music.play()
    
    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

#For Pause
def pause():
    if pauseButton["text"]=="Pause":
        mixer.music.pause()
        pauseButton["text"]="Play"
    else:
        mixer.music.unpause()
        pauseButton["text"]="Pause"

#BUTTONS
top=tk.Frame(canvas,bg="black")
top.pack(padx=10,pady=5,anchor='center')

prevButton=tk.Button(canvas,text="Prev",image=prev_img,bg='black',borderwidth=0,command=prev)
prevButton.pack(pady=15,in_=top,side='left')

stopButton=tk.Button(canvas,text="Stop",image=stop_img,bg='black',borderwidth=0,command=stop)
stopButton.pack(pady=15,in_=top,side='left')

playButton=tk.Button(canvas,text="Stop",image=play_img,bg='black',borderwidth=0,command=select)
playButton.pack(pady=15,in_=top,side='left')

pauseButton=tk.Button(canvas,text="Stop",image=pause_img,bg='black',borderwidth=0,command=pause)
pauseButton.pack(pady=15,in_=top,side='left')

nextButton=tk.Button(canvas,text="Stop",image=next_img,bg='black',borderwidth=0,command=next)
nextButton.pack(pady=15,in_=top,side='left')

#Insert all music ending with mp3 to the end of box
for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listbox.insert('end',filename)

canvas.mainloop()
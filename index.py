from get import Get
from graph import Graph
from stockget import Get1
from stockgraph import Graph1
from tkinter import *
import tkinter as tk
import tkinter
from PIL import ImageTk, Image
import subprocess

#intro

print("[Intro music playing, please wait 9 seconds!]")
audio_file = "intro.m4a"

return_code = subprocess.call(["afplay", audio_file])

print("Welcome to AssetTracker!")

#user interface made with tkinter, firstly defining background picture and initial window size for instance

root = tk.Tk()
root.title("AssetTracker")

root.geometry("500x500")
image1 = Image.open("test.jpg")

test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(root, image=test)
label1.image = test
label1.place(x=0, y=0)
frame1 = Frame( root, bg = "#88cffa")
frame1.pack(pady = 20)

margin = 0.23

#putting the entries and buttons in place

entry = tk.Entry(root)

entry.pack(pady=(90, 0))

def getcoin():
    Get.main(entry.get())

button_calc = tk.Button(root, text="Get coin", command=getcoin)
button_calc.pack()

entry1 = tk.Entry(root)

entry1.pack(pady=(10, 0))

def graphcoin():
    Graph.main(entry1.get())

button_calc = tk.Button(root, text="Coin graph", command=graphcoin)
button_calc.pack()

margin = 0.23

entry2 = tk.Entry(root)

entry2.pack(pady=(10, 0))

def getstock():
    Get1.main(entry2.get())

button_calc1 = tk.Button(root, text="Get stock (ticker)", command=getstock)
button_calc1.pack()

entry3 = tk.Entry(root)

entry3.pack(pady=(10, 0))

def graphstock():
    Graph1.main(entry3.get())

button_calc = tk.Button(root, text="Stock graph (ticker)", command=graphstock)
button_calc.pack()

root.mainloop()

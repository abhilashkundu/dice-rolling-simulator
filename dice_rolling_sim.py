import random
from tkinter import *

root=Tk()
root.title("AK's Video Downloader")
root.geometry("700x450")

l1=Label(root,text="Welcome to Abhilash's Dice Roll Simulator",font=("times", 200))

def roll():
    number=['\u2680', '\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number)}')
    l1.pack()

def rolltwice():
    number=['\u2680', '\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack()

b1=Button(root,text="TAP TO ROLL ONCE",command=roll)
b2=Button(root,text="TAP TO ROLL TWICE IN A GO",command=rolltwice)
b1.place(x=130,y=0)
b2.place(x=430,y=0)

root.mainloop()


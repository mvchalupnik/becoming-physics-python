import tkinter as tk
from PIL import Image, ImageTk
import variables as v
from Game import *

class FirstScreen(tk.Frame, tk.Tk): ##we add a second parameter so we have master
    def __init__ (self, master=None): ##master of self is default none but we basically always use it
        tk.Frame.__init__(self, master) ##self is automatically passed 
        self.grid()
        self.create_widgets()
        
    def startGame(self):
        self.canvas.destroy()
        self.lab1.destroy()
        self.yesbut.destroy()
        self.nobut.destroy()
        Game(self)
        
    def create_widgets(self):
        self.image = Image.open('100by100test.png') #open the image
        self.pimage = ImageTk.PhotoImage(self.image) #do some bullshit stuff that  may or may not be necessary
        self.canvas = tk.Canvas(self, width=v.imgwidth + 100, height=v.imgheight + 100) #make a canvas
        self.canvas.create_image(v.imgheight,v.imgwidth,image=self.pimage) #make the canvas have the image
        self.canvas.grid(row=0, column=1) #place the canvas
        self.lab1 = tk.Label(self, text = v.introtext)
        
        ##Universal widget methods -- tkinter guide
        ## ctrl+f quit
        ##Events: responding to stimuli
        self.yesbut = tk.Button(self, text='Yes', command=self.startGame)
        self.nobut = tk.Button(self, text='No',
            command=self.quit)
            
        self.lab1.grid(row=1, column=1)
        self.yesbut.grid(row=3, column=0)
        self.nobut.grid(row=3, column=3)
        
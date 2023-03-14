import tkinter as tk
from PIL import Image, ImageTk
from constants import IMG_HEIGHT, IMG_WIDTH
from game_text import INTRO_TEXT
from Game import *

"""
FirstScreen.py
"""

class FirstScreen(tk.Frame, tk.Tk):
    """ FirstScreen is the first screen that is displayed in the Becoming Physics game.
    """

    def __init__ (self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_first_screen()
        
    def start_game(self):
        """ Destroys the FirstScreen canvas and associated objects and instantiates the
        Game class
        """
        self.canvas.destroy()
        self.lab1.destroy()
        self.yesbut.destroy()
        self.nobut.destroy()

        # Start the game
        Game(self)
        
    def create_first_screen(self):
        """ Creates the first screen, and associated objects.
        """

        # Open the image
        self.image = Image.open('100by100test.png')
        self.pimage = ImageTk.PhotoImage(self.image)

        # Make a canvas
        self.canvas = tk.Canvas(self, width=IMG_WIDTH + 100, height=IMG_HEIGHT + 100)

        # Place the image on the canvas
        self.canvas.create_image(IMG_HEIGHT, IMG_WIDTH, image=self.pimage)

        # Place the canvas
        self.canvas.grid(row=0, column=1)
        self.lab1 = tk.Label(self, text=INTRO_TEXT)
        self.yesbut = tk.Button(self, text='Yes', command=self.start_game) #TODO
        self.nobut = tk.Button(self, text='No', command=self.quit)
            
        self.lab1.grid(row=1, column=1)
        self.yesbut.grid(row=3, column=0)
        self.nobut.grid(row=3, column=3)

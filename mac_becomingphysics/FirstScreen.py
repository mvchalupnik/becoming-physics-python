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
        self.first_label.destroy()
        self.yes_button.destroy()
        self.no_button.destroy()

        # Start the game
        Game(self)
        
    def create_first_screen(self):
        """ Creates the first screen, and associated objects.
        """

        # Open the image
        self.image = Image.open('pics/100by100test.png')
        self.pimage = ImageTk.PhotoImage(self.image)

        # Make a canvas
        self.canvas = tk.Canvas(self, width=IMG_WIDTH + 100, height=IMG_HEIGHT + 100)

        # Place the image on the canvas
        self.canvas.create_image(IMG_HEIGHT, IMG_WIDTH, image=self.pimage)

        # Place the canvas
        self.canvas.grid(row=0, column=1)
        self.first_label = tk.Label(self, text=INTRO_TEXT)
        self.yes_button = tk.Button(self, text='Yes', command=self.start_game)
        self.no_button = tk.Button(self, text='No', command=self.quit)
            
        self.first_label.grid(row=1, column=1)
        self.yes_button.grid(row=3, column=0)
        self.no_button.grid(row=3, column=3)

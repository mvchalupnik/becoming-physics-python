import tkinter as tk
from PIL import Image, ImageTk
import constants as v

class Pclass:
    """ A Pclass is a PhysicsClass.

    :param name: The name of the class
    :param hap: The amount of happiness the class gives you per day attended
    :param kno: The amount of knowledge the class gives you per day attended
    :param day: How many days of the class you have attended
    :param lecs: The lectures associated with the class
    :param final: The final exam associated with the class
    """
    
    def __init__ (self, name, hap, kno, day, lecs, final):
        # Initialize final grade as 0, and update this after finals
        final_grade = 0 #previously finalGrade

        self.name = name
        self.hap = hap #TODO fix up variable names?
        self.kno = kno

        # Start on day 0
        self.day = 0
        self.lectures = lecs
        self.final = final

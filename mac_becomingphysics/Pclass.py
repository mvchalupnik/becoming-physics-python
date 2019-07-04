import tkinter as tk
from PIL import Image, ImageTk
import variables as v

class Pclass:
    finalGrade = 0 ##initialize final grade as 0, change after finals
    
    ##class methods
    def __init__ (self, name, hap, kno, day, lecs, final):
        self.name = name
        self.hap = hap
        self.kno = kno
        self.day = 0 ##start on day 0
        self.lectures = lecs ##initialize as a empty set?
        self.final = final
    
    
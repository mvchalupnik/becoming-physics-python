import tkinter as tk
from PIL import Image, ImageTk
import variables as v
#from Pclass import *

class Question:
    def __init__ (self, qtext, a, b, c, d, correctAnswer ):
        self.qtext = qtext #string
        self.answers = [a, b, c, d] # list of strings
        self.answer = correctAnswer #char
        #self.after = after #string
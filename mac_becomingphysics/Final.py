import tkinter as tk
from PIL import Image, ImageTk
import variables as v
#from Pclass import *

class Final:
    def __init__ (self, pclass, question1, question2, question3 ):
        self.pclass = pclass #string
        self.qs = [question1, question2, question3] #List of Questions
        #self.after = after #string
        
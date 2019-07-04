import variables as v
from LabScenario import *

class Choice:
    ##Tag with big/small 
    ##class methods
    def __init__ (self, text, hap, kno, res, after):
        self.text = text #string
        self.hap = hap #int
        self.kno = kno #int
        self.res = res #int
        self.after = after #string

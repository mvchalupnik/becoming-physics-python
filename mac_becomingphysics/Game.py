import tkinter as tk
from PIL import Image, ImageTk
import constants as v
from Pclasses import *
from Lab import *
from Pclass import *
from LabScenario import *
from Ending import *


triggerEndgame = 1 ##MODIFY THIS -- SET TO 1 FOR REAL GAMEPLAY, 0 FOR DEBUGGING

class Game(tk.Frame):
    ##class variables
    happiness = 100
    knowledge = 0
    research = 0
    characterPortrait = Image.open('100by100test.png')
    day = 0
    myPclasses = [] ##list of pClass (new class)
    myResearch = Lab("none")
    
    ##class methods
    def __init__ (self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        ##initialize dynamic string variables
        self.portrait = tk.LabelFrame(self, text = "Stats") ##added
         
        self.portrait.canvas = tk.Canvas(self.portrait, width=v.smallimgwidth, height=v.smallimgheight) #make a canvas
        self.portrait.haplab = tk.Label(self.portrait, text = "Happiness: "+ str(self.happiness))
        self.portrait.knolab = tk.Label(self.portrait, text = "Knowledge: " + str(self.knowledge))
        self.portrait.reslab = tk.Label(self.portrait, text = "Research: " + str(self.research))
        self.portrait.daylab = tk.Label(self.portrait, text = "Day: " + str(self.day))
        
        self.portrait.classlab = tk.Label(self.portrait, text = "Classes: ")
         
        self.hapstrvar = tk.StringVar()
        self.knostrvar = tk.StringVar()
        self.resstrvar = tk.StringVar()
        self.daystrvar = tk.StringVar()
        #self.classstrvar ##TODO
        #self.researchlabstrlab ##TODO
        
        self.create_widgets()
    
    def showStatChanges(self,h,k,r):
        self.portrait.haplab.config(text= "Happiness: "+ str(self.happiness) + " + " + str(h))
        if h >= 0:
            self.portrait.haplab.config(bg = "green")
        else:
            self.portrait.haplab.config(bg = "red")
            
        self.portrait.knolab.config(text= "Knowledge: "+ str(self.knowledge) + " + " + str(k))
        if k >= 0:
            self.portrait.knolab.config(bg="green")
        else:
            self.portrait.knolab.config(bg="red")
        
        self.portrait.reslab.config(text= "Research: "+ str(self.research) + " + " + str(r))
        if r >=0:
            self.portrait.reslab.config(bg="green")
        else:
            self.portrait.reslab.config(bg="red")
            
        self.portrait.daylab.config(text= "Day: "+ str(self.day) + " + 1")
        #self.endf2.R1.config(bg = "green")
        
        #self.portrait.grid()
    
    
    def updatePortrait(self):    
        ##PORTRAIT
        ######self.portrait = tk.LabelFrame(self, text = "Stats")
        self.portrait.image = Image.open('50by50test.png') #open the image
        self.portrait.pimage = ImageTk.PhotoImage(self.portrait.image) #do some bullshit stuff that  may or may not be necessary
        #self.portrait.canvas = tk.Canvas(self.portrait, width=v.smallimgwidth, height=v.smallimgheight) #make a canvas
        
        self.portrait.canvas.create_image(0,0,image=self.portrait.pimage, anchor= tk.NW) #make the canvas have the image
        self.portrait.canvas.grid(row=0, column=0, sticky=tk.W) #place the canvas
        #self.portrait.haplab = tk.Label(self.portrait, text = "Happiness: "+ str(self.happiness))
        self.portrait.haplab.config(text = "Happiness: " + str(self.happiness))
        self.portrait.haplab.config(bg = "white")
        self.portrait.haplab.grid(row=1, column=0, sticky=tk.W)
        #self.portrait.knolab = tk.Label(self.portrait, text = "Knowledge: " + str(self.knowledge))
        self.portrait.knolab.config(text = "Knowledge: " + str(self.knowledge))
        self.portrait.knolab.config(bg = "white")
        self.portrait.knolab.grid(row=2, column=0, sticky=tk.W)
        #self.portrait.reslab = tk.Label(self.portrait, text = "Research: " + str(self.research))
        self.portrait.reslab.config(text = "Research: " + str(self.research))
        self.portrait.reslab.config(bg = "white")
        self.portrait.reslab.grid(row=3, column = 0, sticky=tk.W)
        #self.portrait.daylab = tk.Label(self.portrait, text = "Day: " + str(self.day))
        self.portrait.daylab.config(text="Day: " + str(self.day))
        self.portrait.daylab.grid(row=4, column=0, sticky=tk.W)
        
        #self.portrait.classlab = tk.Label(self.portrait, text = "Classes: ")
        self.portrait.classlab.grid(row=6, column=0, sticky=tk.W)
        for i, item in enumerate(self.myPclasses):
            self.portrait.class2lab = tk.Label(self.portrait, text = self.myPclasses[i].name)
            self.portrait.class2lab.grid(row=7+i, column=0)
        self.portrait.researchlab = tk.Label(self.portrait, text = "Lab : " + self.myResearch.name)
        self.portrait.researchlab.grid(row=5, column=0, sticky=tk.W)
        
        self.portrait.grid(row=0,column=0)
        
    def create_widgets(self):
    ##PORTRAIT
        self.updatePortrait()

        
        ###Actions
        self.mainframe = tk.Frame(self)
        
        self.mainframe.laba = tk.Label(self.mainframe, text = "Welcome to University School!\n Here you can take the first steps to becoming a physics. \nWhat would you like to do today?")
        
        ##If no classes, join a class. Or else go to class
        if len(self.myPclasses) == 0: 
            self.mainframe.registerbut = tk.Button(self.mainframe, text = "Register for Classes", command = self.registerClasses)
            self.mainframe.registerbut.grid(row=2, column = 0)
        else:
            self.mainframe.gotoclassbut = tk.Button(self.mainframe, text = "Go to Class", command = self.goToClass)
            self.mainframe.gotoclassbut.grid(row=2, column = 0)
            
        ## if no lab, join a lab, or else go to lab
        if self.myResearch.name == "none":
            self.mainframe.joinbut = tk.Button(self.mainframe, text = "Join a Lab", command = self.joinLab)
            self.mainframe.joinbut.grid(row=3, column=0)
        else:
            self.mainframe.gotolabbut = tk.Button(self.mainframe, text = "Go to Lab", command = self.goToLab) 
            self.mainframe.gotolabbut.grid(row = 3, column = 0)
            
            
        self.mainframe.laba.grid(row=1, column=0)
        self.mainframe.grid(row=1, column=0)

    def checkBoundaries(self):
        ##Do stuff to check for endgame
        ###BOUNDARY CHECKING!!! Can't be greater than 100 or less than 0
        ##ALSO check if you are at day 10!! If so, take finals!!!!
        ###Also TODO!!! Change self portrait according to stats!!!!
        ###Non-end game conditions
        
        ###Can't have any stats greater than 100
        if self.happiness > 100 :
            self.happiness = 100
        if self.knowledge > 100 :
            self.knowledge = 100
        if self.research > 100 :
            self.research = 100
        
        ##Can't have (non-happiness) stats less than 0
        if self.knowledge < 0:
            self.knowledge = 0
        if self.research < 0:
            self.research = 0
        
        self.updatePortrait() ##is this the right place for this???
        ###End-game conditions
        
    def checkForEndgame(self):
        ###Happiness reaches 0
        if self.happiness <= 0 and triggerEndgame:
            return 1
        
        ###You reach day 10
        if self.day >= v.daysInQuarter and triggerEndgame:
            return 2
        return 0
        
    def addClass(self, checkvarlist):
        self.fr.grid_remove()
        for index, item in enumerate(checkvarlist):
            if item.get() == 1 and classlist[index].name == "Fake Physics":
                #self.fr.grid()
                #print("debugginging")
                classlist[index].name = "Controversial Physics"
                self.foo = tk.Frame(self)
                self.foo.lab = tk.Message(self.foo, text="Fake Physics has been renamed Controversial Physics in order to be more culturally sensitive. (Please select your classes again)" )
                self.foo.but = tk.Button(self.foo, text="Ok then", command = self.ughfunction)
                self.foo.lab.grid(row=0, column=0)
                self.foo.but.grid(row=1, column=0)
                self.foo.grid(row=0, column=1)
                return
        for index, item in enumerate(checkvarlist):
            if item.get() == 1:
                #print("debugging!")
                #print(classlist[index])
                self.myPclasses.append(classlist[index])
        
        self.create_widgets()
    
    def registerClasses(self): 
        ##Can only do this once, at the beginning of the game
        
        self.mainframe.grid_remove()
        
        self.fr = tk.Frame(self)
        
        self.fr.labb = tk.Message(self.fr, text = v.registertext)
        self.fr.labb.grid(row=1, column=0)
        
        ##loop 
        ##maybe I'll make it so if you hover over the button it displays 
        ##info about the class
        ##and classes you can't register for yet are greyed out
        self.fr.CheckVar = []
        ##checkboxes??!!!
        for index, item in enumerate(classlist):
            self.fr.CheckVar.append(tk.IntVar())
            self.fr.C1 = tk.Checkbutton(self.fr, text = item.name, variable = self.fr.CheckVar[index], onvalue = 1, offvalue = 0, height = 2)
            self.fr.C1.grid()
        
        tk.Button(self.fr, text="Done", command = lambda item=item:self.addClass(self.fr.CheckVar)).grid(row=2 + len(classlist), column=0)
        

        self.fr.grid(row=0, column=1)
    
    #def sel(): ##This is the function that is called
    #    selection = "You selected the option " + str(var.get())
    #    label.config(text = selection)   
    def ughfunction(self):
        self.foo.grid_remove()
        self.registerClasses()
        
    def guhfunction(self):
        self.frr.grid_remove()
        self.create_widgets()
    
    def addlab(self, i):
        
        if lablist[i].name == "Medium-Sized Stuff" :
            self.frr = tk.Frame(self)
            self.fr.grid_remove()
            tk.Message(self.frr, text="Lol we already know everything there is to know about Medium-sized stuff. Try another lab!").grid(column=0, row=0)
            tk.Button(self.frr, text="Try Again", command = self.guhfunction).grid(column=0)
            self.frr.grid(column=1, row=0)
            #self.fr.grid_remove()
        else: 
            self.fr.grid_remove()
            self.myResearch = lablist[i]
            self.create_widgets()
        
        #
        
    def joinLab(self): 
        #
        self.mainframe.grid_remove()
        
        self.fr = tk.Frame(self)
        
        self.fr.labc = tk.Label(self.fr, text = v.jointext)
        self.fr.labc.grid(row=1, column=0)
        
        var = tk.IntVar()
        for index, item in enumerate(lablist):
            #self.fr.RadioVar.append(tk.IntVar())
            self.fr.R1 = tk.Radiobutton(self.fr, text = item.name,  variable = var, value = index )
            self.fr.R1.grid()
        
        self.fr.labjoinbut = tk.Button(self.fr, text="Done", command = lambda :self.addlab(var.get()))
        self.fr.labjoinbut.grid(row=2 + len(lablist), column=0)
        
        self.fr.grid(row=0, column=1)
    
    def afterClass(self, i):
        self.frr.grid_remove()
        
        ##If i = -1, this means we ran out of classes
        if i >= 0 :
            ###BOUNDARY CHECKING!!! Can't be greater than 100 or less than 0
            ##
            self.happiness = self.happiness + self.myPclasses[i].hap
            self.knowledge = self.knowledge + self.myPclasses[i].kno
            self.day = self.day + 1
            self.myPclasses[i].day = self.myPclasses[i].day + 1
            ##update stuff!!
        
        self.checkBoundaries()
        status = self.checkForEndgame()
        if status != 0 : 
            self.endGame(status)
        else:
            self.create_widgets()
    
    def inClass(self, i):
        #
        #print("In class!!" + str(i))
        self.fr.grid_remove()
        
        self.frr = tk.Frame(self)
        
        ##Make sure you haven't reached the end of all lectures
        if self.myPclasses[i].day < len(self.myPclasses[i].lectures) :
          
            self.frr.cp1 = Image.open(self.myPclasses[i].lectures[self.myPclasses[i].day][1])
            
            self.showStatChanges(self.myPclasses[i].hap, self.myPclasses[i].kno, 0) ##RECENT
            
            ##Resize image but keep old aspect ratio
            newwidth = int((self.frr.cp1.width * 500)/self.frr.cp1.height)  
            self.frr.cp1 = self.frr.cp1.resize((newwidth, 500), Image.ANTIALIAS)
            self.frr.cp2 = ImageTk.PhotoImage(self.frr.cp1) #do some bullshit
            
            
            self.frr.cv = tk.Canvas(self.frr, width=newwidth, height=500)
            self.frr.cv.create_image(0,0,anchor=tk.NW,image=self.frr.cp2)##LOL First numbers are coordinates NOT SIZES!!! OMG 
            #The default is anchor=tk.CENTER, meaning that the image is centered on the (x,y) position. See Section 5.5, “Anchors” (p. 12) for the possible values of this option. For example, if you specify anchor=tk.S, the image will be positioned so that point (x, y) is located at the center of the bottom (south) edge of the image.
            self.frr.cv.grid()
            
            
            self.frr.msg = tk.Message(self.frr, text=self.myPclasses[i].lectures[self.myPclasses[i].day][0], aspect=1000)###may need to adjust aspect more
            self.frr.msg.grid()
            
            
        else : ###TODO FIX BETTER
            tk.Label(self.frr, text = "Wheee you ran out of classes").grid(row=0, column=0)
            i = -1
            
        tk.Button(self.frr, text="Done", command = lambda:self.afterClass(i)).grid(row=2, column=0)
        
        self.frr.grid(row=0, column=1, sticky=tk.NW)
    
    def goToClass(self):
        self.mainframe.grid_remove()
        
        self.fr = tk.Frame(self)
        
        var = tk.IntVar()
        for index, item in enumerate(self.myPclasses):
            self.fr.R1 = tk.Radiobutton(self.fr, text = item.name,  variable = var, value = index)
            self.fr.R1.grid(row=1 + index)
        
        tk.Button(self.fr, text="Go To This Class", command = lambda item=item:self.inClass(var.get())).grid(row=2 + len(self.myPclasses), column=0)
        
        self.fr.labd = tk.Label(self.fr, text = v.chooseclasstext)
        self.fr.labd.grid(row=0, column=0)
        
        self.fr.grid(row=0, column=1)
    
    def afterLab(self, choice):
        self.frr.grid_remove()
        
        self.happiness = self.happiness + choice.hap
        self.knowledge = self.knowledge + choice.kno
        self.research = self.research + choice.res
        self.day = self.day + 1
        ##update stuff!!
        
        ##check Boundaries!
        self.checkBoundaries()
        status = self.checkForEndgame() #1 for happiness low, 2 for reached day 10
        if status != 0 : 
            ##print("status is" + str(status))
            self.endGame(status)
        else:
            self.create_widgets()
    
    def atLab(self, choice):
        self.fr.grid_remove()
        
        self.frr = tk.Frame(self)
   
        self.showStatChanges(choice.hap, choice.kno, choice.res)
   		
        tk.Message(self.frr, text=choice.after, aspect=1000).grid(row=0, column=0)
        tk.Button(self.frr, text="Done", command = lambda:self.afterLab(choice)).grid(row=2, column=0)

        self.frr.grid(row=0, column=1)
    
    def goToLab(self):
        self.mainframe.grid_remove()
        
        ls = self.myResearch.generateLabScenario(self.myResearch.name)
        if ls.scenario == "error" : ##Ran out of scenarios!
            self.fr = tk.Frame(self)
            self.fr.grid(column=1)
            tk.Message(self.fr, text = "You go to lab, but there is no work for you there. Maybe you should go to class instead?").grid()
            tk.Button(self.fr, text = "Ok", command = self.create_widgets).grid()
        else : 
            self.fr = tk.Frame(self)
            self.fr.labe = tk.Label(self.fr, text= "You went to Lab:")
            self.fr.labf = tk.Message(self.fr, text = ls.scenario)
            self.fr.butfr = tk.Frame(self.fr)
            self.fr.butfr.choice1 = tk.Button(self.fr.butfr, text = ls.choice1.text, command = lambda: self.atLab(ls.choice1))
            self.fr.butfr.choice2 = tk.Button(self.fr.butfr, text = ls.choice2.text, command = lambda: self.atLab(ls.choice2))
        
            self.fr.labe.grid(row=0, column = 0)
            self.fr.labf.grid(row=1, column=0)
            self.fr.butfr.grid(row=2, column=0)
        
            self.fr.butfr.choice1.grid(row=0, column = 0)
            self.fr.butfr.choice2.grid(row=0, column=1)
        
            self.fr.grid(row=0, column=1)
    
    def gradeFinal(self, vars,cnum):
        ###Display the correct answers
        self.endf.grid_remove()
        pclass = self.myPclasses[cnum]
        
        self.endf2 = tk.Frame(self)

        
        self.endf2.pclab = tk.Label(self.endf2, text=pclass.name + " Final Answers", font ="Arial 16")
        self.endf2.pclab.grid()
 
        for i in range(0,3) :
            self.endf2.q = tk.Message(self.endf2, text = str(i+1) + ". " + pclass.final.questions[i].qtext, aspect = 1200, font = "Courier 14")
            self.endf2.q.grid(sticky = tk.W)
            ##var.append(tk.IntVar())
            for j in range(0, 4):
                #self.fr.RadioVar.append(tk.IntVar())
                ##if it's the correct answer,make color 
                
                ##if it's the wrong answer, make color red
                ##Leave the selected thing as is
                
                oldvar = tk.IntVar()
                oldvar = vars[i]
                
                self.endf2.R1 = tk.Radiobutton(self.endf2, text = pclass.final.questions[i].answers[j], font = "Courier 12", justify = tk.LEFT, variable = oldvar, value = j)
                
                ##vars[i] = 0,1,2, or 3 depending on what was selected
                #if vars[i].get() == j:
                    #print("i is " + str(i))
                    #print("j is " + str(j))
                    #print("vars[i] is " + str(vars[i].get()))
                    ##select the previously selected answer
                    #self.endf2.R1.select()
 

                if self.myPclasses[cnum].final.questions[i].answer == j:
                    ##green
                    #print("green control")
                    self.endf2.R1.config(bg = "green")
                else:
                    ##red
                    #print("red control")
                    self.endf2.R1.config(bg = "red")
              
               ##DISABLE button
                #####self.endf2.R1.config(state = tk.DISABLED)
                
                self.endf2.R1.grid(sticky = tk.W)
                
        self.endf2.gradebut = tk.Button(self.endf2, text="Continue", command = lambda :self.doFinal(cnum))
        self.endf2.gradebut.grid()
        #self.endf.qlabel = tk.Label(self.endf, text=)
        self.endf2.grid(column=1, row=0)
        
        ##Make and store grade
        score = 0
        for i in range(0,3) :
            if self.myPclasses[cnum].final.questions[i].answer == vars[i].get() :
                #print("for debugging purposes")
                score = score + 1
        self.myPclasses[cnum].finalGrade = score ###Maybe change... implement curve? #TODO
        cnum = cnum + 1
        ##self.doFinal(cnum) ##error handling at beginning of doFinal
    
    def determineEnding(self): 
        if(self.happiness >= 90 and self.knowledge >= 90 and self.research >= 90):
            return equationEnding
        elif(self.knowledge >= 80 and self.happiness >= 50 and self.research >= 50):
            return gradSchoolEnding
        elif(self.research >= 80) :
            return scopeEnding
        else:
            return badStudentEnding ##TODO
    
    def endScreen(self, end):
        #if hasattr(self, self.endf):
        #    self.endf.grid_remove()

        self.endd = tk.Frame(self)
        self.endd.endlab = tk.Label(self.endd, text=end.title, font=" 14")
        
        self.endd.pic = Image.open(end.pic)
        ##Resize image but keep old aspect ratio
        newwidth = int((self.endd.pic.width * 500)/self.endd.pic.height)  
        self.endd.pic = self.endd.pic.resize((newwidth, 500), Image.ANTIALIAS)
        self.endd.pic = ImageTk.PhotoImage(self.endd.pic) #do some bullshit
            
        self.endd.endcanv = tk.Canvas(self.endd, width = newwidth, height=500)
        self.endd.endcanv.create_image(0,0, anchor=tk.NW, image=self.endd.pic)
        
        self.endd.endmsg = tk.Message(self.endd, text = end.text, aspect = 1200)
        ##self.endd.endbut = tk.Button(self.endd, text = "Play Again?", command = main)
        ##clean up old frames first????? TODO
        self.endd.quitbut = tk.Button(self.endd, text = "Quit", command = self.quit)
        
        self.endd.endlab.grid()
        self.endd.endcanv.grid()
        self.endd.endmsg.grid()
        self.endd.quitbut.grid()
        self.endd.grid(column=1, row = 0) ##NOT SURE ON
        ##CHECK THIS
    
    def letterGrade(self, tg):
        tg = float(tg) ##should be unnecessary bc already do this
        tg = tg * 4./3. ##convert to 4.0
        if 3.7 < tg <= 4.0 :
            return "A"
        if 3.3 < tg <= 3.7 :
            return "A-"
        if 3.0 < tg <= 3.3 :
            return "B+"
        if 2.7 < tg <= 3.0 :
            return "B"
        if 2.3 < tg <= 2.7 :
            return "B-"
        if 2.0 < tg <= 2.3 :
            return "C+"
        if 1.7 < tg <= 2.0 :
            return "C"
        if 1.3 < tg <= 1.7 :
            return "C-"
        if 1 < tg <= 1.3 :
            return "D+"
        if 0.5 < tg <= 1 :
            return "D"
        else:
            return "F"
            
    def gpaHappiness(self, tg) :
        if 3.5 < tg <= 4.0 :
            self.happiness = self.happiness + 100
        elif 3.0 < tg <= 3.5 :
            self.happiness = self.happiness + 30
        elif 2.5 < tg <= 3.0 :
            self.happiness = self.happiness + 10
        elif 2.0 < tg <= 2.5 :
            self.happiness = self.happiness - 10
        elif 1.0 < tg <= 2.0 :
            self.happiness = self.happiness - 30
        else:
            self.happiness = self.happiness - 60
        self.checkBoundaries()
    
    def muhh(self, end) :
        self.endf.grid_remove()
        self.endScreen(end)
        
    def doFinal(self, cnum): ##This function is ugly and should make it better when/if time TODO
        self.endff.grid_remove()
        if cnum > 0 :
            self.endf2.grid_remove() ##THERE MUST BE A BETTER WAY :( 
        self.endf = tk.Frame(self)

        if cnum == len(self.myPclasses) :
            ##we have reached the end of finals.
            

            ###Determine gpa and display lettergrade of each class
            gpa = 0
            for index, item in enumerate(self.myPclasses) :
                gpa = gpa + item.finalGrade
                tk.Label(self.endf, text = item.name + ": " + self.letterGrade(item.finalGrade)).grid(row=1 + index)
                
            gpa = float(gpa)
            gpa = gpa / len(self.myPclasses)
            gpa = gpa * 4./3.
            
            ##Determine letterGrades (and label and grid)
            
            ##Determine happiness change based on gpa
            self.gpaHappiness(gpa)
            self.checkBoundaries()
            
            end = self.determineEnding()
            tk.Label(self.endf, text = "Your Grades Are in...", font="Ariel 14").grid(column=0 ,row=0)
            self.endf.gradelabel = tk.Label(self.endf, text = "Your GPA is: " + str(gpa) + "\nThis has affected your happiness")
            self.endf.buttt = tk.Button(self.endf, text = "Continue", command = lambda: self.muhh(end))
            self.endf.gradelabel.grid()
            self.endf.buttt.grid()
            self.endf.grid(column=2, row=0) 
            return
        
        ##Do a final for class number cnum
        pclass = self.myPclasses[cnum]

        self.endf.pclab = tk.Label(self.endf, text=pclass.name + " Final", font ="Arial 14")
        self.endf.pclab.grid()
        var = []
        for i in range(0,3) :
            self.endf.q = tk.Message(self.endf, text = str(i+1) + ". " + pclass.final.questions[i].qtext, aspect = 1200, font = "Courier 14")
            self.endf.q.grid(sticky = tk.W)
            var.append(tk.IntVar())
            for j in range(0, 4):
                self.endf.R1 = tk.Radiobutton(self.endf, text = pclass.final.questions[i].answers[j], font = "Courier 12", justify = tk.LEFT, variable = var[i], value = j )
                self.endf.R1.grid(sticky = tk.W)
        self.endf.gradebut = tk.Button(self.endf, text="Hand in", command = lambda :self.gradeFinal(var,cnum))
        self.endf.gradebut.grid()
        self.endf.grid(column=1, row=0)
    
    def endGame(self, status):
        self.checkBoundaries() ##changed from updatePortrait
        ##print("now status is " + str(status))
        if status == 1 :
            #print("control is here")
            self.endff = tk.Frame(self)
            self.endff.flab = tk.Message(self.endff, text="You are too sad to continue!! :( :( ")
            self.endff.fbut = tk.Button(self.endff, text="What happens now?", command = lambda : self.endScreen(sadEnding))
            self.endff.grid(column=1, row=0)
            self.endff.flab.grid()
            self.endff.fbut.grid()
            ##happiness ending ##endf screen, continue button
        
        elif status == 2 and len(self.myPclasses) != 0:
            self.endff = tk.Frame(self)
            self.endff.flab = tk.Message(self.endff, text="You have reached Finals week!! Remember, if you aren't miserable, you aren't studying hard enough!!")
            self.endff.fbut = tk.Button(self.endff, text="To Finals!", command = lambda :self.doFinal(0))
            self.endff.grid(column=1, row=0)
            self.endff.flab.grid()
            self.endff.fbut.grid()
            ##FINALS
            
        else:
            self.endScreen(noClassesEnding)
            ##here's where endgame will end up if you enroll in no classes 
        
import tkinter as tk
from PIL import Image, ImageTk
from constants import IMG_HEIGHT, IMG_WIDTH, SMALL_IMG_HEIGHT, SMALL_IMG_WIDTH, DAYS_IN_QUARTER
from game_text import REGISTER_TEXT, JOIN_TEXT, CHOOSE_CLASS_TEXT, ALL_CLASSES, ALL_LABS,\
                      SAD_ENDING, NO_CLASSES_ENDING, BAD_STUDENT_ENDING, SCOPE_ENDING,\
                      GRAD_SCHOOL_ENDING, EQUATION_ENDING

from Lab import *
from PhysicsClass import *
from LabScenario import *
from Ending import *
import pdb

# Set to False for "endless mode" (no endgame triggered) or debugging; True for normal play
debug_endgame_off = True

class Game(tk.Frame):
    """ TODO description

    """

    # Initial game stats
    happiness = 100
    knowledge = 0
    research = 0
    day = 0

    enrolled_physics_classes = []
    joined_research_lab = Lab("none", LabType.NONE)

    def __init__ (self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.portrait = tk.LabelFrame(self, text = "Stats")
         
        # Make a tkinter canvas
        self.portrait.canvas = tk.Canvas(self.portrait, width= SMALL_IMG_WIDTH, height= SMALL_IMG_HEIGHT)
        self.portrait.haplab = tk.Label(self.portrait, text = "Happiness: "+ str(self.happiness))
        self.portrait.knolab = tk.Label(self.portrait, text = "Knowledge: " + str(self.knowledge))
        self.portrait.reslab = tk.Label(self.portrait, text = "Research: " + str(self.research))
        self.portrait.daylab = tk.Label(self.portrait, text = "Day: " + str(self.day))
        self.portrait.classlab = tk.Label(self.portrait, text = "Classes: ")
         
        self.hapstrvar = tk.StringVar()
        self.knostrvar = tk.StringVar()
        self.resstrvar = tk.StringVar()
        self.daystrvar = tk.StringVar()
        
        self.show_main_choices()
    
    def show_stat_changes(self,h,k,r):
        """
        """
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
    
    def update_portrait(self):    
        """ Update portrait and displayed stats. 
        """
        self.portrait.image = Image.open('50by50test.png') #open the image
        self.portrait.pimage = ImageTk.PhotoImage(self.portrait.image)
        
        # Place the image on the canvas
        self.portrait.canvas.create_image(0,0,image=self.portrait.pimage, anchor= tk.NW)
        # Place the canvas
        self.portrait.canvas.grid(row=0, column=0, sticky=tk.W)

        # Create player Happiness label
        self.portrait.haplab.config(text = "Happiness: " + str(self.happiness))
        self.portrait.haplab.config(bg = "white")
        self.portrait.haplab.grid(row=1, column=0, sticky=tk.W)

        # Create player Knowledge label
        self.portrait.knolab.config(text = "Knowledge: " + str(self.knowledge))
        self.portrait.knolab.config(bg = "white")
        self.portrait.knolab.grid(row=2, column=0, sticky=tk.W)

        # Create player Research label
        self.portrait.reslab.config(text = "Research: " + str(self.research))
        self.portrait.reslab.config(bg = "white")
        self.portrait.reslab.grid(row=3, column = 0, sticky=tk.W)

        # Create a day label
        self.portrait.daylab.config(text="Day: " + str(self.day))
        self.portrait.daylab.grid(row=4, column=0, sticky=tk.W)
        
        # Place Classes label
        self.portrait.classlab.grid(row=6, column=0, sticky=tk.W)
        for i, item in enumerate(self.enrolled_physics_classes):
            self.portrait.class2lab = tk.Label(self.portrait, text = self.enrolled_physics_classes[i].name)
            self.portrait.class2lab.grid(row=7+i, column=0)
        self.portrait.researchlab = tk.Label(self.portrait, text = "Lab : " + self.joined_research_lab.name)
        self.portrait.researchlab.grid(row=5, column=0, sticky=tk.W)
        
        self.portrait.grid(row=0,column=0)
        
    def show_main_choices(self):
        """
        """
        self.update_portrait()

        ###Actions
        self.mainframe = tk.Frame(self)
        
        self.mainframe.laba = tk.Label(self.mainframe,
                                       text = "Welcome to University School!\n Here you can take the "\
                                       "first steps to becoming a physics. \nWhat would you like to do today?")
        
        if len(self.enrolled_physics_classes) == 0:
            # If player has not joined any classes, display join classes option
            self.mainframe.registerbut = tk.Button(self.mainframe,
                                                   text = "Register for Classes",
                                                   command = self.register_classes)
            self.mainframe.registerbut.grid(row=2, column = 0)
        else:
            # If player has joined classes, display option to go to class
            self.mainframe.gotoclassbut = tk.Button(self.mainframe, text = "Go to Class", command = self.go_to_class)
            self.mainframe.gotoclassbut.grid(row=2, column = 0)
            
        ## if no lab, join a lab, or else go to lab
        if self.joined_research_lab.name == "none":
            self.mainframe.joinbut = tk.Button(self.mainframe, text = "Join a Lab", command = self.join_lab)
            self.mainframe.joinbut.grid(row=3, column=0)
        else:
            self.mainframe.gotolabbut = tk.Button(self.mainframe, text = "Go to Lab", command = self.go_to_lab) 
            self.mainframe.gotolabbut.grid(row = 3, column = 0)

        self.mainframe.laba.grid(row=1, column=0)
        self.mainframe.grid(row=1, column=0)

    def check_boundaries(self):
        """ After player stats are changed, validate the changes


        """
        
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
        
        self.update_portrait()
        ###End-game conditions
        
    def check_for_endgame(self):
        # End game is triggered if player happiness reaches 0 or less
        if self.happiness <= 0 and debug_endgame_off:
            return 1
        
        # End game is triggered if player reaches day 10
        if self.day >= DAYS_IN_QUARTER and debug_endgame_off:
            return 2
        return 0
        
    def add_class(self, checkvarlist):
        """ Add a class
        """
        self.fr.grid_remove()
        for index, item in enumerate(checkvarlist):
            if item.get() == 1 and ALL_CLASSES[index].name == "Fake Physics":

                ALL_CLASSES[index].name = "Controversial Physics"
                self.foo = tk.Frame(self)
                controversial_message = "Fake Physics has been renamed Controversial Physics in "\
                                        "order to be more culturally sensitive. (Please select your classes again)" 
                self.foo.lab = tk.Message(self.foo, text=controversial_message)
                self.foo.but = tk.Button(self.foo, text="Ok then", command = self.recall_register_classes)
                self.foo.lab.grid(row=0, column=0)
                self.foo.but.grid(row=1, column=0)
                self.foo.grid(row=0, column=1)
                return
        for index, item in enumerate(checkvarlist):
            if item.get() == 1:
                self.enrolled_physics_classes.append(ALL_CLASSES[index])
        
        self.show_main_choices()
    
    def register_classes(self): 
        ##Can only do this once, at the beginning of the game
        
        self.mainframe.grid_remove()
        
        self.fr = tk.Frame(self)
        
        self.fr.labb = tk.Message(self.fr, text = REGISTER_TEXT)
        self.fr.labb.grid(row=1, column=0)
        
        self.fr.CheckVar = []

        # Create check boxes for registering for classes
        for index, item in enumerate(ALL_CLASSES):
            self.fr.CheckVar.append(tk.IntVar())
            self.fr.C1 = tk.Checkbutton(self.fr, 
                                        text=item.name,
                                        variable=self.fr.CheckVar[index],
                                        onvalue = 1,
                                        offvalue = 0,
                                        height = 2)
            self.fr.C1.grid()
        
        tk.Button(self.fr,
                  text="Done",
                  command = lambda item=item:self.add_class(self.fr.CheckVar)).grid(row=2 + len(ALL_CLASSES), column=0)

        self.fr.grid(row=0, column=1)
    
    def recall_register_classes(self):
        self.foo.grid_remove()
        self.register_classes()
        
    def recall_show_main_choices(self):
        self.frr.grid_remove()
        self.show_main_choices()
    
    def add_lab(self, i):
        """
        """
        if ALL_LABS[i].name == "Medium-Sized Stuff" :
            self.frr = tk.Frame(self)
            self.fr.grid_remove()
            medium_sized_lab_text = "Lol we already know everything there is to know about "\
                                    "Medium-sized stuff. Try another lab!"
            tk.Message(self.frr, text=medium_sized_lab_text).grid(column=0, row=0)
            tk.Button(self.frr, text="Try Again", command = self.recall_show_main_choices).grid(column=0)
            self.frr.grid(column=1, row=0)

        else: 
            self.fr.grid_remove()
            self.joined_research_lab = ALL_LABS[i]
            self.show_main_choices()
        
    def join_lab(self): 
        """ Join a lab
        """
        self.mainframe.grid_remove()
        
        self.fr = tk.Frame(self)
        
        self.fr.labc = tk.Label(self.fr, text = JOIN_TEXT)
        self.fr.labc.grid(row=1, column=0)
        
        var = tk.IntVar()
        for index, item in enumerate(ALL_LABS):
            self.fr.R1 = tk.Radiobutton(self.fr, text=item.name,  variable=var, value=index )
            self.fr.R1.grid()
        
        self.fr.labjoinbut = tk.Button(self.fr, text="Done", command=lambda :self.add_lab(var.get()))
        self.fr.labjoinbut.grid(row=2 + len(ALL_LABS), column=0)
        
        self.fr.grid(row=0, column=1)
    
    def after_class(self, i):
        """ This function is called after a Class finishes

        TODO WHY i??
        """
        self.frr.grid_remove()
        
        ##If i = -1, this means we ran out of classes
        if i >= 0 :
            # Add happiness and knowledge gained from classes to player stats
            self.happiness = self.happiness + self.enrolled_physics_classes[i].happiness
            self.knowledge = self.knowledge + self.enrolled_physics_classes[i].knowledge

            # Advance the day by 1
            self.day = self.day + 1

            # Advance the physics class index by 1
            self.enrolled_physics_classes[i].day = self.enrolled_physics_classes[i].day + 1
        
        # Validate changes to player stats
        self.check_boundaries()

        # Check for endgame
        status = self.check_for_endgame()
        if status != 0 : 
            self.end_game(status)
        else:
            self.show_main_choices()
    
    def in_class(self, i):
        """ Display this if you are in class
        """
        self.fr.grid_remove()
        
        self.frr = tk.Frame(self)
        
        ##Make sure you haven't reached the end of all lectures
        if self.enrolled_physics_classes[i].day < len(self.enrolled_physics_classes[i].lectures):
          
            self.frr.cp1 = Image.open(self.enrolled_physics_classes[i].lectures[self.enrolled_physics_classes[i].day][1])
            
            self.show_stat_changes(self.enrolled_physics_classes[i].happiness, self.enrolled_physics_classes[i].knowledge, 0)
            
            ##Resize image but keep old aspect ratio
            newwidth = int((self.frr.cp1.width * 500)/self.frr.cp1.height)  
            self.frr.cp1 = self.frr.cp1.resize((newwidth, 500), Image.ANTIALIAS)
            self.frr.cp2 = ImageTk.PhotoImage(self.frr.cp1) #do some bullshit
            
            
            self.frr.cv = tk.Canvas(self.frr, width=newwidth, height=500)
            self.frr.cv.create_image(0,0,anchor=tk.NW,image=self.frr.cp2)
            ##LOL First numbers are coordinates NOT SIZES!!! OMG 
            #The default is anchor=tk.CENTER, meaning that the image is centered on the (x,y) position. 
            self.frr.cv.grid()
            
            lecture_text = self.enrolled_physics_classes[i].lectures[self.enrolled_physics_classes[i].day][0]
            self.frr.msg = tk.Message(self.frr, text=lecture_text, aspect=1000)
            self.frr.msg.grid()

        else :
            # Player has attended all possible lectures for that particular class
            tk.Label(self.frr, text = "Wheee you ran out of lectures").grid(row=0, column=0)
            i = -1
            
        tk.Button(self.frr, text="Done", command = lambda:self.after_class(i)).grid(row=2, column=0)
        
        self.frr.grid(row=0, column=1, sticky=tk.NW)
    
    def go_to_class(self):
        """ go to class
        """
        self.mainframe.grid_remove()
        
        self.fr = tk.Frame(self)
        
        var = tk.IntVar()
        for index, item in enumerate(self.enrolled_physics_classes):
            self.fr.R1 = tk.Radiobutton(self.fr, text = item.name,  variable = var, value = index)
            self.fr.R1.grid(row=1 + index)
        
        tk.Button(self.fr,
                  text="Go To This Class",
                  command = lambda item=item:self.in_class(var.get())).grid(row=2 + len(self.enrolled_physics_classes),
                  column=0)
        
        self.fr.labd = tk.Label(self.fr, text = CHOOSE_CLASS_TEXT)
        self.fr.labd.grid(row=0, column=0)
        
        self.fr.grid(row=0, column=1)
    
    def after_lab(self, choice):
        """ Funtion called after lab scenario
        """

        self.frr.grid_remove()

        # Update player stats        
        self.happiness = self.happiness + choice.happiness
        self.knowledge = self.knowledge + choice.knowledge
        self.research = self.research + choice.research
        self.day = self.day + 1
        
        ##check Boundaries!
        self.check_boundaries()
        status = self.check_for_endgame() #1 for happiness low, 2 for reached day 10
        # (TODO we aren't using the functionality of 2 reached for day 10)
        if status != 0 : 
            self.end_game(status)
        else:
            self.show_main_choices()
    
    def at_lab(self, choice):
        """
        """
        self.fr.grid_remove()
        self.frr = tk.Frame(self)
   
        self.show_stat_changes(choice.happiness, choice.knowledge, choice.research)
   		
        tk.Message(self.frr, text=choice.effect_text, aspect=1000).grid(row=0, column=0)
        tk.Button(self.frr, text="Done", command = lambda:self.after_lab(choice)).grid(row=2, column=0)

        self.frr.grid(row=0, column=1)
    
    def go_to_lab(self):
        """ Go to lab and generate a LabScenario
        """
        self.mainframe.grid_remove()
        
        ls = self.joined_research_lab.generate_lab_scenario()
        if ls.scenario is None: ##Ran out of scenarios!
            self.fr = tk.Frame(self)
            self.fr.grid(column=1)
            tk.Message(self.fr,
                      text = "You go to lab, but there is no work for you there. "\
                             "Maybe you should go to class instead?").grid()
            tk.Button(self.fr, text = "Ok", command = self.show_main_choices).grid()
        else : 
            self.fr = tk.Frame(self)
            self.fr.labe = tk.Label(self.fr, text= "You went to Lab:")
            self.fr.labf = tk.Message(self.fr, text = ls.scenario)
            self.fr.butfr = tk.Frame(self.fr)
            self.fr.butfr.choice1 = tk.Button(self.fr.butfr,
                                              text = ls.choice1.choice_text,
                                              command = lambda: self.at_lab(ls.choice1))
            self.fr.butfr.choice2 = tk.Button(self.fr.butfr,
                                              text = ls.choice2.choice_text,
                                              command = lambda: self.at_lab(ls.choice2))
        
            self.fr.labe.grid(row=0, column = 0)
            self.fr.labf.grid(row=1, column=0)
            self.fr.butfr.grid(row=2, column=0)
        
            self.fr.butfr.choice1.grid(row=0, column = 0)
            self.fr.butfr.choice2.grid(row=0, column=1)
        
            self.fr.grid(row=0, column=1)
    
    def grade_final(self, vars,cnum):
        """ grade the final
        """
        ###Display the correct answers
        self.endf.grid_remove()
        pclass = self.enrolled_physics_classes[cnum]
        
        self.endf2 = tk.Frame(self)
        
        self.endf2.pclab = tk.Label(self.endf2, text=pclass.name + " Final Answers", font ="Arial 16")
        self.endf2.pclab.grid()
 
        for i in range(0,3) :
            finals_text = str(i+1) + ". " + pclass.final.questions[i].qtext
            self.endf2.q = tk.Message(self.endf2,
                                      text = finals_text,
                                      aspect = 1200,
                                      font = "Courier 14")
            self.endf2.q.grid(sticky = tk.W)
            for j in range(0, 4):
                ##if it's the correct answer,make color green
                
                ##if it's the wrong answer, make color red
                ##Leave the selected thing as is
                
                oldvar = tk.IntVar()
                oldvar = vars[i]
                
                radio_button_text = pclass.final.questions[i].answers[j]
                self.endf2.R1 = tk.Radiobutton(self.endf2,
                                               text = radio_button_text,
                                               font = "Courier 12",
                                               justify = tk.LEFT,
                                               variable = oldvar,
                                               value = j)
                
                if self.enrolled_physics_classes[cnum].final.questions[i].answer.value == j:
                    ##green
                    self.endf2.R1.config(bg = "green")
                else:
                    ##red
                    self.endf2.R1.config(bg = "red")
                
                self.endf2.R1.grid(sticky = tk.W)
                
        self.endf2.gradebut = tk.Button(self.endf2, text="Continue", command = lambda :self.do_final(cnum))
        self.endf2.gradebut.grid()
        self.endf2.grid(column=1, row=0)
        
        ##Make and store grade
        score = 0
        for i in range(0,3):
            if self.enrolled_physics_classes[cnum].final.questions[i].answer.value == vars[i].get() :
                score = score + 1
        self.enrolled_physics_classes[cnum].final_grade = score
        cnum = cnum + 1
    
    def determine_ending(self):
        """
        """
        if(self.happiness >= 90 and self.knowledge >= 90 and self.research >= 90):
            return EQUATION_ENDING
        elif(self.knowledge >= 80 and self.happiness >= 50 and self.research >= 50):
            return GRAD_SCHOOL_ENDING
        elif(self.research >= 80) :
            return SCOPE_ENDING
        else:
            return BAD_STUDENT_ENDING
    
    def end_screen(self, end):
        """
        """

        self.endd = tk.Frame(self)
        self.endd.endlab = tk.Label(self.endd, text=end.ending_title, font=" 14")
        
        self.endd.image = Image.open(end.image)

        ##Resize image but keep old aspect ratio
        newwidth = int((self.endd.image.width * 500)/self.endd.image.height)  
        self.endd.image = self.endd.image.resize((newwidth, 500), Image.ANTIALIAS)
        self.endd.image = ImageTk.PhotoImage(self.endd.image) #do some bullshit
            
        self.endd.endcanv = tk.Canvas(self.endd, width = newwidth, height=500)
        self.endd.endcanv.create_image(0,0, anchor=tk.NW, image=self.endd.image)
        
        self.endd.endmsg = tk.Message(self.endd, text = end.ending_text, aspect = 1200)
        self.endd.quitbut = tk.Button(self.endd, text = "Quit", command = self.quit)
        
        self.endd.endlab.grid()
        self.endd.endcanv.grid()
        self.endd.endmsg.grid()
        self.endd.quitbut.grid()
        self.endd.grid(column=1, row = 0)
    
    def get_letter_grade(self, tg):
        # Find GPA and letter grade from the 3 question quiz
        tg = float(tg) * 4./3.

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
            
    def adjust_happiness_from_gpa(self, tg) :
        """ Adjust happiness based on GPA
        """
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

        # Check player stat boundaries
        self.check_boundaries()
    
    def trigger_end_screen(self, end):
        """
        """
        self.endf.grid_remove()
        self.end_screen(end)
        
    def do_final(self, cnum):
        """
        """
        self.endff.grid_remove()
        if cnum > 0 :
            self.endf2.grid_remove() ##THERE MUST BE A BETTER WAY :( TODO
        self.endf = tk.Frame(self)

        if cnum == len(self.enrolled_physics_classes):
            ##we have reached the end of finals.

            ###Determine gpa and display lettergrade of each class
            gpa = 0
            for index, physics_class in enumerate(self.enrolled_physics_classes):
                gpa = gpa + physics_class.final_grade
                letter_grade_text = physics_class.name + ": " + self.get_letter_grade(physics_class.final_grade)
                tk.Label(self.endf, text = letter_grade_text).grid(row=1 + index)

            # Find total GPA
            gpa = float(gpa) / len(self.enrolled_physics_classes)
            gpa = gpa * 4./3.
            
            ##Determine happiness change based on gpa
            self.adjust_happiness_from_gpa(gpa)
            self.check_boundaries()
            
            end = self.determine_ending()
            tk.Label(self.endf, text = "Your Grades Are in...", font="Ariel 14").grid(column=0 ,row=0)

            grade_text = "Your GPA is: " + str(gpa) + "\nThis has affected your happiness"
            self.endf.gradelabel = tk.Label(self.endf, text = grade_text)
            self.endf.buttt = tk.Button(self.endf, text = "Continue", command = lambda: self.trigger_end_screen(end))
            self.endf.gradelabel.grid()
            self.endf.buttt.grid()
            self.endf.grid(column=2, row=0) 
            return
        
        ##Do a final for class number cnum
        pclass = self.enrolled_physics_classes[cnum]

        self.endf.pclab = tk.Label(self.endf, text=pclass.name + " Final", font ="Arial 14")
        self.endf.pclab.grid()
        var = []
        for i in range(0,3) :
            finals_question_text = str(i+1) + ". " + pclass.final.questions[i].qtext
            self.endf.q = tk.Message(self.endf, text = finals_question_text, aspect = 1200, font = "Courier 14")
            self.endf.q.grid(sticky = tk.W)
            var.append(tk.IntVar())
            for j in range(0, 4):
                finals_question_answer = pclass.final.questions[i].answers[j]
                self.endf.R1 = tk.Radiobutton(self.endf,
                                              text = finals_question_answer,
                                              font = "Courier 12",
                                              justify = tk.LEFT,
                                              variable = var[i],
                                              value = j)
                self.endf.R1.grid(sticky = tk.W)
        self.endf.gradebut = tk.Button(self.endf, text="Hand in", command = lambda: self.grade_final(var,cnum))
        self.endf.gradebut.grid()
        self.endf.grid(column=1, row=0)
    
    def end_game(self, status):
        """ 
        """
        self.check_boundaries()
        if status == 1 :
            self.endff = tk.Frame(self)
            self.endff.flab = tk.Message(self.endff, text="You are too sad to continue!! :( :( ")
            self.endff.fbut = tk.Button(self.endff, text="What happens now?", command = lambda: self.end_screen(SAD_ENDING))
            self.endff.grid(column=1, row=0)
            self.endff.flab.grid()
            self.endff.fbut.grid()
            ##happiness ending ##endf screen, continue button
        
        elif status == 2 and len(self.enrolled_physics_classes) != 0:

            # Trigger the start of Finals
            self.endff = tk.Frame(self)
            self.endff.flab = tk.Message(self.endff,
                                         text="You have reached Finals week!! Remember, if you aren't miserable, "\
                                              "you aren't studying hard enough!!")
            self.endff.fbut = tk.Button(self.endff,
                                        text="To Finals!",
                                        command=lambda: self.do_final(0))
            self.endff.grid(column=1, row=0)
            self.endff.flab.grid()
            self.endff.fbut.grid()

        else:
            # If you enroll in no classes, call that no classes ending
            self.end_screen(NO_CLASSES_ENDING)

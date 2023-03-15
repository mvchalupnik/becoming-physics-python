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

class EndGameStatus(Enum):
    CONTINUE = 0
    NEGATIVE_HAPPINESS = 1
    START_FINALS = 2

class Game(tk.Frame):
    """ Displays and runs the primary portion of the Becoming Physics Game

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
        self.portrait.happiness_label = tk.Label(self.portrait, text = "Happiness: "+ str(self.happiness))
        self.portrait.knowledge_label = tk.Label(self.portrait, text = "Knowledge: " + str(self.knowledge))
        self.portrait.research_label = tk.Label(self.portrait, text = "Research: " + str(self.research))
        self.portrait.day_label = tk.Label(self.portrait, text = "Day: " + str(self.day))
        self.portrait.class_label = tk.Label(self.portrait, text = "Classes: ")
         
        self.show_main_choices()
    
    def show_stat_changes(self, delta_h, delta_k, delta_r):
        """ Show changes in players stats after lab or class event.
        Also shows advancement of day by + 1
        
        :param delta_h: The change in happiness
        :param delta_k: The change in knowledge
        :param delta_r: The change in research
        """
        self.portrait.happiness_label.config(text= "Happiness: "+ str(self.happiness) + " + " + str(delta_h))
        if delta_h >= 0:
            self.portrait.happiness_label.config(bg = "green")
        else:
            self.portrait.happiness_label.config(bg = "red")
            
        self.portrait.knowledge_label.config(text= "Knowledge: "+ str(self.knowledge) + " + " + str(delta_k))
        if delta_k >= 0:
            self.portrait.knowledge_label.config(bg="green")
        else:
            self.portrait.knowledge_label.config(bg="red")
        
        self.portrait.research_label.config(text= "Research: "+ str(self.research) + " + " + str(delta_r))
        if delta_r >=0:
            self.portrait.research_label.config(bg="green")
        else:
            self.portrait.research_label.config(bg="red")
            
        self.portrait.day_label.config(text= "Day: "+ str(self.day) + " + 1")    
    
    def update_portrait(self):    
        """ Update portrait and display stats. 
        """
        # Open character portrait image
        self.portrait.image = Image.open('50by50test.png')
        self.portrait.pimage = ImageTk.PhotoImage(self.portrait.image)

        # Place the image on the canvas
        self.portrait.canvas.create_image(0,0,image=self.portrait.pimage, anchor= tk.NW)
        # Place the canvas
        self.portrait.canvas.grid(row=0, column=0, sticky=tk.W)

        # Create player Happiness label
        self.portrait.happiness_label.config(text = "Happiness: " + str(self.happiness))
        self.portrait.happiness_label.config(bg="white")
        self.portrait.happiness_label.grid(row=1, column=0, sticky=tk.W)

        # Create player Knowledge label
        self.portrait.knowledge_label.config(text = "Knowledge: " + str(self.knowledge))
        self.portrait.knowledge_label.config(bg="white")
        self.portrait.knowledge_label.grid(row=2, column=0, sticky=tk.W)

        # Create player Research label
        self.portrait.research_label.config(text = "Research: " + str(self.research))
        self.portrait.research_label.config(bg="white")
        self.portrait.research_label.grid(row=3, column = 0, sticky=tk.W)

        # Create a day label
        self.portrait.day_label.config(text="Day: " + str(self.day))
        self.portrait.day_label.grid(row=4, column=0, sticky=tk.W)
        
        # Place Classes label
        self.portrait.class_label.grid(row=6, column=0, sticky=tk.W)

        # Display all enrolled classes
        for i, enrolled_physics_class in enumerate(self.enrolled_physics_classes):
            self.portrait.enrolled_classes_label = tk.Label(self.portrait, text=enrolled_physics_class.name)
            self.portrait.enrolled_classes_label.grid(row=7+i, column=0)
        # Display research lab
        self.portrait.joined_lab_label = tk.Label(self.portrait, text = "Lab: " + self.joined_research_lab.name)
        self.portrait.joined_lab_label.grid(row=5, column=0, sticky=tk.W)        
        self.portrait.grid(row=0,column=0)
        
    def show_main_choices(self):
        """ Show the main screen, showing the player's main choices of joining lab and classes, or attending
        lab or classes.
        """
        self.update_portrait()

        # Create Frame showing player actions
        self.mainframe = tk.Frame(self)

        self.mainframe.intro_label = tk.Label(self.mainframe,
                                       text = "Welcome to University School!\n Here you can take the "\
                                       "first steps to becoming a physics. \nWhat would you like to do today?")
        
        if len(self.enrolled_physics_classes) == 0:
            # If player has not joined any classes, display Register for classes option
            self.mainframe.register_button = tk.Button(self.mainframe,
                                                   text="Register for Classes",
                                                   command=self.register_classes)
            self.mainframe.register_button.grid(row=2, column=0)
        else:
            # If player has joined classes, display option to go to class
            self.mainframe.go_to_class_button = tk.Button(self.mainframe, text="Go to Class", command=self.go_to_class)
            self.mainframe.go_to_class_button.grid(row=2, column=0)
            
        # If player is not in a lab, display option to join a lab. Otherwise, display option to go to lab.
        if self.joined_research_lab.name == "none":
            self.mainframe.join_lab_button = tk.Button(self.mainframe, text="Join a Lab", command=self.join_lab)
            self.mainframe.join_lab_button.grid(row=3, column=0)
        else:
            self.mainframe.go_to_lab_button = tk.Button(self.mainframe, text="Go to Lab", command=self.go_to_lab) 
            self.mainframe.go_to_lab_button.grid(row=3, column=0)

        self.mainframe.intro_label.grid(row=1, column=0)
        self.mainframe.grid(row=1, column=0)

    def check_boundaries(self):
        """ After player stats are changed, validate the changes. In particular, no stats may exceed 100, so cap there, 
        and no stats may be less than 0, so place a floor there.
        """
        
        # Cap stats at 100
        if self.happiness > 100:
            self.happiness = 100
        if self.knowledge > 100:
            self.knowledge = 100
        if self.research > 100:
            self.research = 100
        
        # Set floor for stats at 0, except for the happiness stat
        if self.knowledge < 0:
            self.knowledge = 0
        if self.research < 0:
            self.research = 0

        self.update_portrait()
        
    def check_for_endgame(self):
        """ Check for endgame conditions
        """
        # End game is triggered if player happiness reaches 0 or less
        if self.happiness <= 0 and debug_endgame_off:
            return EndGameStatus.NEGATIVE_HAPPINESS
        
        # End game is triggered if player reaches day 10
        if self.day >= DAYS_IN_QUARTER and debug_endgame_off:
            return EndGameStatus.START_FINALS

        # Otherwise, continue playing
        return EndGameStatus.CONTINUE
        
    def add_class(self, checkbox_variables):
        """ Add all classes that the player selected the checkbox for to the player's class enrolled classes list

        :param checkbox_variables: This is a list of checkbox variables
        """
        self.event_frame.grid_remove()
        for index, checkbox_variable in enumerate(checkbox_variables):
            if checkbox_variable.get() == 1 and ALL_CLASSES[index].name == "Fake Physics":
                # Rename Fake Physics to Controversial Physics
                ALL_CLASSES[index].name = "Controversial Physics"
                self.cmessage_frame = tk.Frame(self)
                controversial_message = "Fake Physics has been renamed Controversial Physics in "\
                                        "order to be more culturally sensitive. (Please select your classes again)" 
                self.cmessage_frame.label = tk.Message(self.cmessage_frame, text=controversial_message)
                self.cmessage_frame.button = tk.Button(self.cmessage_frame, 
                                                       text="Ok then",
                                                       command=self.recall_register_classes)
                self.cmessage_frame.label.grid(row=0, column=0)
                self.cmessage_frame.button.grid(row=1, column=0)
                self.cmessage_frame.grid(row=0, column=1)
                return
        for index, checkbox_variable in enumerate(checkbox_variables):
            # Enroll in all classes for which the checkbox was selected
            if checkbox_variable.get() == 1:
                self.enrolled_physics_classes.append(ALL_CLASSES[index])
        
        self.show_main_choices()
    
    def register_classes(self):
        """ Register for a class by displaying to the player a list of classes with the options to 
        select a checkbox next to them, and prompting the player to select classes they would like
        to join.
        """
        # Clean up mainframe
        self.mainframe.grid_remove()
        
        # Create frame with text telling player to register for classes
        self.event_frame = tk.Frame(self)
        self.event_frame.labb = tk.Message(self.event_frame, text=REGISTER_TEXT)
        self.event_frame.labb.grid(row=1, column=0)
        
        self.event_frame.checkbox_list = []

        # Create check boxes for registering for classes
        for index, physics_class in enumerate(ALL_CLASSES):
            self.event_frame.checkbox_list.append(tk.IntVar())
            self.event_frame.checkbox = tk.Checkbutton(self.event_frame, 
                                                       text=physics_class.name,
                                                       variable=self.event_frame.checkbox_list[index],
                                                       onvalue=1,
                                                       offvalue=0,
                                                       height=2)
            self.event_frame.checkbox.grid()
        
        tk.Button(self.event_frame,
                  text="Done",
                  command=lambda: self.add_class(self.event_frame.checkbox_list)).grid(row=2 + len(ALL_CLASSES),
                  column=0)

        self.event_frame.grid(row=0, column=1)
    
    def recall_register_classes(self):
        """ Prompt player to register for classes again
        """
        self.cmessage_frame.grid_remove()
        self.register_classes()
        
    def recall_show_main_choices(self):
        """ Bring player back to main choices screen
        """
        self.lab_frame.grid_remove()
        self.show_main_choices()
    
    def add_lab(self, lab_index):
        """ Add the lab that the player chooses

        :param lab_index: The index of the lab which the player chose
        """
        if ALL_LABS[lab_index].name == "Medium-Sized Stuff" :
            self.lab_frame = tk.Frame(self)
            self.event_frame.grid_remove()
            medium_sized_lab_text = "Lol we already know everything there is to know about "\
                                    "Medium-sized stuff. Try another lab!"
            tk.Message(self.lab_frame, text=medium_sized_lab_text).grid(column=0, row=0)
            tk.Button(self.lab_frame, text="Try Again", command = self.recall_show_main_choices).grid(column=0)
            self.lab_frame.grid(column=1, row=0)

        else: 
            self.event_frame.grid_remove()
            self.joined_research_lab = ALL_LABS[lab_index]
            self.show_main_choices()
        
    def join_lab(self): 
        """ Join a lab
        """
        # Clean up frame
        self.mainframe.grid_remove()
        
        # Create event frame
        self.event_frame = tk.Frame(self)
        
        # Create label with directions to join a lab
        self.event_frame.join_lab_label = tk.Label(self.event_frame, text=JOIN_TEXT)
        self.event_frame.join_lab_label.grid(row=1, column=0)
        
        # Create variable to keep track of player lab choice
        var = tk.IntVar()

        # Create RadioButtons for each lab choice and display
        for index, lab in enumerate(ALL_LABS):
            self.event_frame.radio_button = tk.Radiobutton(self.event_frame, text=lab.name,  variable=var, value=index)
            self.event_frame.radio_button.grid()
        
        self.event_frame.join_button = tk.Button(self.event_frame, text="Done", command=lambda: self.add_lab(var.get()))
        self.event_frame.join_button.grid(row=2 + len(ALL_LABS), column=0)
        
        self.event_frame.grid(row=0, column=1)
    
    def after_class(self, class_index):
        """ This function is called after a Class finishes

        :param class_index: The index of enrolled_physics_classes pointing to the desired class
        """
        # Clean up frame
        self.lab_frame.grid_remove()
        
        # If class_index = -1, this means we ran out of classes
        if class_index >= 0 :
            # Add happiness and knowledge gained from classes to player stats
            self.happiness = self.happiness + self.enrolled_physics_classes[class_index].happiness
            self.knowledge = self.knowledge + self.enrolled_physics_classes[class_index].knowledge

            # Advance the day by 1
            self.day = self.day + 1

            # Advance the physics class index by 1
            self.enrolled_physics_classes[class_index].day = self.enrolled_physics_classes[class_index].day + 1
        
        # Validate changes to player stats
        self.check_boundaries()

        # Check for endgame
        status = self.check_for_endgame()
        if status == EndGameStatus.CONTINUE:
            self.show_main_choices()
        else:
            self.end_game(status)
    
    def in_class(self, class_index):
        """ Display class image and text if player attends class lecture.

        :param class_index: The index of enrolled_physics_classes pointing to the desired class
        """
        # Clean up frame
        self.event_frame.grid_remove()
        
        # Create new frame
        self.lab_frame = tk.Frame(self)
        
        selected_class = self.enrolled_physics_classes[class_index]

        # Make sure the player hasn't finished all possible lectures
        if selected_class.day < len(selected_class.lectures):
          
            self.lab_frame.class_image = Image.open(selected_class.lectures[selected_class.day]['image_location'])
            
            self.show_stat_changes(selected_class.happiness, selected_class.knowledge, 0)
            
            # Resize image but keep old aspect ratio
            newwidth = int((self.lab_frame.class_image.width * 500)/self.lab_frame.class_image.height)  
            self.lab_frame.class_image = self.lab_frame.class_image.resize((newwidth, 500), Image.ANTIALIAS)
            self.lab_frame.class_frame = ImageTk.PhotoImage(self.lab_frame.class_image)
            
            self.lab_frame.class_image_frame = tk.Canvas(self.lab_frame, width=newwidth, height=500)

            # First numbers are coordinates, not sizes
            # The default is anchor=tk.CENTER, meaning that the image is centered on the (x,y) position. 
            self.lab_frame.class_image_frame.create_image(0,0,anchor=tk.NW, image=self.lab_frame.class_frame)
            self.lab_frame.class_image_frame.grid()
            
            lecture_text = selected_class.lectures[selected_class.day]['lecture']
            self.lab_frame.msg = tk.Message(self.lab_frame, text=lecture_text, aspect=1000)
            self.lab_frame.msg.grid()

        else :
            # Player has attended all possible lectures for that particular class
            tk.Label(self.lab_frame, text = "Wheee you ran out of lectures").grid(row=0, column=0)
            class_index = -1
        
        # Place "Done" button
        tk.Button(self.lab_frame, text="Done", command = lambda:self.after_class(class_index)).grid(row=2, column=0)
        
        # Place everything in the frame
        self.lab_frame.grid(row=0, column=1, sticky=tk.NW)
    
    def go_to_class(self):
        """ Display classes which player is enrolled in, and radio buttons for them to choose which class to attend
        """
        # Clean up frame
        self.mainframe.grid_remove()

        # Place event frame
        self.event_frame = tk.Frame(self)

        # Create variable for the Radio buttons
        var = tk.IntVar()
        for index, enrolled_physics_class in enumerate(self.enrolled_physics_classes):
            self.event_frame.radio_button = tk.Radiobutton(self.event_frame, 
                                                           text = enrolled_physics_class.name,
                                                           variable = var,
                                                           value = index)
            self.event_frame.radio_button.grid(row=1 + index)

        # Display button to attend class
        tk.Button(self.event_frame,
                  text="Go To This Class",
                  command = lambda:self.in_class(var.get())).grid(row=2 + len(self.enrolled_physics_classes),
                  column=0)
        
        self.event_frame.labd = tk.Label(self.event_frame, text = CHOOSE_CLASS_TEXT)
        self.event_frame.labd.grid(row=0, column=0)
        
        self.event_frame.grid(row=0, column=1)
    
    def after_lab(self, choice):
        """ Funtion called after lab scenario completes
        """
        # Clean up frame
        self.lab_frame.grid_remove()

        # Update player stats        
        self.happiness = self.happiness + choice.happiness
        self.knowledge = self.knowledge + choice.knowledge
        self.research = self.research + choice.research
        self.day = self.day + 1
        
        # check stat boundaries
        self.check_boundaries()

        # Check for endgame conditions
        status = self.check_for_endgame()
        if status != EndGameStatus.CONTINUE: 
            self.end_game(status)
        else:
            self.show_main_choices()
    
    def at_lab(self, choice):
        """ Show stat changes and display lab choice text for lab scenario.

        :param choice: the Choice which the player selected for a given LabScenario
        """
        # Clean up frame
        self.event_frame.grid_remove()

        # Set up lab frame
        self.lab_frame = tk.Frame(self)

        # Show changes in stats
        self.show_stat_changes(choice.happiness, choice.knowledge, choice.research)
   		
        tk.Message(self.lab_frame, text=choice.effect_text, aspect=1000).grid(row=0, column=0)
        tk.Button(self.lab_frame, text="Done", command = lambda:self.after_lab(choice)).grid(row=2, column=0)

        self.lab_frame.grid(row=0, column=1)
    
    def go_to_lab(self):
        """ Go to lab and generate a LabScenario
        """
        self.mainframe.grid_remove()
        
        # Generate a lab scenario 
        lab_scenario = self.joined_research_lab.generate_lab_scenario()
        if lab_scenario.scenario is None: # Ran out of scenarios!
            self.event_frame = tk.Frame(self)
            self.event_frame.grid(column=1)
            tk.Message(self.event_frame,
                      text = "You go to lab, but there is no work for you there. "\
                             "Maybe you should go to class instead?").grid()
            tk.Button(self.event_frame, text="Ok", command=self.show_main_choices).grid()
        else:
            # Display Lab scenario 
            self.event_frame = tk.Frame(self)
            self.event_frame.lab_title = tk.Label(self.event_frame, text="You went to Lab:")
            self.event_frame.lab_scenario_label = tk.Message(self.event_frame, text=lab_scenario.scenario)
            self.event_frame.ls_frame = tk.Frame(self.event_frame)

            # Display the two LabScenario Choices
            self.event_frame.ls_frame.choice1 = tk.Button(self.event_frame.ls_frame,
                                              text = lab_scenario.choice1.choice_text,
                                              command = lambda: self.at_lab(lab_scenario.choice1))
            self.event_frame.ls_frame.choice2 = tk.Button(self.event_frame.ls_frame,
                                              text = lab_scenario.choice2.choice_text,
                                              command = lambda: self.at_lab(lab_scenario.choice2))
        
            self.event_frame.lab_title.grid(row=0, column = 0)
            self.event_frame.lab_scenario_label.grid(row=1, column=0)
            self.event_frame.ls_frame.grid(row=2, column=0)
        
            self.event_frame.ls_frame.choice1.grid(row=0, column = 0)
            self.event_frame.ls_frame.choice2.grid(row=0, column=1)
        
            self.event_frame.grid(row=0, column=1)
    
    def grade_final(self, vars, class_index):
        """ Grade a final for a given PhysicsClass. Update player stats.


        """
        # Clean up frame
        self.endf.grid_remove()

        # get class from list of player's enrolled classes
        physics_class = self.enrolled_physics_classes[class_index]


        self.endf2 = tk.Frame(self)
        
        self.endf2.pclab = tk.Label(self.endf2, text=physics_class.name + " Final Answers", font ="Arial 16")
        self.endf2.pclab.grid()

        # Display the correct answers 
        for i in range(0,3) :
            finals_text = str(i+1) + ". " + physics_class.final.questions[i].qtext
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
                
                radio_button_text = physics_class.final.questions[i].answers[j]
                self.endf2.radio_button = tk.Radiobutton(self.endf2,
                                               text = radio_button_text,
                                               font = "Courier 12",
                                               justify = tk.LEFT,
                                               variable = oldvar,
                                               value = j)
                
                if physics_class.final.questions[i].answer.value == j:
                    ##green
                    self.endf2.radio_button.config(bg = "green")
                else:
                    ##red
                    self.endf2.radio_button.config(bg = "red")
                
                self.endf2.radio_button.grid(sticky = tk.W)
                
        self.endf2.gradebut = tk.Button(self.endf2, text="Continue", command = lambda :self.do_final(class_index))
        self.endf2.gradebut.grid()
        self.endf2.grid(column=1, row=0)
        
        ##Make and store grade
        score = 0
        for i in range(0,3):
            if physics_class.final.questions[i].answer.value == vars[i].get() :
                score = score + 1
        physics_class.final_grade = score
        class_index = class_index + 1
    
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
                self.endf.radio_button = tk.Radiobutton(self.endf,
                                              text = finals_question_answer,
                                              font = "Courier 12",
                                              justify = tk.LEFT,
                                              variable = var[i],
                                              value = j)
                self.endf.radio_button.grid(sticky = tk.W)
        self.endf.gradebut = tk.Button(self.endf, text="Hand in", command = lambda: self.grade_final(var,cnum))
        self.endf.gradebut.grid()
        self.endf.grid(column=1, row=0)
    
    def end_game(self, status):
        """ End the game, with the ending determined by the ending status Enum provided.
        """
        self.check_boundaries()
        if status == EndGameStatus.NEGATIVE_HAPPINESS:
            # If Happiness < 0, trigger SAD_ENDING
            self.endff = tk.Frame(self)
            self.endff.flab = tk.Message(self.endff, text="You are too sad to continue!! :( :( ")
            self.endff.fbut = tk.Button(self.endff, text="What happens now?", command = lambda: self.end_screen(SAD_ENDING))
            self.endff.grid(column=1, row=0)
            self.endff.flab.grid()
            self.endff.fbut.grid()
        
        elif status == EndGameStatus.START_FINALS and len(self.enrolled_physics_classes) != 0:
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

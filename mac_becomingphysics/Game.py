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
        
        # Display text prompting to choose which class to attend
        self.event_frame.labd = tk.Label(self.event_frame, text=CHOOSE_CLASS_TEXT)
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
    
    def grade_final(self, completed_final, class_index):
        """ Grade a final for a given PhysicsClass. Update player stats.
        
        :param completed_final: A list of IntVars() passed containing player's completed answers to the final
        :param class_index: The class index of enrolled_physics_classes pointing to the desired class
        """
        # Clean up frame
        self.finals_frame.grid_remove()

        # get class from list of player's enrolled classes
        physics_class = self.enrolled_physics_classes[class_index]

        # Create a new frame to display grades
        self.grade_frame = tk.Frame(self)
        self.grade_frame.physics_class_label = tk.Label(self.grade_frame,
                                                        text=physics_class.name + " Final Answers",
                                                        font ="Arial 16")
        self.grade_frame.physics_class_label.grid()

        # Display each question
        for question_index in range(0, len(physics_class.final.questions)):
            question = physics_class.final.questions[question_index]

            finals_text = str(question_index+1) + ". " + question.question_text
            self.grade_frame.question_message=tk.Message(self.grade_frame,
                                                         text=finals_text,
                                                         aspect=1200,
                                                         font="Courier 14")
            self.grade_frame.question_message.grid(sticky = tk.W)

            # Loop over each answer and display the correct answer
            for answer_index in range(0, len(question.answers)):                
                player_answer = completed_final[question_index]
                radio_button_text = question.answers[answer_index]

                # Place the radio buttons back and keep the player's answer selected
                self.grade_frame.radio_button = tk.Radiobutton(self.grade_frame,
                                               text = radio_button_text,
                                               font = "Courier 12",
                                               justify = tk.LEFT,
                                               variable = player_answer,
                                               value = answer_index)

                if question.correct_answer.value == answer_index:
                    # Make the correct answer appear in green
                    self.grade_frame.radio_button.config(bg = "green")
                else:
                    # Make all wrong answers appear in red
                    self.grade_frame.radio_button.config(bg = "red")
                
                self.grade_frame.radio_button.grid(sticky = tk.W)
        
        # Create Continue button
        self.grade_frame.grade_button = tk.Button(self.grade_frame,
                                                  text="Continue",
                                                  command = lambda:self.do_final(class_index))
        self.grade_frame.grade_button.grid()
        self.grade_frame.grid(column=1, row=0)
        
        # Calculate and store grade
        score = 0
        for question_index in range(0, len(physics_class.final.questions)):
            if physics_class.final.questions[question_index].correct_answer.value == completed_final[question_index].get():
                score = score + 1
        physics_class.final_grade = score

        # Increase class_index by 1 for when continue button is pushed above
        class_index = class_index + 1
    
    def determine_ending(self):
        """ Determine the earned ending based on player stats
        """

        if(self.happiness >= 90 and self.knowledge >= 90 and self.research >= 90):
            # Best possible ending
            return EQUATION_ENDING
        elif(self.knowledge >= 80 and self.happiness >= 50 and self.research >= 50):
            # Okay ending
            return GRAD_SCHOOL_ENDING
        elif(self.research >= 80):
            # Okay ending
            return SCOPE_ENDING
        else:
            # Bad ending
            return BAD_STUDENT_ENDING
    
    def end_screen(self, ending):
        """ Display ending screen based on ending passed

        :param ending: the Ending to display to the player
        """
        # Create ending screen frame
        self.end_frame = tk.Frame(self)
        self.end_frame.end_label = tk.Label(self.end_frame, text=ending.ending_title, font=" 14")
        
        # Open ending image
        self.end_frame.image = Image.open(ending.image)

        # Resize image but keep old aspect ratio
        new_width = int((self.end_frame.image.width * 500)/self.end_frame.image.height)  
        self.end_frame.image = self.end_frame.image.resize((new_width, 500), Image.ANTIALIAS)
        self.end_frame.image = ImageTk.PhotoImage(self.end_frame.image)
        
        # Create canvas for the image 
        self.end_frame.end_canvas = tk.Canvas(self.end_frame, width = new_width, height=500)
        self.end_frame.end_canvas.create_image(0,0, anchor=tk.NW, image=self.end_frame.image)
        
        # Display ending message
        self.end_frame.end_message = tk.Message(self.end_frame, text = ending.ending_text, aspect = 1200)
        self.end_frame.quit_button = tk.Button(self.end_frame, text = "Quit", command = self.quit)
        
        self.end_frame.end_label.grid()
        self.end_frame.end_canvas.grid()
        self.end_frame.end_message.grid()
        self.end_frame.quit_button.grid()
        self.end_frame.grid(column=1, row = 0)
    
    def get_letter_grade(self, score):
        """ Calculate GPA and letter grade for a given class from the three question quiz

        :score: the player's score on the three question quiz
        """
        score = float(score) * 4./3.

        if 3.7 < score <= 4.0 :
            return "A"
        if 3.3 < score <= 3.7 :
            return "A-"
        if 3.0 < score <= 3.3 :
            return "B+"
        if 2.7 < score <= 3.0 :
            return "B"
        if 2.3 < score <= 2.7 :
            return "B-"
        if 2.0 < score <= 2.3 :
            return "C+"
        if 1.7 < score <= 2.0 :
            return "C"
        if 1.3 < score <= 1.7 :
            return "C-"
        if 1 < score <= 1.3 :
            return "D+"
        if 0.5 < score <= 1 :
            return "D"
        else:
            return "F"
            
    def adjust_happiness_from_gpa(self, gpa) :
        """ Adjust player happiness based on GPA

        :param gpa: The player's GPA
        """
        if 3.5 < gpa <= 4.0 :
            self.happiness = self.happiness + 100
        elif 3.0 < gpa <= 3.5 :
            self.happiness = self.happiness + 30
        elif 2.5 < gpa <= 3.0 :
            self.happiness = self.happiness + 10
        elif 2.0 < gpa <= 2.5 :
            self.happiness = self.happiness - 10
        elif 1.0 < gpa <= 2.0 :
            self.happiness = self.happiness - 30
        else:
            self.happiness = self.happiness - 60

        # Check player stat boundaries
        self.check_boundaries()
    
    def trigger_end_screen(self, end):
        """ Trigger the end screen
        """
        self.finals_frame.grid_remove()
        self.end_screen(end)
        
    def do_final(self, class_index):
        """ Set up a final for a given PhysicsClass for the player to complete

        :param class_index:  The class index of enrolled_physics_classes pointing to the desired class
        """
        # Clean up end frame
        self.check_end_frame.grid_remove()

        # Clean up old frames (recursive call of do_final)
        if class_index > 0 :
            self.grade_frame.grid_remove()

        # Create Finals frame
        self.finals_frame = tk.Frame(self)

        # If class_index is equal to the size of the list of enrolled classes, we have finished finals
        if class_index == len(self.enrolled_physics_classes):
            # Determine gpa and display lettergrade of each class
            gpa = 0
            for index, physics_class in enumerate(self.enrolled_physics_classes):
                gpa = gpa + physics_class.final_grade
                letter_grade_text = physics_class.name + ": " + self.get_letter_grade(physics_class.final_grade)
                tk.Label(self.finals_frame, text = letter_grade_text).grid(row=1 + index)

            # Find total GPA
            gpa = float(gpa) / len(self.enrolled_physics_classes)
            gpa = gpa * 4./3.
            
            # Determine happiness change based on gpa
            self.adjust_happiness_from_gpa(gpa)
            self.check_boundaries()
            
            # Determine player ending based on final stats
            end = self.determine_ending()

            # Display final grades
            tk.Label(self.finals_frame, text = "Your Grades Are in...", font="Ariel 14").grid(column=0 ,row=0)

            grade_text = "Your GPA is: " + str(gpa) + "\nThis has affected your happiness"
            self.finals_frame.gradelabel = tk.Label(self.finals_frame, text = grade_text)
            self.finals_frame.final_grade_button = tk.Button(self.finals_frame, 
                                                             text = "Continue",
                                                             command = lambda: self.trigger_end_screen(end))
            self.finals_frame.gradelabel.grid()
            self.finals_frame.final_grade_button.grid()
            self.finals_frame.grid(column=2, row=0) 
            return
        
        # Otherwise, do a final for class number class_index
        physics_class = self.enrolled_physics_classes[class_index]

        self.finals_frame.physics_class_label = tk.Label(self.finals_frame,
                                                         text=physics_class.name + " Final",
                                                         font ="Arial 14")
        self.finals_frame.physics_class_label.grid()
        
        # Create a list of IntVars and loop through to place these in three RadioButton questions
        player_answers = []
        for question_index in range(0,len(physics_class.final.questions)):
            question = physics_class.final.questions[question_index]
            finals_question_text = str(question_index+1) + ". " + question.question_text
            self.finals_frame.question_message = tk.Message(self.finals_frame, 
                                                            text = finals_question_text,
                                                            aspect = 1200,
                                                            font = "Courier 14")
            self.finals_frame.question_message.grid(sticky = tk.W)
            player_answers.append(tk.IntVar())

            # Loop through each of four possible answers
            for answer_index in range(0, len(question.answers)):
                finals_question_answer = question.answers[answer_index]
                self.finals_frame.radio_button = tk.Radiobutton(self.finals_frame,
                                              text = finals_question_answer,
                                              font = "Courier 12",
                                              justify = tk.LEFT,
                                              variable = player_answers[question_index],
                                              value = answer_index)
                self.finals_frame.radio_button.grid(sticky = tk.W)
        # Create button to hand in exam
        self.finals_frame.grade_button = tk.Button(self.finals_frame,
                                                   text="Hand in",
                                                   command = lambda: self.grade_final(player_answers, class_index))
        self.finals_frame.grade_button.grid()
        self.finals_frame.grid(column=1, row=0)
    
    def end_game(self, status):
        """ Either end the game, or trigger finals, with particular route determined by status Enum provided.

        :param status: An EndGameStatus Enum to determine which route to take
        """
        self.check_boundaries()
        if status == EndGameStatus.NEGATIVE_HAPPINESS:
            # If Happiness < 0, trigger SAD_ENDING
            self.check_end_frame = tk.Frame(self)
            self.check_end_frame.final_label = tk.Message(self.check_end_frame,
                                                          text="You are too sad to continue!! :( :( ")
            self.check_end_frame.final_button = tk.Button(self.check_end_frame,
                                                          text="What happens now?",
                                                          command = lambda: self.end_screen(SAD_ENDING))
            self.check_end_frame.grid(column=1, row=0)
            self.check_end_frame.final_label.grid()
            self.check_end_frame.final_button.grid()
        
        elif status == EndGameStatus.START_FINALS and len(self.enrolled_physics_classes) != 0:
            # Trigger the start of Finals
            self.check_end_frame = tk.Frame(self)
            self.check_end_frame.final_label = tk.Message(self.check_end_frame,
                                         text="You have reached Finals week!! Remember, if you aren't miserable, "\
                                              "you aren't studying hard enough!!")
            self.check_end_frame.final_button = tk.Button(self.check_end_frame,
                                        text="To Finals!",
                                        command=lambda: self.do_final(0))
            self.check_end_frame.grid(column=1, row=0)
            self.check_end_frame.final_label.grid()
            self.check_end_frame.final_button.grid()

        else:
            # If you enroll in no classes, call that no classes ending
            self.end_screen(NO_CLASSES_ENDING)

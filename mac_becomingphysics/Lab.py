import tkinter as tk
from PIL import Image, ImageTk
import constants as v
from LabScenario import *
from Choice import *
import random as random



class Lab:
    ##Tags
    BIG_STUFF = 2
    SMALL_STUFF = 1
    BOTH = 0
    
    ##LabScenario(scenario, Choice(choice, hap, know, res, after), Choice(...), tag)
    errorScenario = LabScenario("Error", Choice("Error", 0,0,0,"Error"),Choice("Error",0,0,0,"Error"), BOTH)
    
    ##(happiness, knowledge, research)
    ##Lab stuff ##TODO lengthen afters
    lss = [LabScenario("You didn't get enough sleep the night before. How to try to stay awake? Should you list all of the Real Housewives of Beverly Hills in your head that you can remember, or list all of the scientists in your head that you can think of?", Choice("Real Housewives", 20,0,20, "Lisa Rinna...Lisa Vanderpump... Eileen Davidson... Kyle Richards... Kim Richards... You stay awake"), Choice("Scientists", -5, 0, 5, "You fall asleep"), BOTH), 
    LabScenario("You didn't get enough sleep the night before. How to try to stay awake? Should you list all of the Real Housewives of Beverly Hills in your head that you can remember, or list all of the scientists in your head that you can think of?", Choice("Real Housewives", -5,0,5, "You fall asleep"), Choice("Scientists", 5, 0, 20, "You stay awake"), BOTH),
    LabScenario("You are cold because you work in the basement of a basement. You have an extra sweater and a winter coat you can but on. But, thinking about it, maybe you should just tough it out?", Choice("Wear extra sweater and coat", 20,10,10, "Good choice. You are much warmer now and are able to think more clearly."), Choice("Tough it out", -60, -10, -20, "You decide to not put on your coat or extra sweater and just tough it out. This was not a good idea. Two hours later, you reach the stage of hypothermia where cold feels warm, and you begin paradoxical undressing. This is not good to do in a place of research. You lose a lot of research points and happiness."), BOTH),
    LabScenario("How hard to work today?", Choice("Really hard!", 10,10,10, "Good!"), Choice("Really really hard!", -20, -20, 0, "You pass out from exhaustion, and accidentally hit a lever releasing low level radiation into the lab."), BOTH),
    LabScenario("How hard to work today?", Choice("Really hard!", 10,5,15, "Good but could be better..."), Choice("Really really hard!", 20, 40, 60, "Amazing!!"), BOTH),
    LabScenario("Something is flashing red. Do you press the button next to it? But wait... this is an important experiment, and it isn't your experiment. You could mess it up. Maybe you should leave it alone?", Choice("Press button", 10,10,20, "The experiment is ruined but you save the lab from burning down! Good call!"), Choice("Do nothing", -40, -10, -20, "The lab burns down! :("), BOTH),
    LabScenario("Something is flashing red. Do you press the button next to it? But wait... this is an important experiment, and it isn't your experiment. You could mess it up. Maybe you should leave it alone?", Choice("Press button", -20,-10,10, "Experiment is ruined! Your PI is super mad at you. :("), Choice("Do nothing", 20, 30, 60, "Experiment is fine, good call!"), BOTH),
    LabScenario("Your entire lab has been trying to discover the Bigs Hoson particle for years. You think you see the signs of one in today's collider data. Do you immediately call the press to tell them?", Choice("Yes!", 50, 10, 40, "You call the press and tell them. It turns out the signs were real, and you did discover the Bigs Hoson! You become a physics celebrity and go on many talk shows."), Choice("No!", -10,0,0, "You decide to wait and talk to your PI first. But in the two minutes you wait, some other lab calls the press and announces they have discovered the Bigs Hoson. :( "), SMALL_STUFF),
    LabScenario("Your entire lab has been trying to discover the Bigs Hoson particle for years. You think you see the signs of one in today's collider data. Do you immediately call the press to tell them?", Choice("Yes!", -50, -10, -10, "You call the press and tell them. It turns out the signs were false. You are laughed at by all of physics."), Choice("No!", 20,0,20, "You decide to wait and talk to your PI first. This is the normal and reasonable thing to do. Turns out the signs were false. Good thing you didn't go to the press. "), SMALL_STUFF),
    LabScenario("You were setting up some optics but you got a mirror dirty. Should you clean it with methanol or acetone?", Choice("Methanol", 0,0,5, "This mirror had extra dirt on it and the methanol isn't strong enough... you should have used acetone."), Choice("Acetone",20,0,15, "Good call! You are able to clean the mirror which had a lot of dirt on it."), SMALL_STUFF),
    LabScenario("You were setting up some optics but you got a mirror dirty. Should you clean it with methanol or acetone?", Choice("Methanol", 20,0,15, "Good call! This mirror didn't have that much dirt on it, so acetone would have been overkill. You successfully clean the mirror."), Choice("Acetone", 0,0,5,"Oh no! After 20 minutes of cleaning, you end up making the mirror dirtier than it initially was."), SMALL_STUFF),
    LabScenario("You are looking through your telescope and you see an asteroid coming to hit Earth. The asteroid is the size of the moon. Earth is doomed. What should you do?", Choice("Tell your PI", -100,-100,-100, "It doesn't really matter, does it? The entire planet is doomed."), Choice("Go into the woods and live as a hermit for your remaining days", -100,-100,-100,"It doesn't really matter, does it? The entire planet is doomed."), BIG_STUFF),
    LabScenario("The distance between the sun and the Earth is 93,000,000 miles. The sun has a diameter of about 860,000 miles. The Earth has a radius of about 8,000 miles. You are 5 feet tall. There are 5280 feet in a mile. You are 0.001 miles tall. You are so tiny. A grain of sand is 0.003 feet which is 0.0000006 miles in diameter.",Choice("Wow that's disturbing",-15,0, 10,"Maybe you shouldn't have decided to study Big Stuff"), Choice("That makes me uncomfortable",-15,0,10, "Maybe you shouldn't have decided to study Big Stuff"), BIG_STUFF)
    ]
    ##one or two more Small stuff scenarios #TODO
    ##another big stuff scenario -- you become an astronaut? and either go insane or are successful. 
    
    
    ###set up siblings
    lss[0].sibling = 1
    lss[1].sibling = 0
    lss[3].sibling = 4
    lss[4].sibling = 3 ## a better way to do this is to just check if titles match... TODO
    lss[5].sibling = 6
    lss[6].sibling = 5
    lss[7].sibling = 8
    lss[8].sibling = 7
    lss[9].sibling = 10
    lss[10].sibling = 9
    
    ##class methods
    def __init__ (self, name):
        self.name = name
        #big
        #small
    
    def generateLabScenario(self, research_name):
        #convert research_name to tag (prolly a prettier way to do this... :()
        tag = 0
        if research_name == "Big Stuff" :
            tag = self.BIG_STUFF
        if research_name == "Small Stuff" :
            tag = self.SMALL_STUFF
        ##print(str(tag)) ##debugging
        

        ##random generating of scenario
        ##Check if the scenario has already been displayed. If so, then don't show it.
        
        trys = 100
        for x in range (0, trys):
            rindex = int(random.random()*len(self.lss)) ##gives me my random index
            if self.lss[rindex].seen == 0 and (self.lss[rindex].tag == self.BOTH or self.lss[rindex].tag == tag): #if you haven't seen it and it's the correct tag,keep the rindex
                ##change seen field to 1
                self.lss[rindex].seen = 1
                
                ##check for a sibling, and if a sibling, set sibling seen to 1 TODO
                sindex = self.lss[rindex].sibling
                if sindex >=0 :
                    self.lss[sindex].seen = 1
                return self.lss[rindex]
        else:
            return self.errorScenario 
        
        

        
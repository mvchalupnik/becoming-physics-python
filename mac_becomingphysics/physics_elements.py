import random as random
from enum import Enum
from typing import Dict, List

""" 
physics_elements.py
Contains classes used in Becoming Physics
"""
class Question:
    """ A Question is a multiple choice question given on a final for a class at the end of the term.

    :param question_text: The text of the question
    :param answers: The four possible multiple choice answers
    :param correct_answer: The correct answer
    """
    def __init__ (self, question_text: str, a: str, b: str, c: str, d: str, correct_answer: str):
        self.question_text = question_text
        self.answers = [a, b, c, d]
        self.correct_answer = correct_answer


class Final:
    """ Final contains a PhysicsClass, and a list of three Questions for the associated Final

    :param physics_class: A string with the name of the class which the Final is associated with
    :param questions: A list of three Questions for the final

    """
    def __init__ (self, physics_class: str, questions: List[Question]):
        self.physics_class = physics_class
        self.questions = questions


class PhysicsClass:
    """ A PhysicsClass is a university Physics class that the player can enroll in in order to
    gain knowledge and affect happiness. At the end of the quarter, the player must take
    a final exam for each PhysicsClass they have enrolled in.

    :param name: The name of the class
    :param happiness: The amount of happiness the class gives you per day attended
    :param knowledge: The amount of knowledge the class gives you per day attended
    :param day: How many days of the class you have attended
    :param lectures: The lectures associated with the class
    :param final: The final exam associated with the class
    """
    
    def __init__ (self, name: str, happiness: int, knowledge: int, day: int, lectures: List[Dict], final: Final):
        # Initialize final grade as 0, and update this after finals
        self.final_grade = 0

        self.name = name
        self.happiness = happiness
        self.knowledge = knowledge

        # Start on day 0 of the class
        self.day = 0
        self.lectures = lectures
        self.final = final


class Choice:
    """ Choice gives the text, happiness, knowledge, and research change associated with a given choice, 
    as well as a string associated with what comes afterwards.

    :param choice_text: String containing text describing the choice
    :param happiness: Int of the amount happiness will change due to this choice
    :param knowledge: Int of the amount knowledge will change due to this choice
    :param research: Int of the amount research will change due to this choice
    :param effect_text: string containing text describing the after effect of the Choice
    """
    def __init__ (self, choice_text: str, happiness: int, knowledge: int, research: int, effect_text: str):
        self.choice_text = choice_text
        self.happiness = happiness
        self.knowledge = knowledge
        self.research = research
        self.effect_text = effect_text


class LabScenario:
    """ LabScenario describes a scenario that happens to you while you are working in lab.
        LabScenarios have associated Choices and the player's choice will affect player stats.

    :param scenario: A string containing text describing what happens in the scenario
    :param choice1: A Choice giving one possible choice to pick
    :param choice2: A Choice giving the second possible choice to pick
    :param lab_category: An Enum denoting which Labs will come across that scenario
    :param has_been_displayed: A bool which is set to True after the LabScenario has been shown
    :param sibling: An int giving the index in the LabScenarios list which contains the same LabScenario, but
                    with different outcomes. Set to -1 if there is no sibling.
    """
    
    def __init__ (self, scenario: str, choice1: Choice, choice2: Choice, lab_category: Enum,
                  has_been_displayed: bool, sibling: int):

        self.has_been_displayed = has_been_displayed
        self.sibling = sibling

        self.scenario = scenario
        self.choice1 = choice1
        self.choice2 = choice2

        # Whether the LabScenario is associated with Big or Small studies
        self.lab_category = lab_category


class LabType(Enum):
    BIG_STUFF = 2
    SMALL_STUFF = 1
    BOTH = 0
    NONE = -1


##(happiness, knowledge, research)
lab_scenarios = [LabScenario("You didn't get enough sleep the night before. How to try to stay awake? Should you list all "\
                   "of the Real Housewives of Beverly Hills in your head that you can remember, or list all of "\
                   "the scientists in your head that you can think of?", Choice("Real Housewives", 20,0,20,
                    "Lisa Rinna...Lisa Vanderpump... Eileen Davidson... Kyle Richards... Kim Richards... "\
                    "You stay awake"), Choice("Scientists", -5, 0, 5, "You fall asleep"), LabType.BOTH),
LabScenario("You didn't get enough sleep the night before. How to try to stay awake? Should you list all of "\
            "the Real Housewives of Beverly Hills in your head that you can remember, or list all of the "\
            "scientists in your head that you can think of?", Choice("Real Housewives", -5,0,5, "You fall asleep"),
            Choice("Scientists", 5, 0, 20, "You stay awake"), LabType.BOTH),
LabScenario("You are cold because you work in the basement of a basement. You have an extra sweater "\
            "and a winter coat you can but on. But, thinking about it, maybe you should just tough it out?",
            Choice("Wear extra sweater and coat", 20,10,10,
                "Good choice. You are much warmer now and are able to think more clearly."),
            Choice("Tough it out", -60, -10, -20, "You decide to not put on your coat or extra sweater and "\
                "just tough it out. This was not a good idea. Two hours later, you reach the stage of "\
                "hypothermia where cold feels warm, and you begin paradoxical undressing. This is not good "\
                "to do in a place of research. You lose a lot of research points and happiness."), LabType.BOTH),
LabScenario("How hard to work today?", Choice("Really hard!", 10,10,10, "Good!"),
            Choice("Really really hard!", -20, -20, 0,
                "You pass out from exhaustion, and accidentally hit a lever releasing low level radiation "\
                "into the lab."), LabType.BOTH),
LabScenario("How hard to work today?",
            Choice("Really hard!", 10,5,15, "Good but could be better..."),
            Choice("Really really hard!", 20, 40, 60, "Amazing!!"), LabType.BOTH),
LabScenario("Something is flashing red. Do you press the button next to it? But wait... this is an important "\
            "experiment, and it isn't your experiment. You could mess it up. Maybe you should leave it alone?",
            Choice("Press button", 10,10,20,
            "The experiment is ruined but you save the lab from burning down! Good call!"),
            Choice("Do nothing", -40, -10, -20, "The lab burns down! :("), LabType.BOTH),
LabScenario("Something is flashing red. Do you press the button next to it? But wait... this is an important "\
            "experiment, and it isn't your experiment. You could mess it up. Maybe you should leave it alone?",
            Choice("Press button", -20,-10,10, "Experiment is ruined! Your PI is super mad at you. :("),
            Choice("Do nothing", 20, 30, 60, "Experiment is fine, good call!"), LabType.BOTH),
LabScenario("Your entire lab has been trying to discover the Bigs Hoson particle for years. You think you "\
            "see the signs of one in today's collider data. Do you immediately call the press to tell them?",
            Choice("Yes!", 50, 10, 40, 
                "You call the press and tell them. It turns out the signs were real, and you did discover "\
                "the Bigs Hoson! You become a physics celebrity and go on many talk shows."),
            Choice("No!", -10,0,0, "You decide to wait and talk to your PI first. But in the two minutes "\
                   "you wait, some other lab calls the press and announces they have discovered the Bigs Hoson. :( "),
            LabType.SMALL_STUFF),
LabScenario("Your entire lab has been trying to discover the Bigs Hoson particle for years. "\
            "You think you see the signs of one in today's collider data. Do you immediately "\
            "call the press to tell them?",
            Choice("Yes!", -50, -10, -10,
                   "You call the press and tell them. It turns out the signs were false. You are "\
                   "laughed at by all of physics."),
            Choice("No!", 20,0,20, "You decide to wait and talk to your PI first. This is the normal "\
                    "and reasonable thing to do. Turns out the signs were false. Good thing you didn't "\
                    "go to the press. "), LabType.SMALL_STUFF),
LabScenario("You were setting up some optics but you got a mirror dirty. "\
            "Should you clean it with methanol or acetone?",
            Choice("Methanol", 0,0,5,
                "This mirror had extra dirt on it and the methanol isn't strong enough... "\
                "you should have used acetone."),
            Choice("Acetone",20,0,15, "Good call! You are able to clean the mirror which had a lot of dirt on it."),
            LabType.SMALL_STUFF),
LabScenario("You were setting up some optics but you got a mirror dirty. "\
            "Should you clean it with methanol or acetone?",
            Choice("Methanol", 20,0,15,
                "Good call! This mirror didn't have that much dirt on it, so acetone would have been overkill. "\
                "You successfully clean the mirror."),
            Choice("Acetone", 0,0,5,
                "Oh no! After 20 minutes of cleaning, you end up making the mirror dirtier than it initially was."),
            LabType.SMALL_STUFF),
LabScenario("You are looking through your telescope and you see an asteroid coming to hit Earth. "\
            "The asteroid is the size of the moon. Earth is doomed. What should you do?",
            Choice("Tell your PI", -100,-100,-100, "It doesn't really matter, does it? The entire planet is doomed."),
            Choice("Go into the woods and live as a hermit for your remaining days", -100,-100,-100,
                "It doesn't really matter, does it? The entire planet is doomed."), LabType.BIG_STUFF),
LabScenario("The distance between the sun and the Earth is 93,000,000 miles. The sun has a diameter of about "\
            "860,000 miles. The Earth has a radius of about 8,000 miles. You are 5 feet tall. There are 5280 "\
            "feet in a mile. You are 0.001 miles tall. You are so tiny. A grain of sand is 0.003 feet which is "\
            "0.0000006 miles in diameter.",
            Choice("Wow that's disturbing",-15,0, 10,"Maybe you shouldn't have decided to study Big Stuff"),
            Choice("That makes me uncomfortable",-15,0,10, "Maybe you shouldn't have decided to study Big Stuff"),
            LabType.BIG_STUFF)]


class Lab:
    """ Lab for player to join. Once the player joins a lab, the player may spend time in lab in order
    to affect happiness, research, and knowledge stats.

    :param name: The name of the Lab as a string, to be displayed
    :param lab_category: The Enum type of the lab

    """

    # TODO I don't like that this is located here??
    ###set up siblings
    lab_scenarios[0].sibling = 1
    LAB_SCENARIOS[1].sibling = 0
    LAB_SCENARIOS[3].sibling = 4
    LAB_SCENARIOS[4].sibling = 3 ## a better way to do this is to just check if titles match... TODO
    LAB_SCENARIOS[5].sibling = 6
    LAB_SCENARIOS[6].sibling = 5
    LAB_SCENARIOS[7].sibling = 8
    LAB_SCENARIOS[8].sibling = 7
    LAB_SCENARIOS[9].sibling = 10
    LAB_SCENARIOS[10].sibling = 9
    
    def __init__ (self, name: str, lab_category: Enum):
        self.name = name
        self.lab_category = lab_category
    
    def generate_lab_scenario(self):
        """ Generate a LabScenario based on the LabType. Do not repeat LabScenarios.
        """

        # Create list of indices of undisplayed LabScenarios
        undisplayed_lab_scenarios = []
        for lab_scenario in lab_scenarios #NOT A CONSTANT TODO

        # Randomly generate a LabScenario associated with the LabType
        trys = 100
        for x in range (0, trys): # TODO improve this??
            # Gives me my random index
            rindex = int(random.random()*len(lab_scenarios))

            # Check to make sure that LabScenario hasn't already been displayed
            if (not lab_scenarios[rindex].has_been_displayed) and \
                (lab_scenarios[rindex].lab_category == LabType.BOTH or\
                lab_scenarios[rindex].lab_category == self.lab_category):

                # Change has_been_displayed field to True
                lab_scenarios[rindex].has_been_displayed = True
                
                # Check for a sibling, and if a sibling exists, change has_been_displayed to True
                # for the sibling also
                sindex = lab_scenarios[rindex].sibling
                if sindex >=0:
                    lab_scenarios[sindex].has_been_displayed = True
                return lab_scenarios[rindex]
        else:
            # Ran out of lab_scenarios
            return None


class Ending:
    """ Ending gives the title, image, and text to display for a given ending scenario.

    :param title: String containing the ending title
    :param image: String containing a path to the ending picture
    :param text: String containing the ending text
    """

    def __init__ (self, ending_title: str, image: str, ending_text: str):
        self.ending_title = ending_title
        self.image = image
        self.ending_text = ending_text

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
                  has_been_displayed: bool=False, sibling: int=-1):

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


class Lab:
    """ Lab for player to join. Once the player joins a lab, the player may spend time in lab in order
    to affect happiness, research, and knowledge stats.

    :param name: The name of the Lab as a string, to be displayed
    :param lab_category: The Enum type of the lab

    """
    def __init__ (self, name: str, lab_category: Enum):
        self.name = name
        self.lab_category = lab_category
    
    def generate_lab_scenario(self, lab_scenarios):
        """ Generate a LabScenario based on the LabType. Do not repeat LabScenarios.
        """

        # Create list of indices of undisplayed LabScenarios
        undisplayed_lab_scenarios = []
        for lab_scenario in lab_scenarios:
            if (not lab_scenario.has_been_displayed) and \
                (lab_scenario.lab_category == LabType.BOTH or\
                lab_scenario.lab_category == self.lab_category):
                # Append to list
                undisplayed_lab_scenarios.append(lab_scenario)

        if len(undisplayed_lab_scenarios) == 0:
            return None

        # Randomly generate lab scenario
        random_index = int(random.random()*len(undisplayed_lab_scenarios))

        # Change has_been_displayed field to True
        undisplayed_lab_scenarios[random_index].has_been_displayed = True

        # Check for a sibling, and if a sibling exists, change has_been_displayed to True
        # for the sibling also
        sibling_index = undisplayed_lab_scenarios[random_index].sibling
        if sibling_index >=0:
            lab_scenarios[sibling_index].has_been_displayed = True

        return undisplayed_lab_scenarios[random_index]


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

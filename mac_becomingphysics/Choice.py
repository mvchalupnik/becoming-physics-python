"""
Choice.py
"""

class Choice:
    """ Choice gives the text, happiness, knowledge, and research change associated with a given choice, 
    as well as a string associated with what comes afterwards.

    :param choice_text: String containing text describing the choice
    :param happiness: Int of the amount happiness will change due to this choice
    :param knowledge: Int of the amount knowledge will change due to this choice
    :param research: Int of the amount research will change due to this choice
    :param effect_text: string containing text describing the after effect of the Choice
    """
    def __init__ (self, choice_text, happiness, knowledge, research, effect_text):
        self.choice_text = choice_text #string
        self.happiness = happiness #int
        self.knowledge = knowledge #int
        self.research = research #int
        self.effect_text = effect_text #string (?)

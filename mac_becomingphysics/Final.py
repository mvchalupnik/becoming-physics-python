"""
Final.py
"""

class Final:
    """ Final contains a PhysicsClass, and a list of three Questions for the associated Final

    :param pclass: A PhysicsClass which the Final is associated with
    :param questions: A list of three Questions for the final

    """
    def __init__ (self, pclass, questions):
        self.pclass = pclass #string ## TODO IS THIS A STRING??
        self.questions = questions #List of Questions

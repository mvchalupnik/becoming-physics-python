"""
Final.py
"""

class Final:
    """ Final contains a PhysicsClass, and a list of three Questions for the associated Final

    :param physics_class: A PhysicsClass which the Final is associated with
    :param questions: A list of three Questions for the final

    """
    def __init__ (self, physics_class, questions):
        self.physics_class = physics_class #string ## TODO IS THIS A STRING??
        self.questions = questions #List of Questions


class PhysicsClass:
    """ A PhysicsClass is a university Physics class that the player can enroll in in order to
    gain knowledge and affect happiness. At the end of the quarter, the player must take
    a final exam for each PhysicsClass they have enrolled in.

    :param name: The name of the class
    :param hap: The amount of happiness the class gives you per day attended
    :param kno: The amount of knowledge the class gives you per day attended
    :param day: How many days of the class you have attended
    :param lecs: The lectures associated with the class
    :param final: The final exam associated with the class
    """
    
    def __init__ (self, name, happiness, knowledge, day, lectures, final):
        # Initialize final grade as 0, and update this after finals
        self.final_grade = 0

        self.name = name
        self.happiness = happiness
        self.knowledge = knowledge

        # Start on day 0
        self.day = 0
        self.lectures = lectures
        self.final = final

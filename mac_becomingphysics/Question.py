
class Question:
    """ A Question is a multiple choice question given on a final for a class at the end of the term.

    :param qtext: The text of the question
    :param answers: The four possible multiple choice answers
    :param answer: The correct answer
    """
    def __init__ (self, qtext, a, b, c, d, correctAnswer):
        self.qtext = qtext #string
        self.answers = [a, b, c, d] # list of strings
        self.answer = correctAnswer #char

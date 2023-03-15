
class Question:
    """ A Question is a multiple choice question given on a final for a class at the end of the term.

    :param question_text: The text of the question
    :param answers: The four possible multiple choice answers
    :param answer: The correct answer
    """
    def __init__ (self, question_text, a, b, c, d, correct_answer):
        self.question_text = question_text #string
        self.answers = [a, b, c, d] # list of strings
        self.correct_answer = correct_answer #char

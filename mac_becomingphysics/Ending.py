"""
Ending.py
"""

class Ending:
    """ Ending gives the title, image, and text to display for a given ending scenario.

    :param title: String containing the ending title
    :param image: String containing a path to the ending picture
    :param text: String containing the ending text
    """

    def __init__ (self, ending_title, image, ending_text):
        self.ending_title = ending_title
        self.image = image
        self.ending_text = ending_text

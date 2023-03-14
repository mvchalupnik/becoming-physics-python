"""
LabScenario.py
"""

class LabScenario:
    """ LabScenario describes a scenario that happens to you while you are working in lab.
        LabScenarios have associated Choices and the player's choice will affect player stats.

    """
    
    def __init__ (self, scenario, choice1, choice2, tag):
        # initialize whether the LabScenario has been displayed
        self.has_been_displayed = 0

        # A sibling is the same LabScenario but with different outcomes
        # If there is a sibling, this number will be changed to the index of the sibling
        # TODO just point to the scenario??
        self.sibling = -1

        self.scenario = scenario
        self.choice1 = choice1
        self.choice2 = choice2

        # Whether the LabScenario is associated with Big or Small studies
        self.tag = tag #TODO change this

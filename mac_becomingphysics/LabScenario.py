import variables as v

class LabScenario:
    ##Tag with big/small 
    ##class methods
    seen = 0
    sibling = -1 ##a sibling is the same labscenario but with different outcomes
    ##if there is a sibling, this number will be changed to be the index (of lss) of the sibling
    
    def __init__ (self, scenario, choice1, choice2, tag):
        self.scenario = scenario
        self.choice1 = choice1
        self.choice2 = choice2
        self.tag = tag


    

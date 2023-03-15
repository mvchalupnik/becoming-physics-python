import tkinter as tk
from PIL import Image, ImageTk
import constants as v
from PhysicsClass import *
from Lab import *
from LabScenario import *
from Final import *
from Question import *
from Ending import *


class TestAnswer(Enum):
    A = 0
    B = 1
    C = 2
    D = 3

# Texts
INTRO_TEXT = "Do you want to become physics?????\n"

REGISTER_TEXT = "There are many physics classes you can take. Unfortunately, "\
               "since you are a beginning student, you can only register for "\
               "the beginning classes. You can register for as many classes as you want, "\
               "but whichever classes you register for, you will have to take finals for at "\
               "the end of the quarter. Which classes would you like to register for?"

JOIN_TEXT = "What kind of lab do you want to join? Do you want to study Big Stuff, "\
            "like astronomy and cosmology, \nEveryday Stuff, or Small Stuff, like "\
            "particle physics and atomic physics?"

CHOOSE_CLASS_TEXT = "Which class do you want to go to?"


# Physics Lectures
COOL_PHYSICS_LECTURES = [{'lecture': "Today we're going to DERIVE Snell's Law from electrodynamics! "\
                                    "We will only get halfway through the derivation today.", 
                         'image_location':'pics/snelllaw1.png'},
                        {'lecture': "Today we finish our derivation of Snell's Law! As an added bonus, we get the Law "\
                         "of Reflection also. Yay physics!!!!!!", 'image_location': 'pics/snellpart22.png'},
                        {'lecture': "What is the electric potential of a dipole? Let's figure it out from the defition "\
                         "of electric potential, binomial expansions, and law of cosines! Yay!!!!!",
                         'image_location': 'pics/griffithsdipole.png'}, 
                         {'lecture': "What is the energy stored in an electric field? We can figure it out through logic "\
                         "and math!!! Yay physics!!!!", 'image_location': 'pics/electroenergy.png'}]

BORING_PHYSICS_LECTURES = [{'lecture': "Here is the law of reflection. Nobody knows where it comes from. Here is how you "\
                            "solve problems involving the law of reflection.", 
                            'image_location': 'pics/reflectionlawboring.png'},
                          {'lecture': "Here is Snell's Law. It is an experimental law. It cannot be derived. Here is how "\
                          "you solve problems involving Snell's Law.",
                          'image_location': 'pics/boringsnelllaw.png'},
                          {'lecture': "What is the electric potential of a dipole? Here is the equation. You can "\
                          "memorize the equation and use it to put numbers in and get numbers out. ",
                          'image_location': 'pics/dipoleboring.png'},
                          {'lecture': "What is the energy stored in an electric field? It is this equation. "\
                          "You can put in numbers for E and e0 and 2 and do math on the numbers and get "\
                          "another number and that number is a number and you can put that number into "\
                          "another number and then it will be a number with a number.....",
                          'image_location': 'pics/workenergyboring.png'}]

FAKE_PHYSICS_LECTURES = [{'lecture': "Today we're going to learn about magenetism. Magnetism was discovered by the "\
                          "great scientist Rene Descartes. His theories led to the development of Maxwell's "\
                          "equations.", 'image_location': 'pics/bigdescartes2.png'},
                         {'lecture': "Today we're going to learn about Quantum Physics.",
                         'image_location': 'pics/sciencereligion2.png'},
                         {'lecture': "Today we're going to learn about how mass and electromagnetism are related.",
                         'image_location': 'pics/yourlegalaction.png'}]

MATH_PHYSICS_LECTURES = [{'lecture': ":-/ ", 'image_location': 'pics/sadimaginary.png'},
                         {'lecture': ":-(", 'image_location': 'pics/saddiffeqmodified.png'},
                         {'lecture': ":,-(", 'image_location': 'pics/saderff.png'},
                         {'lecture': ":,,,,,,,-(", 'image_location': 'pics/sadwahhmath.png'}]

OCHECM_LECTURES = [{'lecture': "Here are some reactions. These reactions have mechanisms that are part logical "\
                   "and part arbitrary. You will probably need to memorize the reagents. But that's ok, "\
                   "it's not like there are whole other classes of reactions", 
                   'image_location': 'pics/alkynestuffs2.png'},
                   {'lecture': "Lol jk there actually are many other classes of reactions. Here are some with alkynes. "\
                   "(Don't forget alcohols and aldehydes and esters and ethers and...)",
                   'image_location': 'pics/alkenestuffs2.png'},
                   {'lecture': "NMR can be used to identify chemicals. We're going to memorize the positions of NMR peaks. ",
                   'image_location': 'pics/nmrstuffs2.png'},
                   {'lecture': "Here are some more arbitrary things to memorize.",
                   'image_location': 'pics/couplingconstants.png'},
                   {'lecture': "Here are some PKAs to memorize.", 'image_location': 'pics/pkas.png'}]

##FINALS!!
COOL_FINAL = Final("Cool Physics", 
            [Question("A photon checks into a hotel. The bellhop asks, 'Can I help you with your luggage?'"\
                    "What does the photon say?",
                      "A. Yes, please do.", "B. No thanks, I'm super good at carrying things.",
                      "C. That's offensive. ", "D. I don't have any, I'm travelling light.", TestAnswer.D),
            Question("A neutron walked into a bar and asked 'How much for a drink?' What did the bartender"\
                     "reply?", "A. $5", "B. For you, no charge", "C. 5 Coulombs", "D. 5 e", TestAnswer.B), 
            Question("Two atoms are walking down the street. One says to the other, 'Hey, I think I lost an "\
                     "electron!' The other says, 'Are you sure?' What does the first one reply?",
                     "A. Yes, I'm positive!", "B. No, you can never be 100 percent sure about anything in life",
                     "C. No, I'm neutral!", "D. Yes, I'm negatively sure!", TestAnswer.A)])
BORING_FINAL = Final("Boring Physics",
              [Question("F = MA. If M = 5 kg and a = 20 m/s, what is F?",
                "A. 4 Newtons", "B. 100 Newtons", "C. 200 Newtons", "D. This is so boring.", TestAnswer.D),
               Question("If I can travel 100 miles in 40 seconds, how many miles can I travel in 20 seconds?",
                "A. 0 miles because I'm tired now.", "B. Unrealistic speeds. No one can travel that fast.",
                "C. 50 miles", "D. 40 miles", TestAnswer.B),
               Question("N is a number. E(N) is an equation that gives some other number you want to know. "\
                "What is the other number you want to know?", "A. N", "B. N(E)", "C. E(N)",
                "D. I am asleep right now", TestAnswer.D)])
FAKE_FINAL = Final("Controversial Physics",
            [Question("Light is electromagnetic radiation. It travels through the ether, even though "\
                "we have not detected ether yet. Why have we not detected ether yet?",
                "A. Ether doesn't exist",
                "B. We don't have sensitive enough intruments but we will find it someday",
                "C. Special relativity means that ether exists but is impossible to detect",
                "D. Ether travels at the speed of light, so it is too fast to detect.", TestAnswer.B),
            Question("Which field is objectively the best field?",
                "A. Biology", "B. Chemistry", "C. Physics", "D. Math", TestAnswer.C),
            Question("The Bohr model is an early model of atomic structure that was later shown to be bad. "\
                "What is the best reason for why it is bad?",
                "A. Quantum physics means the Heisenberg Uncertainty principle which is wave particle "\
                "duality \nand quantum mechanics to be of itself", "B. Actually the Bohr model is correct",
                "C. Because it's BOHRING HAHAHAHAHAHAHAHAHAHHAH sorry I'll never \ntry to make a joke ever again.",
                "D. If the Bohr model were accurate, that would mean that electrons "\
                "were \nplanets orbiting nuclei which were suns and little tiny people lived in those planets, "\
                "\nbut we already know there are only 8 million people on Earth, and \nthere's several hundreds "\
                "of atoms on Earth, so that means there can't be any more people.", TestAnswer.B)])
MATH_FINAL = Final("Math Physics",
            [Question(" :( ", "A. :( ", "B. :, (", "C. :,,,,(", "D. :/", TestAnswer.A),
             Question("X = ?", "A. 1", "B. 2", "C. 3", "4. -100000", TestAnswer.A),
             Question("math = ?", "A. Mad - d + th", "B. Sad - d + th", "C. Bad - d + th", "D. Rad - d + th", TestAnswer.A)])
OCHEM_FINAL = Final("Organic Chemistry",
             [Question("Which reagents will take you from an alkyne to an antimarkovnikov brominated alkene? "\
                "Please also draw the mechanism.", "A. Br_2", "B. HBr and H_2O_2", "C. Lindlar's catalyst",
                "D. NaBr, H_2O", TestAnswer.B),
             Question("Order these hydrogens in order of NMR delta shift, from lower shift to higher shift. "\
                "(Hint: hydrogens that are more delta shifted tend to be attached to electronegative atoms "\
                "since they are more deshielded from the magnetic field. However, there are exceptions. The "\
                "exceptions are justified by rules that are arbitrarily made up to fit the exceptions.)",
                "A. carboxylic acid hydrogen, hydrogen on a phenyl, hydrogen on a phenol, hydrogen on an "\
                "alkane carbon", "B. hydrogen on an alkane carbon,  hydrogen on a phenyl, hydrogen on a phenol,"\
                " carboxylic acid hydrogen", "C. hydrogen on an alkane carbon, hydrogen on a phenol, hydrogen"\
                " on a phenyl, carboxylic acid hydrogen", "D. hydrogen on an alkane carbon, hydrogen on a phenyl,"\
                " carboxylic acid hydrogen, hydrogen on a phenol", TestAnswer.B),
             Question("Order the hydrogens by PKAs, low to high. (Hint: PKA is defined as the - "\
                "log of the concentration of H+ divided by the concentration of the conjugate base "\
                "at equilibrium. Strong acids tend to have lower PKAs. Acidity depends on the "\
                "electronegativity of the atom the hydrogen is attached to, resonance, orbital effects, "\
                "and ultimately, memorization.)", 
                "A. diketone, phenol, carboxylic acid, hydrogen on a carbon connected to two nitriles", 
                "B. carboxylic acid, phenol, hydrogen on a carbon connected to two nitriles, diketone", 
                "C. carboxylic acid, diketone, phenol, hydrogen on a carbon connected to two nitriles ", 
                "D. carboxylic acid, phenol, diketone, hydrogen on a carbon connected to two nitriles ", TestAnswer.C)])

# Create classes and put them into a class list
ALL_CLASSES = [PhysicsClass("Cool Physics", 15, 15, 0, 
            COOL_PHYSICS_LECTURES, COOL_FINAL), 
            PhysicsClass("Boring Physics", -15, 5, 0, BORING_PHYSICS_LECTURES, BORING_FINAL), 
            PhysicsClass("Fake Physics", -5, 5, 0, FAKE_PHYSICS_LECTURES, FAKE_FINAL),
            PhysicsClass("Math Physics", -20, 20, 0, MATH_PHYSICS_LECTURES, MATH_FINAL),
            PhysicsClass("Organic Chemistry",-15,-5, 0, OCHECM_LECTURES, OCHEM_FINAL)]


##LAB STUFF
ALL_LABS = [Lab("Big Stuff", LabType.BIG_STUFF), 
            Lab("Medium-Sized Stuff", LabType.NONE),
            Lab("Small Stuff", LabType.SMALL_STUFF)]





###Endings
#TODO get rid of weird inconsistent camel case

# Ending where happiness drops to 0
SAD_ENDING = Ending("Ending 1 of 6: Sad Hermit",
                    'pics/hermit.png',
                    "You are too unhappy, and you decide physics isn't for you. "\
                    "Disillusioned, you drop out of school and become a hermit. "\
                    "You become the coolest hermit in the world. Unfortunately, "\
                    "you did not become physics. YOU LOSE.")

# Ending if you don't enroll in any classes
NO_CLASSES_ENDING = Ending("Ending 2 of 6: You didn't enroll in any classes?",
                         'pics/noclasses.png',
                         "You didn't enroll in any classes? How can you become physics if you don't enroll "\
                         "in any physics classes? More importantly, How can you measure your self worth "\
                         "without grades and a gpa? YOU LOSE.")

# Ending where you become chemistry by mistake... TODO

# Ending if you finish the quarter but without high research or knowledge
BAD_STUDENT_ENDING = Ending("Ending 3 of 6: Bad Student",
                          'pics/badstudent.png',
                          "You did not have high enough knowledge or research. You did not become physics. "\
                          "You became a bad student. YOU LOSE.")

# Ending with med/low knowledge (between 0 and 79), high research (between 80 and 100)
SCOPE_ENDING = Ending("Ending 4 of 6: Too much research", 
                     'pics/scope1.jpg', 
                     "Oh no! You became an oscilloscope! You spent too much time in the lab! "\
                     "Your research went up but you didn't have high enough knowledge to go to "\
                     "grad school. YOU LOSE.")

# Ending with high knowledge (between 80 and 100), research > 50, happiness > 50
GRAD_SCHOOL_ENDING = Ending("Ending 5 of 6: Physicist",
                          'pics/physicist.png',
                          "You have a lot of physics knowledge, so you go to grad school. "\
                          "You become a physicist, not a physics! YOU LOSE.")

# Ending with happiness = between 90 and 100. research between 90 and 100. Knowledge between 90 and 100.
EQUATION_ENDING = Ending("Ending 6 of 6: Success!",
                        'pics/becomingphys.png',
                        "You did it!! You became a physics of yourself! This is you. You became physics! "\
                        "See how happy you are! YOU WIN!")

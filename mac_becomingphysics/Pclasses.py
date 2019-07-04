import tkinter as tk
from PIL import Image, ImageTk
import variables as v
from Pclass import *
from Lab import *
from LabScenario import *
from Final import *
from Question import *
from Ending import *

A = 0
B = 1
C = 2
D = 3

##TODO lecture words
coolphyslec1 = ["Today we're going to DERIVE Snell's Law from electrodynamics! We will only get halfway through the derivation today.", 'pics/snelllaw1.png']
coolphyslec2 = ["Today we finish our derivation of Snell's Law! As an added bonus, we get the Law of Reflection also. Yay physics!!!!!!", 'pics/snellpart22.png']
coolphyslec3 = ["What is the electric potential of a dipole? Let's figure it out from the defition of electric potential, binomial expansions, and law of cosines! Yay!!!!!", 'pics/griffithsdipole.png']
coolphyslec4 = ["What is the energy stored in an electric field? We can figure it out through logic and math!!! Yay physics!!!!", 'pics/electroenergy.png']

boringphyslec1 = ["Here is the law of reflection. Nobody knows where it comes from. Here is how you solve problems involving the law of reflection.", 'pics/reflectionlawboring.png']
boringphyslec2 = ["Here is Snell's Law. It is an experimental law. It cannot be derived. Here is how you solve problems involving Snell's Law.", 'pics/boringsnelllaw.png']
boringphyslec3 = ["What is the electric potential of a dipole? Here is the equation. You can memorize the equation and use it to put numbers in and get numbers out. ",'pics/dipoleboring.png']
boringphyslec4 = ["What is the energy stored in an electric field? It is this equation. You can put in numbers for E and e0 and 2 and do math on the numbers and get another number and that number is a number and you can put that number into another number and then it will be a number with a number.....",'pics/workenergyboring.png']

fakephyslec1 = ["Today we're going to learn about magenetism. Magnetism was discovered by the great scientist Rene Descartes. His theories led to the development of Maxwell's equations.",'pics/bigdescartes2.png']
fakephyslec2 = ["Today we're going to learn about Quantum Physics.", 'pics/sciencereligion2.png']
fakephyslec3 = ["Today we're going to learn about how mass and electromagnetism are related.", 'pics/yourlegalaction.png']

mathphyslec1 = [":-/ ",'pics/sadimaginary.png']
mathphyslec2 = [":-(", 'pics/saddiffeqmodified.png']
mathphyslec3 = [":,-(", 'pics/saderff.png']
mathphyslec4 = [":,,,,,,,-(", 'pics/sadwahhmath.png']

ochemlec1 = ["Here are some reactions. These reactions have mechanisms that are part logical and part arbitrary. You will probably need to memorize the reagents. But that's ok, it's not like there are whole other classes of reactions", 'pics/alkynestuffs2.png'] 
ochemlec2 = ["Lol jk there actually are many other classes of reactions. Here are some with alkynes. (Don't forget alcohols and aldehydes and esters and ethers and...)",'pics/alkenestuffs2.png']
ochemlec3 = ["NMR can be used to identify chemicals. We're going to memorize the positions of NMR peaks. ", 'pics/nmrstuffs2.png']
ochemlec4 = ["Here are some more arbitrary things to memorize.", 'pics/couplingconstants.png']
ochemlec5 = ["Here are some PKAs to memorize.", 'pics/pkas.png']

##FINALS!!
coolfinal = Final("Cool Physics", Question("A photon checks into a hotel. The bellhop asks, 'Can I help you with your luggage?' What does the photon say?", "A. Yes, please do.", "B. No thanks, I'm super good at carrying things.", "C. That's offensive. ", "D. I don't have any, I'm travelling light.", D), Question("A neutron walked into a bar and asked 'How much for a drink?' What did the bartender reply?", "A. $5", "B. For you, no charge", "C. 5 Coulombs", "D. 5 e", B), Question("Two atoms are walking down the street. One says to the other, 'Hey, I think I lost an electron!' The other says, 'Are you sure?' What does the first one reply?", "A. Yes, I'm positive!", "B. No, you can never be 100 percent sure about anything in life", "C. No, I'm neutral!", "D. Yes, I'm negatively sure!", A))
boringfinal = Final("Boring Physics", Question("F = MA. If M = 5 kg and a = 20 m/s, what is F?", "A. 4 Newtons", "B. 100 Newtons", "C. 200 Newtons", "D. This is so boring.", D), Question("If I can travel 100 miles in 40 seconds, how many miles can I travel in 20 seconds?", "A. 0 miles because I'm tired now.", "B. Unrealistic speeds. No one can travel that fast.", "C. 50 miles", "D. 40 miles", B), Question("N is a number. E(N) is an equation that gives some other number you want to know. What is the other number you want to know?", "A. N", "B. N(E)", "C. E(N)", "D. I am asleep right now", D))
fakefinal = Final("Controversial Physics", Question("Light is electromagnetic radiation. It travels through the ether, even though we have not detected ether yet. Why have we not detected ether yet?", "A. Ether doesn't exist", "B. We don't have sensitive enough intruments but we will find it someday", "C. Special relativity means that ether exists but is impossible to detect", "D. Ether travels at the speed of light, so it is too fast to detect.", B), Question("Which field is objectively the best field?", "A. Biology", "B. Chemistry", "C. Physics", "D. Math", C), Question("The Bohr model is an early model of atomic structure that was later shown to be bad. What is the best reason for why it is bad?", "A. Quantum physics means the Heisenberg Uncertainty principle which is wave particle duality \nand quantum mechanics to be of itself", "B. Actually the Bohr model is correct", "C. Because it's BOHRING HAHAHAHAHAHAHAHAHAHHAH sorry I'll never \ntry to make a joke ever again.", "D. If the Bohr model were accurate, that would mean that electrons were \nplanets orbiting nuclei which were suns and little tiny people lived in those planets, \nbut we already know there are only 8 million people on Earth, and \nthere's several hundreds of atoms on Earth, so that means there can't be any more people.", B))
mathfinal = Final("Math Physics", Question(" :( ", "A. :( ", "B. :, (", "C. :,,,,(", "D. :/", A), Question("X = ?", "A. 1", "B. 2", "C. 3", "4. -100000", A), Question("math = ?", "A. Mad - d + th", "B. Sad - d + th", "C. Bad - d + th", "D. Rad - d + th", A))
ochemfinal = Final("Organic Chemistry", Question("Which reagents will take you from an alkyne to an antimarkovnikov brominated alkene? Please also draw the mechanism.", "A. Br_2", "B. HBr and H_2O_2", "C. Lindlar's catalyst", "D. NaBr, H_2O", B), Question("Order these hydrogens in order of NMR delta shift, from lower shift to higher shift. (Hint: hydrogens that are more delta shifted tend to be attached to electronegative atoms since they are more deshielded from the magnetic field. However, there are exceptions. The exceptions are justified by rules that are arbitrarily made up to fit the exceptions.)", "A. carboxylic acid hydrogen, hydrogen on a phenyl, hydrogen on a phenol, hydrogen on an alkane carbon", "B. hydrogen on an alkane carbon,  hydrogen on a phenyl, hydrogen on a phenol, carboxylic acid hydrogen", "C. hydrogen on an alkane carbon, hydrogen on a phenol, hydrogen on a phenyl, carboxylic acid hydrogen", "D. hydrogen on an alkane carbon, hydrogen on a phenyl, carboxylic acid hydrogen, hydrogen on a phenol", B), Question("Order the hydrogens by PKAs, low to high. (Hint: PKA is defined as the - log of the concentration of H+ divided by the concentration of the conjugate base at equilibrium. Strong acids tend to have lower PKAs. Acidity depends on the electronegativity of the atom the hydrogen is attached to, resonance, orbital effects, and ultimately, memorization.)", "A. diketone, phenol, carboxylic acid, hydrogen on a carbon connected to two nitriles", "B. carboxylic acid, phenol, hydrogen on a carbon connected to two nitriles, diketone", "C. carboxylic acid, diketone, phenol, hydrogen on a carbon connected to two nitriles ", "D. carboxylic acid, phenol, diketone, hydrogen on a carbon connected to two nitriles ", C))


##TODO reevaluate statistics assigned to each class (happiness, knowledge, day)
classlist = [Pclass("Cool Physics", 15, 15, 0, 
[coolphyslec1, coolphyslec2, coolphyslec3,coolphyslec4], coolfinal), 
Pclass("Boring Physics", -15, 5, 0, 
[boringphyslec1, boringphyslec2, boringphyslec3,boringphyslec4], boringfinal), 
Pclass("Fake Physics", -5, 5, 0, 
[fakephyslec1, fakephyslec2, fakephyslec3], fakefinal),
Pclass("Math Physics", -20, 20, 0, 
[mathphyslec1, mathphyslec2, mathphyslec3, mathphyslec4], mathfinal),
Pclass("Organic Chemistry",-15,-5, 0, 
[ochemlec1, ochemlec2, ochemlec3,ochemlec4,ochemlec5], ochemfinal)]
##TODO implement finals!




##LAB STUFF
lablist = [Lab("Big Stuff"), Lab("Medium-Sized Stuff"), Lab("Small Stuff")]

###Endings

#Happiness drops to 0
sadEnding = Ending("Ending 1 of 6: Sad Hermit", 'pics/hermit.png', "You are too unhappy, and you decide physics isn't for you. Disillusioned, you drop out of school and become a hermit. You become the coolest hermit in the world. Unfortunately, you did not become physics. YOU LOSE.") ##pic TODO

#don't enroll in any classes
noClassesEnding = Ending("Ending 2 of 6: You didn't enroll in any classes?", 'pics/noclasses.png', "You didn't enroll in any classes? How can you become physics if you don't enroll in any physics classes? More importantly, How can you measure your self worth without grades and a gpa? YOU LOSE.") ##pic TODO

##become chemistry by mistake... TODO

##finish the quarter but not high research or knowledge
badStudentEnding = Ending("Ending 3 of 6: Bad Student", 'pics/badstudent.png', "You did not have high enough knowledge or research. You did not become physics. You became a bad student. YOU LOSE.") ##pic TODO

##med/low knowledge (between 0 and 79), high research (between 80 and 100)
scopeEnding = Ending("Ending 4 of 6: Too much research", 'pics/scope1.jpg', "Oh no! You became an oscilloscope! You spent too much time in the lab! Your research went up but you didn't have high enough knowledge to go to grad school. YOU LOSE.") ##pic TODO

##high knowledge (between 80 and 100), research > 50, happiness > 50
gradSchoolEnding = Ending("Ending 5 of 6: Physicist", 'pics/physicist.png', "You have a lot of physics knowledge, so you go to grad school. You become a physicist, not a physics! YOU LOSE.") ##Pic todo

##happiness = between 90 and 100. research between 90 and 100. Knowledge between 90 and 100.
equationEnding = Ending("Ending 6 of 6: Success!", 'pics/becomingphys.png', "You did it!! You became a physics of yourself! This is you. You became physics! See how happy you are! YOU WIN!")



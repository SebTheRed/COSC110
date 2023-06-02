#Sebastian Belfonti
#COSC 110-821 Assignment 2
#This class is instantialized with an input (as a float) from the user.
#This input is then multiplied by 9.8 to create the weight aka Newtons.
#The user is then alerted whether or not the weight is too heavy, too light, or just right.

class Weight:
    def __init__ (self, mass):
        self.weightInNewtons = mass * 9.8
    def calcWeight (self):
        if self.weightInNewtons > 500:
            print("Too Heavy!")
        elif self.weightInNewtons < 100:
            print("Too Light!")
        else:
            print("Weight is acceptable!")

inputMass = float(input("Please enter the mass of the object: "))
weightInstance = Weight(inputMass)
weightInstance.calcWeight()
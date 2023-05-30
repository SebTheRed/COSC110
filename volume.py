#Sebastian Belfonti
#COSC 110-821
#This class takes a user's input of radius & liquid height.
#Then uses those values along with the `self.PI` constant to perform a volume calculation.
#This calculation is then output to the user in a nice block-like format.

class CylinderCalculations:
    def __init__ (self):
        self.PI = 3.14159
        self.yellowColor = '\033[33m'
        self.resetColor = '\033[0m'
    def getValues (self):
        tankRadius = float(input("Please enter the tank's radius: "))
        liquidHeight = float(input("Please enter the height of the liquid from the bottom of the tank: "))
        liquidVolume = (self.PI * (tankRadius ** 2) * liquidHeight )
        print(f"""
        Radius {tankRadius:>14.1f} cm
        Height {liquidHeight:>14.1f} cm
        {self.yellowColor}Volume {liquidVolume:>14,.1f} cubic cm{self.resetColor}
        """)

cylinderInstance = CylinderCalculations()
cylinderInstance.getValues()
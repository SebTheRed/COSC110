#Sebastian Belfonti
#COSC 110-821 Assignment 2
#This class instantializes with a user input of weight.
#The weight is then assigned to a variable that is then passed through a series of if statements.
#It's important to start with the highest weight to ensure the logic is passed down correctly.
#The string `self.returnString` is concatenated with the value of the appropriate shipping cost as a string.
#That string is then returned to the user.

#P.S. Please let me know if the color codes are unacceptable.

class ShippingCharges:
    def __init__ (self, weight):
        self.packageWeight = weight
        self.returnString = "\033[33mIt will cost you: "
        if self.packageWeight > 10:
            self.returnString += "\033[32m$4.74"
        elif self.packageWeight > 6:
            self.returnString += "\033[32m$4.00"
        elif self.packageWeight > 2:
            self.returnString += "\033[32m$3.00"
        else:
            self.returnString += "\033[32m$1.50"
        self.returnString += "\033[33m to ship this package!\033[0m"
        print(self.returnString)

weightInput = float(input("Please enter the weight of what you are trying to ship: "))
shippingInstance = ShippingCharges(weightInput)
            
        
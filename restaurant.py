#Sebastian Belfonti
#COSC 110-821
#This class asks for user input of the cost of a meal (food & drink).
#It then does calculations on the input float to determine tax, tip, and total.
#Those values are then returned to the user in a nice box-like format!

#Please let me know if OOP is not acceptable at this level, I can return to functional.
#I simply prefer OOP.
#I am excited for a summer of Python :)

class TabCalc:
    def __init__ (self):
        self.mealTotal = 0
        self.greenColor = '\033[32m'
        self.resetColor = '\033[0m'
    def getMealTotal (self):
        self.mealTotal = float(input("Please enter the cost of all food & drink ordered: "))
        taxTotal = self.mealTotal * 0.06
        tipTotal = self.mealTotal * 0.18
        totalBill = self.mealTotal + taxTotal + tipTotal
        print(f"""
        Meal {self.mealTotal:>9.2f}
        Tax {taxTotal:>10.2f}
        Tip {tipTotal:>10.2f}
        {self.greenColor}Total {totalBill:>8.2f}{self.resetColor}
        """)
        #I could have used "\n" to call new lines, but I learned in the textbook that one can triple quotes and break lines! How cool. I find it looks better in the output too!

diningInstance = TabCalc()
diningInstance.getMealTotal()


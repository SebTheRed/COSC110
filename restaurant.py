class TabCalc:
    def __init__ (self):
        self.mealTotal = 0
        self.greenColor = '\033[32m'
        self.resetColor = '\033[0m'
    def getMealTotal (self):
        self.mealTotal = float(input("Please enter the cost of all food & drink ordered: "))
        self.taxTotal = self.mealTotal * 0.06
        self.tipTotal = self.mealTotal * 0.18
        self.totalBill = self.mealTotal + self.taxTotal + self.tipTotal
        print(f"""
        Meal {self.mealTotal:>9.2f}
        Tax {self.taxTotal:>10.2f}
        Tip {self.tipTotal:>10.2f}
        {self.greenColor}Total {self.totalBill:>8.2f}{self.resetColor}
        """)
        #I could have used "\n" to call new lines, but I learned in the textbook that one can triple quotes and break lines! How cool. I find it looks better in the output too!

diningInstance = TabCalc()
diningInstance.getMealTotal()

#Please let me know if OOP is not acceptable at this level, I can return to functional.
#I simply prefer OOP.
#I am excited for a summer of Python :)
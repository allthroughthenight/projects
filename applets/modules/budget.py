# Buget calculator

def run():
    print("Budget Calculator")

    monthly = float(input("What is your monthly income?: "))

    idealBudget = input("Would you like an ideal budget? Y/N: ")
    
    # Ideal Budget
    # 25% housing
    # 15% savings
    # 15% transportation
    # 10% food
    # 10% utilities
    # 5% healthcare
    # ---
    # 20% left over
    
    if idealBudget == "Y":
        foodBudget = .10
        healthcareBudget = .05
        housingBudget = .25
        transportationBudget = .15
        utilitiesBudget = .10
        savingBudget = .15
    else:
        foodBudget = (float(input("Groceries budget?: "))) / 100
        healthcareBudget = (float(input("Healthcare budget?: "))) / 100
        housingBudget = (float(input("Housing budget?: "))) / 100
        transportationBudget = (float(input("Transportation budget?: "))) / 100
        utilitiesBudget = (float(input("Utilities budget?: "))) / 100
        savingBudget = (float(input("How much would you like to save?: "))) / 100

    total = housingBudget + savingBudget + transportationBudget + \
        foodBudget + utilitiesBudget + healthcareBudget
    extra = 0.0

    if total > 1:
        print("Your budget is too large, try again!")
        exit()

    extraBudget = 1 - total
    total += extraBudget

    if extraBudget > 0:
        print("You budget is too small, you have %.0f%% extra budget" % (extraBudget * 100))

    housingCost = monthly * housingBudget
    savingCost = monthly * savingBudget
    transportationCost = monthly * transportationBudget
    foodCost = monthly * foodBudget
    utilitiesCost = monthly * utilitiesBudget
    healthcareCost = monthly * healthcareBudget
    extraCost = monthly * extraBudget

    print("Monthly Income: %i" % monthly)
    print("")
    print("Item\t\tPercentage\tAllowance")
    print("Housing\t\t%.0f%%\t\t$%.0f" % ((100 * housingBudget), housingCost))
    print("Savings\t\t%.0f%%\t\t$%.0f" % ((100 * savingBudget), savingCost))
    print("Transportation\t%.0f%%\t\t$%.0f" % ((100 * transportationBudget), transportationCost))
    print("Food\t\t%.0f%%\t\t$%.0f" % ((100 * foodBudget), foodCost))
    print("Utilities\t%.0f%%\t\t$%.0f" % ((100 * utilitiesBudget), utilitiesCost))
    print("Healthcare\t%.0f%%\t\t$%.0f" % ((100 * healthcareBudget), healthcareCost))
    if extraBudget > 0:
        print("Extra\t\t%.0f%%\t\t$%.0f" % ((100 * extraBudget), extraCost))

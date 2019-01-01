# day02
# Given the following, find the total cost
# Meal price (base cost of a meal)
# Tip percent (the percentage of the meal price being added as tip)
# Tax percent (the percentage of the meal price being added as tax) for a meal

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    total = meal_cost                           # take param
    total += (meal_cost * (tip_percent/100))    # add tip cost
    total += (meal_cost * (tax_percent/100))    # add tax cost
    total = int(round(total, 0))                # round float and remove trailing zero
    return total

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(solve(meal_cost, tip_percent, tax_percent))


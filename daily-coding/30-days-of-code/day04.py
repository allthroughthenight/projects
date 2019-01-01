# day04
# 1. yearPasses() should increase the instance variable by 1
# 2. amIOld() should perform the following conditional actions:
#   if age < 13, print you are young..
#   if age >= 12 and age < 18, print you are a teenager..
#   otherwise, print you are old..

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.age = initialAge
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        elif self.age >=13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1

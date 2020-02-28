# Life expectancy clock

from datetime import date

def run():
    print("")
    print("Life Clock Calculator")
    print("")

    age = int(input("How old are you?: "))
    death = int(input("When do you think you'll die?: "))
    print("Average life expectancy in America as of 2015 is 78")

    years = death - age
    currentWeek = date.today().isocalendar()[1]
    weeksLeft = 54 - currentWeek

    print("You have %i years and %i weeks left to live, have fun!" % (years, weeksLeft))

# Challenge
# Life expectancy clock like [this](https://github.com/adamtait/ArduinoDeathClock)
#
# To-Do
# Ask life questions and query database(s) to automate estimation
# Exact down to the day, maybe hour
# Use network time clock
# Validate input

from datetime import date

age = int(input("How old are you?: "))
death = int(input("When do you think you'll die?: "))
print("Average life expectancy in America as of 2015 is 78")

years = death - age
currentWeek = date.today().isocalendar()[1]
weeksLeft = 54 - currentWeek

print("You have %i years and %i weeks left to live, have fun!" % (years, weeksLeft))

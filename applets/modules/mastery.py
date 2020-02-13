#
# Challenge
#
# 10,000 hours calculator like [this](http://www.10000hourcalc.com/) or [this](https://toolstud.io/calculate/practice.php)
#
# To-Do
#
# Exact down to the day, maybe hour
# Validate input

# preamble
def title():
    print("")
    print("10,000 Hours Mastery Calculator")
    print("Copyright 2018")
    print("")

def input():
    # input prompt
    days = float(input("How many days a week will you practice? (1-7): "))
    hours = float(input("How many hours per day will you practice? (1-23): "))

def calc1():
    # calculate weekly hours`
    weekly = days * hours

    # calculate yearly hours
    yearly = 54 * weekly

def hours1():
    # total time in smaller bites
    print("Hours per week: %.0f" % weekly)
    print("Hours per year: %.0f" % yearly)

def calc2():
    # calculate total weeks
    totalWeeks = 10000/weekly

    # calculate total years from the number of weeks
    totalYears = totalWeeks/54

    # find remainer weeks when compared to how many per year
    extraWeeks = totalWeeks % 54

def hours2():
    # print total
    print("Total time - %.0f years and %.0f weeks" % (totalYears, extraWeeks))

# 10,000 hours to Mastery calculator

def run():
    print("")
    print("10,000 Hours to Mastery Calculator")
    print("")

    # input prompt
    days = float(input("How many days a week will you practice? (1-7): "))
    hours = float(input("How many hours per day will you practice? (1-23): "))

    # calculate weekly hours
    weekly = days * hours

    # calculate yearly hours
    yearly = 54 * weekly

    # total time in smaller bites
    print("Hours per week: %.0f" % weekly)
    print("Hours per year: %.0f" % yearly)

    # calculate total weeks
    totalWeeks = 10000/weekly

    # calculate total years from the number of weeks
    totalYears = totalWeeks/54

    # find remainer weeks when compared to how many per year
    extraWeeks = totalWeeks % 54

    # print total
    print("Total time - %.0f years and %.0f weeks" % (totalYears, extraWeeks))

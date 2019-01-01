# day06
# given a string, S, of length N that is indexed from 0 to N -1
# print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line

# get string count
stringCount = int(input())
stringIn = []

# take in strings
for x in range(0, stringCount):
    stringIn.append(input())

# go through string list
for x in range(0, stringCount):
    # turn string into list
    tempListWord = list(stringIn[x])

    # temp odd and even lists
    tempListOdd = []
    tempListEven =[]

    # if odd index add letter to odd list
    for y in range(0, len(tempListWord)):
        if y%2 > 0:
            tempListOdd.append(tempListWord[y])
        # else add to even list
        else:
            tempListEven.append(tempListWord[y])

    print("{} {}".format(''.join(tempListEven) ,''.join(tempListOdd)))

# day08
# given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
# you will then be given an unknown number of names to query your phone book for.
# for each name queried, print the associated entry from your phone book on a new line in the form name=phonenumber
# if an entry name for is not found, print not found instead.

recordCount = int(input())
recordStore = {}
tempTest =[]

for x in range(0, recordCount):

    # two item list of name and record number delimited by space
    splitInput = (input()).split(' ')

    # append two item list to working list
    tempTest.append(splitInput)

# cast 2D array to dict
recordStore = dict(tempTest)

for record in recordStore:
    find = input()
    if find in recordStore:
        print("{}={}".format(find,recordStore.get(find)))
    else:
        print('Not found')

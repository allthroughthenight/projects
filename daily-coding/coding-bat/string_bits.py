# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
  myList = list(str)
  myString = ''
  for x in range(0, len(myList)):
    if x % 2 == 0:
      myString += myList[x]

  return myString

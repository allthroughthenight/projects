# Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
  myList = list(str)
  back = myList[-1:]

  myList[-1:] = myList[:1]
  myList[:1] = back

  myString =''
  myString = myString.join(myList)
  return myString

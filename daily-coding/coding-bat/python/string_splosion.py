# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  myList = list(str)
  myCopy = []
  myString = ''

  for x in range(0,len(myList) + 1):
    myCopy += str[0:x]

  myString = myString.join(myCopy)

  return myString

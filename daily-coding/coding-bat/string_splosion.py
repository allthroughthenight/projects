# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  myList = list(str)
  myCopy = []
  myString = ''

  for x in range(0,len(myList)):
    myCopy += myList[0:x+1]

  myString = myString.join(myCopy)

  return myString

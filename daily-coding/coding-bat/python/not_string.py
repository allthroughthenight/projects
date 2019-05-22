# Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged. 

def not_string(str):
  front = str.split(' ')
  phrase = ''
  if front[0] == "not":
    phrase = str
  else:
    phrase = 'not ' + str
  return phrase

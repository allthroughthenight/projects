#  Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
  length = len(str)
  end = str[length - 2 : length]
  count = 0
  for x in range(length - 2):
    if str[x:x+2] == end:
      count += 1
  return count

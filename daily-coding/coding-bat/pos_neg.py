# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

def pos_neg(a, b, negative):
  result = False
  if negative:
    if (a < 0) and (b < 0):
      result = True
  elif (a < 0 and b > -1):
    result = True
  elif (a > -1 and b < 0):
    result = True

  return result

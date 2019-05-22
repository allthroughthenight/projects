# Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
  summation = 0
  if a == b:
    summation = 2 * (a + b)
  else:
    summation = a + b
  return summation

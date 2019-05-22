# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a, b):
  summation = a + b
  is10 = False
  if summation == 10 or a == 10 or b == 10:
    is10 = True
  return is10

# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

def near_hundred(n):
  close = False
  check100 = abs(100 - n)
  check200 = abs(200 - n)
  if check100 <= 10 or check200 <= 10:
    close = True
  return close

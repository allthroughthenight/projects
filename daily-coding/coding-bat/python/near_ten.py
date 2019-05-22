# Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod

def near_ten(num):
  near = False
  close = num % 10
  if close <= 2 or close >= 8:
    near = True

  return near

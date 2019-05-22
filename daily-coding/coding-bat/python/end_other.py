# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

def end_other(a, b):
  a_low = a.lower()
  b_low = b.lower()
  a_len = len(a)
  b_len = len(b)
  if a_low.endswith(b_low,a_len - b_len, a_len):
    return True
  elif b_low.endswith(a_low,b_len - a_len, b_len):
    return True
  else:
    return False

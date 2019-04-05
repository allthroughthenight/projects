# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

def non_start(a, b):
  short_a = a[1::]
  short_b = b[1::]
  return short_a + short_b

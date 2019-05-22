# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

def lone_sum(a, b, c):
  diff = 0

  if a == b or a == c:
    diff -= a
  if b == a or b == c:
    diff -= b
  if c == a or c == b:
    diff -= c

  return (a + b + c) - diff

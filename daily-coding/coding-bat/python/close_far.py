# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

def close_far(a, b, c):

  ab_diff = abs(a - b)
  ac_diff = abs(a - c)
  bc_diff = abs(b - c)

  close_and_far = False

  # b is close, check if c is far
  if ab_diff <= 1:
    if ac_diff >= 2 and bc_diff >= 2:
      close_and_far = True
  # c is close, check if b is far
  if ac_diff <= 1:
    if ab_diff >= 2 and bc_diff >= 2:
      close_and_far =  True

  return close_and_far

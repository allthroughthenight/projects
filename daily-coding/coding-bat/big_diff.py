# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

def big_diff(nums):
  small = nums[0]
  big = 0
  for num in range(len(nums)):
    small = min(small,nums[num])
    big = max(big,nums[num])
  return abs(small - big)

# Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

def max_end3(nums):
  large = 0
  if nums[0] > nums[2]:
    large = nums[0]
  else:
    large = nums[2]

  array = [large, large, large]

  return array

# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

def has22(nums):
  length = len(nums)
  has22 = False

  for num in range(1, length-1):
    if nums[num] == 2:
      if nums[num-1] == 2 or nums[num+1] == 2:
        has22 = True
  if nums == [2 ,2]:
    has22 = True
  return has22

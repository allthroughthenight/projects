# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
  oneTwoThree = [1,2,3]
  search = []
  match = False
  for x in range(0,len(nums)-2):
    search = [nums[x],nums[x+1],nums[x+2]]
    if search == oneTwoThree:
      match = True

  return match

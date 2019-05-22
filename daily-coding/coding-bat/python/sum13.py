# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(nums):
  length = len(nums)
  total = 0

  for num in range(length):
    if length <= 0:
      break
    elif nums[num] == 13:
      total -= nums[num]
      if num+1 < length:
        total -= nums[num+1]
    total += nums[num]

  if total < 0:
    total = 0
  return total

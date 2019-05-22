# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

def sum67(nums):
  total = 0
  skip = False
  for num in nums:
    if num == 6 and skip == False:
      skip = True
    elif num == 7 and skip == True:
      skip = False
    elif skip == False:
      total += num

  return total

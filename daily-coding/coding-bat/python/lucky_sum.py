# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

def lucky_sum(a, b, c):
  nums = [a,b,c]
  sum = 0
  for num in nums:
    if num == 13:
      break
    sum += num
  return sum

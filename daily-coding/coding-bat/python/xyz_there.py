# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
  my_list = list(str)
  there = False
  for num in range(len(my_list) - 2):
    current = my_list[num] + my_list[num+1] + my_list[num+2]
    if current == 'xyz' and my_list[num-1] != '.':
      there = True
  return there

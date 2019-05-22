# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

def count_code(str):
  my_list = list(str)
  count = 0

  for num in range(len(my_list) - 3):
    if my_list[num:num+2] == ['c','o'] and my_list[num+3] == 'e':
      count += 1

  return count

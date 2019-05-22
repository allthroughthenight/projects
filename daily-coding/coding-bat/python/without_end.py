# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

def without_end(str):
  my_list = list(str)
  my_str = ''
  my_str = my_str.join(my_list[1:-1])
  return my_str

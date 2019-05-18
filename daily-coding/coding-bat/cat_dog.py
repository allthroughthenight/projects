# Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
  my_list = list(str)
  cat_dog = False
  cat_count = 0
  dog_count = 0

  for char in range(len(my_list)-2):
    if my_list[char] == 'c' and my_list[char+1] == 'a' and my_list[char+2] == 't':
      cat_count += 1
    if my_list[char] == 'd' and my_list[char+1] == 'o' and my_list[char+2] == 'g':
      dog_count += 1

  if cat_count - dog_count == 0:
    cat_dog = True

  return cat_dog

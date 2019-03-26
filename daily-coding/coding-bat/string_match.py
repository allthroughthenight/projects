# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
  listA = list(a)
  listB = list(b)
  listMin = 0
  match = 0

  if len(listA) < len(listB):
    listMin = len(listA)
  else:
    listMin = len(listB)

  for x in range(listMin-1):
    if listA[x] == listB[x] and listA[x+1] == listB[x+1]:
      match += 1

  return match

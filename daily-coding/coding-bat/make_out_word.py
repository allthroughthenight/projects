# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>". 

def make_out_word(out, word):
  split = list(out)
  
  front = ''
  front = front.join(split[0:2])
  
  back = ''
  back = back.join(split[2:4])
  
  return front + word + back

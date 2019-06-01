// We'll say that a number is "teen" if it is in the range 13..19 inclusive. Given 3 int values, return true if 1 or more of them are teen.

public boolean hasTeen(int a, int b, int c) {
  int[] teens = {a, b, c};
  boolean match = false;

  for(int teen = 0;teen < 3;teen++){
    if(teens[teen] >= 13 && teens[teen] <= 19){
      match = true;
    }
  }
  return match;
}

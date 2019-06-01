// We'll say that a number is "teen" if it is in the range 13..19 inclusive. Given 2 int values, return true if one or the other is teen, but not both.

public boolean loneTeen(int a, int b) {
  boolean teen = false;
  if(checkTeen(a) != checkTeen(b)){
    teen = true;
  }
  return teen;
}

public boolean checkTeen(int a){
  boolean teen = false;
    if(a >= 13 && a <= 19){
      teen = true;
    }
  return teen;
}

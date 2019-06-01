// Given 2 int values, return true if either of them is in the range 10..20 inclusive.

public boolean in1020(int a, int b) {
  boolean match = false;
  if(a >= 10 && a <=20){
    match = true;
  } else if(b >= 10 && b <=20){
    match = true;
  }
  return match;
}

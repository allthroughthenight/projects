// Given three int values, a b c, return the largest.

public int intMax(int a, int b, int c) {
  int big = 0;
  if (a > b && a > c){
    big = a;
  } else if (b > a && b > c){
    big = b;
  } else {
    big = c;
  }
  return big;
}

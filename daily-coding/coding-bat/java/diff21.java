// Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

public int diff21(int n) {
  int difference = 0;
  if (n > 21){
    difference = 2 * (-1 * (21 - n));
  } else {
    difference = 21 - n;
  }
  return difference;
}

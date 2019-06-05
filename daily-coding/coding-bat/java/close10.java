// Given 2 int values, return whichever value is nearest to the value 10, or return 0 in the event of a tie. Note that Math.abs(n) returns the absolute value of a number.

public int close10(int a, int b) {
  int diffA = Math.abs(a - 10);
  int diffB = Math.abs(b - 10);
  int close = 0;
  if(diffA < diffB){
    close = a;
  } else if(diffB < diffA){
    close = b;
  }
  return close;
}

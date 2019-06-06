// Given 2 positive int values, return the larger value that is in the range 10..20 inclusive, or return 0 if neither is in that range.

public int max1020(int a, int b) {
  int max = 0;
  int tempA = 0;
  int tempB = 0;

  // check if params are in range
  // if not then set to zero
  if(a >= 10 && a <= 20){
    tempA = a;
  }
  if(b >= 10 && b <= 20){
    tempB = b;
  }

  // compare and save result
  if(tempA >= tempB){
    max = tempA;
  } else {
    max = tempB;
  }

  return max;
}

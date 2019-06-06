// Given two non-negative int values, return true if they have the same last digit, such as with 27 and 57. Note that the % "mod" operator computes remainders, so 17 % 10 is 7.

public boolean lastDigit(int a, int b) {
  boolean match = false;
  String[] arrayA = Integer.toString(a).split("");
  String[] arrayB = Integer.toString(b).split("");

  if(arrayA[arrayA.length - 1].equals(arrayB[arrayB.length - 1])){
    match = true;
  }
  return match;
}

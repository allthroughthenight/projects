// Given 2 int values, return true if one is negative and one is positive. Except if the parameter "negative" is true, then return true only if both are negative.

public boolean posNeg(int a, int b, boolean negative) {
  boolean match = false;
  if (!negative) {
    if ((a < 0 && b > 0) || (a > 0 && b < 0)) {
      match = true;
    }
  } else if (a < 0 && b < 0) {
    match = true;
  }
  return match;
}

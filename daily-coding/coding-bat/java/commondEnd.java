// Given 2 arrays of ints, a and b, return true if they have the same first element or they have the same last element. Both arrays will be length 1 or more.

public boolean commonEnd(int[] a, int[] b) {
  int aEnd = a.length - 1;
  int bEnd = b.length - 1;
  boolean match = false;

  if(a[0] == b[0]){
    match = true;
  } else if (a[aEnd] == b[bEnd]){
    match = true;
  }

  return match;
}

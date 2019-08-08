// Given 2 int arrays, a and b, return a new array length 2 containing, as much as will fit, the elements from a followed by the elements from b. The arrays may be any length, including 0, but there will be 2 or more elements available between the 2 arrays.

public int[] make2(int[] a, int[] b) {
  int[] myArray = new int[2];

  int lenA = a.length;
  int lenB = b.length;
  int aLoop = 0;

  for(int i = 0; i < lenA && i < 2; i++){
    myArray[i] = a[i];
    aLoop++;
  }

  for(int i = 0; i < lenB && aLoop < 2; i++){
    myArray[aLoop] = b[i];
    aLoop++;
  }

  return myArray;
}

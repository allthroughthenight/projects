// Given 2 int arrays, a and b, of any length, return a new array with the first element of each array. If either array is length 0, ignore that array.

public int[] front11(int[] a, int[] b) {

  List<Integer> myList = new ArrayList<Integer>();

  if(a.length >= 1){
    myList.add(a[0]);
  }

  if(b.length >= 1){
    myList.add(b[0]);
  }

  int[] array = myList.stream().mapToInt(i->i).toArray();

  return array;
}

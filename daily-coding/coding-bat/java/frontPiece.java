// Given an int array of any length, return a new array of its first 2 elements. If the array is smaller than length 2, use whatever elements are present.

public int[] frontPiece(int[] nums) {
  int length = nums.length;
  int myArray[];
  if(length <= 2){
    myArray = nums;
  } else {
    myArray = Arrays.copyOfRange(nums, 0, 2);
  }
  return myArray;
}

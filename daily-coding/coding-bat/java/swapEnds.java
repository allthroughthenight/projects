// Given an array of ints, swap the first and last elements in the array. Return the modified array. The array length will be at least 1.

public int[] swapEnds(int[] nums) {
  int length = nums.length;
  int[] myArray = nums;
  int first = nums[0];

  myArray[0] = myArray[length - 1];
  myArray[length - 1] = first;

  return myArray;
}

// Given an int array, return a new array with double the length where its last element is the same as the original array, and all the other elements are 0. The original array will be length 1 or more. Note: by default, a new int array contains all 0's.

public int[] makeLast(int[] nums) {
  int length = nums.length * 2;
  int myArray[];
  myArray = new int[length];
  myArray[length - 1] = nums[nums.length - 1];
  return myArray;
}

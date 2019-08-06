// Given an array of ints of odd length, return a new array length 3 containing the elements from the middle of the array. The array length will be at least 3.

public int[] midThree(int[] nums) {
  int[] myArray = new int[3];
  int mid = nums.length/2;
  myArray[0] = nums[mid - 1];
  myArray[1] = nums[mid];
  myArray[2] = nums[mid + 1];
  return myArray;
}

// Given an array of ints, return true if the array is length 1 or more, and the first element and the last element are equal.

public boolean sameFirstLast(int[] nums) {
  int length = nums.length;
  boolean frontBack = false;
  if(length >= 1){
    if(nums[0] == nums[length -1]){
      frontBack = true;
    }
  }

  return frontBack;
}

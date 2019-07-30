// Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

public int sum2(int[] nums) {
  int length = nums.length;
  int total = 0;

  if(length == 0){
    // break
  }
  if(length == 1){
    total = nums[0];
  }
  if(length >= 2){
    total = nums[0] + nums[1];
  }

  return total;
}

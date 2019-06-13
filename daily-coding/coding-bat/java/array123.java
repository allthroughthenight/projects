// Given an array of ints, return true if the sequence of numbers 1, 2, 3 appears in the array somewhere.

public boolean array123(int[] nums) {
  int length = nums.length;
  boolean match = false;
  int sum = 0;

  for(int i = 0; i < length - 2;i++){
    sum = nums[i] + nums[i+1] + nums[i+2];
    if(sum == 6){
      match = true;
    }
  }
  return match;
}

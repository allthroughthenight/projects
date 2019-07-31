// Given an int array, return true if the array contains 2 twice, or 3 twice. The array will be length 0, 1, or 2.

public boolean double23(int[] nums) {
  boolean found = false;
  if(nums.length > 1){
    if(nums[0] == 2 && nums[1] == 2){
      found = true;
    } else if(nums[0] == 3 && nums[1] == 3){
      found = true;
    }
  }
  return found;
}

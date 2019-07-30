// Given an int array length 2, return true if it contains a 2 or a 3.

public boolean has23(int[] nums) {
  boolean found = false;
  if(nums[0] == 2 || nums[1] == 2){
    found = true;
  } else  if(nums[0] == 3 || nums[1] == 3){
    found = true;
  }

  return found;
}

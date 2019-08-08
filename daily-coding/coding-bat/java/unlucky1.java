// We'll say that a 1 immediately followed by a 3 in an array is an "unlucky" 1. Return true if the given array contains an unlucky 1 in the first 2 or last 2 positions in the array.

public boolean unlucky1(int[] nums) {
  int length = nums.length;
  boolean match = false;

  if(length < 2){
    // break
  } else {
    for(int i = 0; i < length - 1; i++){
      if((nums[i] == 1 && nums[i + 1] == 3)
      && (i < 2 || i > length - 3)){
        match = true;
      }
    }
  }
  return match;
}

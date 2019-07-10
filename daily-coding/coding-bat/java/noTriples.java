// Given an array of ints, we'll say that a triple is a value appearing 3 times in a row in the array. Return true if the array does not contain any triples.

public boolean noTriples(int[] nums) {
  int length = nums.length;
  boolean match = true;
  for(int i = 0; i < length -2; i++){
    if((nums[i] == nums[i+1]) && (nums[i+1] == nums[i+2])){
      match = false;
    }
  }
  return match;
}
// Given an array of ints, return the number of 9's in the array.

public int arrayCount9(int[] nums) {
  int length = nums.length;
  int count = 0;
  for(int i = 0;i < length;i++){
    if(nums[i]==9){
      count += 1;
    }
  }
  return count;
}

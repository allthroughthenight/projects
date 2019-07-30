// Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

public int[] maxEnd3(int[] nums) {
  int max = nums[0];
  int[] maxArr = {0,0,0};

  if(nums[0] < nums[2]){
      max = nums[2];
  }
  for(int i = 0; i < 3; i++){
    maxArr[i] = max;
  }

  return maxArr;
}

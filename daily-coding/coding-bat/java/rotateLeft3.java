// Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

public int[] rotateLeft3(int[] nums) {
  int[] myArr = nums;
  int last = nums[0];

  for(int i = 0; i < 2; i++){
    myArr[i] = nums[i+1];
  }
  myArr[2] = last;

  return myArr;
}

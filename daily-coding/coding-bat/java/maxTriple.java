// Given an array of ints of odd length, look at the first, last, and middle values in the array and return the largest. The array length will be a least 1.

public int maxTriple(int[] nums) {
  int first = nums[0];
  int middle = nums[nums.length/2];
  int last = nums[nums.length - 1];
  int largest = first;
  if(middle > largest){
    largest = middle;
  }
  if (last > largest){
    largest = last;
  }
  return largest;
}

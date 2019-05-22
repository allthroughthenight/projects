# Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

def sum2(nums):
    total = 0
    if len(nums) >= 2:
        total = nums[0] + nums[1]
    elif len(nums) >= 1:
        total = nums[0]

    return total


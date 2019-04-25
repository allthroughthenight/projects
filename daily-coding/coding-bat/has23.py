# Given an int array length 2, return True if it contains a 2 or a 3.

def has23(nums):
    found = False

    for num in nums:
        if num == 2 or num == 3:
            found = True

    return found

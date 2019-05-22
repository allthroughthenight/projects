# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().

def round_sum(a, b, c):
    total = 0
    nums = [a, b, c]

    for num in nums:
        total += round10(num)
    return total
    # ez mode built in function
    #for num in nums:
    #  total += round(num, -1)
    #return int(total)


def round10(num):
    rounded = 0
    left_over = num % 10
    if left_over < 5:
        rounded = num - left_over
    elif left_over >= 5:
        rounded = num - left_over + 10
    return rounded

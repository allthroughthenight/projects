# day10
# given a base-10 integer, n, convert it to binary (base-2).
# then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    # cast input as integer
    n = int(input())

    # get binary representation of input number
    binary = bin(n)

    # trim leading '0b' of binary notation
    binary = binary[2::]

    # repsentation of previous biniary digit
    previous = '0'
    # idk yet tbh
    consecutive = 0
    found = 0
    for x in binary:
        # if current digit is 1
        if x == '1':
            found += 1

            # set previously found digit as '1'
            previous = '1'
        # else 0
        else:
            # if current found is longer than consecutive, save
            if found > consecutive:
                consecutive = found
            # current is 0 so set
            previous = '0'
            # reset foudn
            found = 0
    # final check out side of if:else
    # in case our last found may be longer than our current inside if:else
    if found > consecutive:
        consecutive = found
    print(consecutive)

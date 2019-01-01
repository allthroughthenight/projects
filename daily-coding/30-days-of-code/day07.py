# day07
# given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n =  0
    # array size
    n = int(input())

    # delimit input items by 'space'
    # remove trailign white space
    # cast each item of type string to int
    # map items and list and assign
    arr = list(map(int, input().rstrip().split()))

    newString = ''

    # append items in reverse order to new string
    for x in range(1, n + 1):
        newString += str(arr[n - x])
        newString += " "
    print(newString)

# day05
# given an integer, n, print its first 10 multiples.
# each multiple n x i (where 1 <= i <= 10) should be printed on a new line in the form:
# n x i = result.

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    for x in range(1, 11):
        print("%d x %d = %d" % (n, x, n*x))

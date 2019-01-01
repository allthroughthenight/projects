# day03
# if n is odd, print weird
# if n is even and in the inclusive range of 2 to 5, print not weird
# if n is even and in the inclusive range of 6 to 20, print weird
# if n is even and greater than 20, print not weird

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    if (N % 2) > 0:                     # if not even print weird
        print("Weird")
    else:
        if (N <= 5) and (N >= 2):       # if between 2 to 5 inclusive
            print("Not Weird")
        elif (N <= 20) and (N >= 6):    # if between 6 to 20 inclusive
            print("Weird")
        elif (N > 20):                  # greater than 20
            print("Not Weird")

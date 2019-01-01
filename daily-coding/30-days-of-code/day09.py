# day09
# Write a factorial function that takes a positive integer N, as a parameter and prints the result of N(N factorial).

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    # if input is still valid
    if n > 1:
        # decrement and recursivley call function again
        n = n * factorial(n -1)
    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()


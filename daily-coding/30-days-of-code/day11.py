import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    # list of hour glass sums
    sumGlass = []

    # x i.e. row coordinate
    for x in range(0,4): 
        
        # y i.e. collumn coordinate
        for y in range(0,4):
            # pattern for top of hourglass
            top = arr[x][y:y+3]
            
            # pattern for middle of hourglass
            mid = arr[x+1][y+1:y+2]
            
            # pattern for bottom of hourglass
            bot = arr[x+2][y:y+3]

            # sum list and appened to 
            arr02.append(sum(top) + sum(mid) + sum(bot))
            
    # sort list from smallest to biggest
    arr02.sort()
    
    # print the last i.e. largest item i nthe list
    print(arr02[-1])

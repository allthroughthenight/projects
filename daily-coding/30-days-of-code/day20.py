import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swapCount = 0
for y in range(len(a)):
    for x in range(n-1):
        if a[x] > a[x+1]:
            temp = a[x]
            a[x] = a[x+1]
            a[x+1] = temp
            swapCount += 1

print("Array is sorted in {} swaps.".format(swapCount))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))

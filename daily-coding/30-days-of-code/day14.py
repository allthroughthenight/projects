class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        sortTemp = self.__elements
        sortTemp.sort()
        self.maximumDifference = sortTemp[-1] - sortTemp[0]

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

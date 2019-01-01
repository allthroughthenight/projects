import sys
debug = False
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class Solution:
    # Write your code here
    def __init__(self):
        self.queueHead = None
        self.queueTail = None
        self.stackHead = None

    def enqueueCharacter(self,data):
        newNode = Node(data)
        if self.queueHead == None:
            self.queueHead = newNode
            self.queueTail = newNode
        if debug: print("queue: {}".format(newNode.data))
        current = self.queueTail
        current.prev = newNode
        newNode.next = current
        self.queueTail = newNode

    def pushCharacter(self,data):
        newNode = Node(data)
        if debug: print("push: {}".format(newNode.data))
        if self.stackHead == None:
            self.stackHead = newNode
        current = self.stackHead
        current.next = newNode
        newNode.prev = current
        self.stackHead = newNode

    def popCharacter(self):
        char = self.stackHead.data
        current = self.stackHead
        self.stackHead = current.prev
        if debug: print("pop: {}".format(current.data))
        return char

    def dequeueCharacter(self):
        char = self.queueHead.data
        current = self.queueHead
        self.queueHead = current.prev
        if debug: print("dequeue: {}".format(current.data))
        return char
# read the string s
s=input()
#Create the Solution class object
obj=Solution()

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data):
    #Complete this method
        # make new node to be inserted
        newNode = Node(data)

        # if the list is empty then set head reference
        if head == None:
            head = newNode
        else:
            # make temp reference from head for position in the list
            current = head

            # keep going till we reach the end of the list
            while current.next != None:

                # set current node to it's neighbor/next node
                current = current.next

            # since current's node neighbor/next is 'None', then set current's
            # poitner to the new node i.e. append/insert it
            current.next = newNode
        return head
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);

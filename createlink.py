class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
#iterative traversal 
temp = head
while temp:
    print(temp.data)
    temp = temp.next
"""
#temp.next method used for operations for last element
temp = head
while temp.next:
    print(temp.data)
    temp = temp.next
"""
"""
Traversal → use while temp:
Finding last node → use while temp.next:

"""
    
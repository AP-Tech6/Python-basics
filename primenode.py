class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next != None:
            temp = temp.next

        temp.next = new_node

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    def primeno(self, data):
        if data < 2:
            return
        for i in range(2, data):
            if data % i == 0:
                return
        self.append(data)

    def primeadd(self):
        temp = self.head
        s = 0

        while temp:
            s += temp.data
            temp = temp.next

        return s


ll = LinkedList()

n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter number: "))
    ll.primeno(num)

ll.display()
print("Sum of prime nodes:", ll.primeadd())
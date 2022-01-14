class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def skipMdeleteN(self, M, N):
        curr = self.head

        while(curr):

            for count in range(1, M):
                if curr is None:
                    return
                curr = curr.next

            if curr is None:
                return

            t = curr.next
            for count in range(1, N+1):
                if t is None:
                    break
                t = t.next

            curr.next = t

            curr = t


llist = LinkedList()
M = 3
N = 4
for i in range(int(input("Enter range:"))):
    llist.push(i)

print("M = %d, N = %d\nGiven Linked List is:" % (M, N))
llist.printList()
print

llist.skipMdeleteN(M, N)

print("\nLinked list after deletion is")
llist.printList()

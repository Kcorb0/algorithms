# Singly linked list implementation
import random as rd


class Node:
    # Constructer with one data element and the next node reference
    def __init__(self, data, next=None):

        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if self.head:
            current = self.head

            # Cycling through nodes until there is no reference
            while current.next:
                current = current.next

            current = new_node

        else:
            self.head = new_node

    def printll(self):
        current = self.head

        while current.next:
            print(current)
            current = current.next


test_ll = LinkedList()
test_ll.add(2)
test_ll.add(3)
test_ll.add(5)
test_ll.add(7)
test_ll.add(9)
test_ll.add(11)

print(test_ll.printll())

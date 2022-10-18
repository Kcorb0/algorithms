# Singly linked list implementation
import random as rd


class Node:
    # Constructer with one data element and the next node reference
    def __init__(self, data, next=None):

        self.data = data
        self.next = next


n1 = Node(5)

print(n1.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = data

        if self.head != None:
            current = self.head

            while current.next != None:
                current.next = new_node

            current.next = new_node

        else:
            self.head = new_node

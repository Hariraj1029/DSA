class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data): # insert at the beginning
        node = Node(data)
        if self.head is None: # if list is empty
            self.head = node    # insert at the beginning
            node.next = self.head   # make the node circular
        else:                  # if list is not empty
            node.next = self.head # insert at the beginning
            self.head = node    # change the head
            last = self.head     # find the last node in the list
            while last.next != self.head: # last node's next is head of the list
                last = last.next    # iterate over the list
            last.next = self.head # make the list circular

    def insert_back(self, data): # insert at the end
        node = Node(data)
        if self.head is None: # if list is empty
            self.head = node    # insert at the beginning
            node.next = self.head # make the node circular
        else:               # if list is not empty
            last = self.head    # find the last node in the list
            while last.next != self.head:   # last node's next is head of the list
                last = last.next    # iterate over the list
            last.next = node    # insert at the end
            node.next = self.head   # make the node circular

    def insert_at(self, data, index):   # insert at a specific index
        node = Node(data)   # create a new node
        if index == 0:  # if the index is 0
            node.next = self.head   # insert at the beginning of the list
            self.head = node    # change the head
            last = self.head    # find the last node in the list
            while last.next != self.head:   # last node's next is head of the list
                last = last.next    # iterate over the list
            last.next = self.head   # make the list circular
        else:            # if the index is not 0
            i = 0    # initialize i to 0
            current = self.head   # initialize current to head
            while i < index-1:  # iterate over the list until i reaches the position before the index
                current = current.next  # iterate over the list 
                i += 1  
            node.next = current.next   # insert at the index                          
            current.next = node   # change the next of the previous node

    def delete_at(self, index):  # delete at a specific index
        if index == 0: # if the index is 0 
            self.head = self.head.next    # delete at the beginning of the list
            last = self.head       # find the last node in the list
            while last.next != self.head: # last node's next is head of the list
                last = last.next   # iterate over the list
            last.next = self.head  # make the list circular
        else:   # if the index is not 0
            i = 0
            node = self.head        # initialize node to head
            while i < index-1:  # iterate over the list until i reaches the position before the index
                node = node.next      # iterate over the list
                i += 1
            node.next = node.next.next   # delete at the index by skiping the element

    def print(self):
        node = self.head
        while node.next != self.head:
            print(node.data)
            node = node.next
        print(node.data)

    def delete(self, data):
        node = self.head
        if node.data == data:
            self.head = self.head.next
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = self.head
        else:
            while node.next != self.head:
                if node.next.data == data:
                    node.next = node.next.next
                    break
                node = node.next
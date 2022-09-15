class Node: # Node class
    def __init__(self, data, next=None): 
        self.data = data  # data
        self.next = next  # next node

class LinkedList: # LinkedList class
    def __init__(self):
        self.head = None # head of list

    def insert_front(self, data): # insert at the beginning
        node = Node(data)
        if self.head is None: # if list is empty
            self.head = node 
        else:                   # if list is not empty
            node.next = self.head
            self.head = node

    def insert_back(self,data): # insert at the end
        node = Node(data)
        if self.head is None: # if list is empty
            self.head = node 
        else:                  # if list is not empty
            last = self.head
            while last.next: # find the last node in the list (last node's next is None)
                last = last.next 
            last.next = node # insert at the end
    
    def insert_at(self, data, index): # insert at a specific index
        node = Node(data)
        if index == 0: # if the index is 0
            node.next = self.head # insert at the beginning of the list
        else:                     # if the index is not 0
            i = 0 # current index
            current = self.head  # current node
            while i < index-1: # iterate over the list until the previous of index is reached
                current = current.next 
                i += 1 
            node.next = current.next # insert at the index 
            current.next = node 

    def delete_at(self, index): # delete at a specific index
        if index == 0: # if the index is 0
            self.head = self.head.next # change the head
        else:
            i = 0
            node = self.head
            while i < index-1: # iterate over the list until the previous of index is reached
                node = node.next
                i += 1
            node.next = node.next.next # delete at the index


    def print(self): # print the list
        node = self.head 
        while node is not None: # iterate over the list
            print(node.data)  # print the data
            node = node.next # go to the next node

    def delete(self, data): # delete a node
        node = self.head 
        if node.data == data: # if the node is the head
            self.head = node.next # change the head
            return 
        while node is not None: # iterate over the list if the node is not the head
            if node.next.data == data: # if the next node is the one to delete
                node.next = node.next.next # skip the node to delete
                return
            node = node.next # go to the next node

    def reverse(self): # reverse the list
        node = self.head  # current node
        prev = None # previous node
        while node is not None: # iterate over the list
            next = node.next # save the next node
            node.next = prev # change the next node
            prev = node # change the previous node
            node = next # change the current node
        self.head = prev # change the head

ll = LinkedList()
ll.head = Node(1)
print(ll.head.data)
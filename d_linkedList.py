class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.previous = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.previous = cur
            new_node.next = None
    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.previous = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.previous = None
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.previous = cur
                new_node.next = nxt
                nxt.previous = new_node
            cur = cur.next
    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.previous is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.previous
                prev.next = new_node
                new_node.previous = prev
                new_node.next = cur
                cur.previous = new_node
            cur = cur.next
    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # Case 1
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                # Case 2
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.previous = None
                    cur = None
                    self.head = nxt
                    return
            elif cur.data == key:
                # Case 3
                if cur.next:
                    nxt = cur.next
                    prev = cur.previous
                    prev.next = nxt
                    nxt.previous = prev
                    cur.next = None
                    cur.previous = None
                    cur = None
                    return
                # Case 4
                else:
                    prev = cur.previous
                    prev.next = None
                    cur.previous = None
                    cur = None
                    return
            cur = cur.next
    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.previous
            cur.previous = cur.next
            cur.next = tmp
            cur = cur.previous
        if tmp:
            self.head = tmp.previous
dlist = doublyLinkedList()
dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.append(4)
dlist.prepend(0)
dlist.print_list()
print(" ")
dlist.add_after_node(2, 5)
dlist.print_list()
print(" ")
dlist.add_before_node(2, 6)
dlist.print_list()
print(" ")
dlist.delete(6)
dlist.print_list()
print(" ")
dlist.reverse()
dlist.print_list()

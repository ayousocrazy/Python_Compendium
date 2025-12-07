"""
Linked List Implementation
implement:
    insert_head
    insert_tail
    delete_value
    search
    display

Without any built-in list.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        if head is not None:
            self.head = Node(head)
        else:
            self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        s = self.head
        while s.next:
            s = s.next
        s.next = new_node

    def delete_value(self, data):
        if not self.head:
            return

        while self.head and self.head.data == data:
            self.head = self.head.next
        
        s = self.head
        while s and s.next:
            if s.next.data == data:
                s.next = s.next.next
            else:
                s = s.next

    def search(self, data):
        s = self.head
        while s:
            if s.data == data:
                return s
            s = s.next
        return None

    def display(self):
        if self.head:
            s = self.head
            while s:
                print(f"{s.data} ->", end="")
                s = s.next
        print(None)

# TESTS
l = LinkedList(10)
l.display()

l.insert_head(20)
l.display()

l.insert_tail(30)
l.display()
l.insert_tail(30)
l.display()
l.insert_tail(30)
l.display()

l.delete_value(30)
l.display()

print(l.search(10))
print(l.search(20))
print(l.search(30))
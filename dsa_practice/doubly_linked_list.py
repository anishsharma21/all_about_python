class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    
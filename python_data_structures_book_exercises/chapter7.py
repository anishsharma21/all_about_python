class Empty(Exception):
    pass

class LinkedStack:
    class Node:
        __slots__ = 'value', 'next'
        def __init__(self, value, next):
            self.value = value
            self.next = next
            
    def __init__(self, head=None):
        self.size = 0
        self.head = head
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, value):
        self.head = self.Node(value, self.head)
        self.size += 1
        
    def top(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self.head.value

    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty')
        top = self.head.value
        self.head = self.head.next
        self.size -= 1
        return top
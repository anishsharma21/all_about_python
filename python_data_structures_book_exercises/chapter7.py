class Empty(Exception):
    pass

class LinkedStack:
    class Node:
        __slots__ = '_value', '_next'
        def __init__(self, _value, _next):
            self._value = _value
            self._next = _next
            
    def __init__(self, head=None):
        self.size = 0
        self.head = head
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, _value):
        self.head = self.Node(_value, self.head)
        self.size += 1
        
    def top(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self.head._value

    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty')
        top = self.head._value
        self.head = self.head._next
        self.size -= 1
        return top

class LinkedQueue:
    class Node:
        __slots__ = '_value', '_next'
        def __init__(self, _value, _next):
            self._value = _value
            self._next = _next
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self.head._value
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('queue is empty')
        first = self.head._value
        self.head = self.head._next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return first
    
    def enqueue(self, value):
        tail = Node(value, None)
        if self.is_empty():
            self.head = tail
        else:
            self.tail._next = tail
        self.tail = tail
        self.size += 1
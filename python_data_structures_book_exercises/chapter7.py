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
        tail = self.Node(value, None)
        if self.is_empty():
            self.head = tail
        else:
            self.tail._next = tail
        self.tail = tail
        self.size += 1

class CircularQueue:
    class Node:
        __slots__ = '_value', '_next'
        def __init__(self, value, next):
            self._value = value
            self._next = next
    
    def __init__(self):
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def first(self):
        return self.tail._next
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('queue is empty')
        oldhead = self.tail._next
        if self.size == 1:
            self.tail = None
        else:
            self.tail = oldhead._next
        self.size -= 1
        return oldhead

    def enqueue(self, value):
        new_tail = self.Node(value, None)
        if self.is_empty():
            new_tail._next = new_tail
            self.tail = new_tail
        else:
            new_tail._next = self.tail._next
            self.tail._next = new_tail
        self.tail = new_tail
        self.size += 1
    
    def rotate(self):
        if self.is_empty():
            raise Empty('queue is empty')
        self.tail = self.tail._next

class _DoublyLinkedBase:
    class _Node:
        __slots__ = '_element', '_prev', '_next'
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
    
    def __init__(self):
        self._header, self._trailer = _Node(None, None, None), _Node(None, None, None)
        self._header._next, self._trailer._prev= self._trailer, self._header
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        new = _Node(e, predecessor, successor)
        predecessor._next, successor._prev = new, new
        self._size += 1
        return new
    
    def _delete_node(self, node):
        predecessor, successor = node._prev, node._next
        predecessor._next, successor._prev = successor, predecessor
        self._size -= 1
        e = node._element
        node._prev = node._next = node._element = None
        return e

class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self._header._next._element
    
    def last(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self._trailer._prev._element
    
    def insert_first(self, e):
        return self._insert_between(e, self._header, self._header._next)
    
    def insert_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def delete_first(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self._delete_node(self._trailer._prev)

class PositionalList(_DoublyLinkedBase):
    class Position:
        __slots__ = '_container', '_node'
        def __init__(self, container, node):
            self._container = container
            self._node = node
        
        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            return type(self) is type(other) and self._node is other._node

        def __ne__(self, other):
            return not (self == other)
    
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        return self.Position(self, node)
    
    def first(self):
        return self._make_position(self._header._next)
    
    def last(self):
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
            
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)
    
    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)
    
    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    
    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)
    
    def replace(self, p, e): #smart
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
    
def insertion_sort(L):
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)

def insertion_sort(data: list) -> list:
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
        
data = [2, 1, 4, 3, -5]
insertion_sort(data)
print(data)

def sqrt(x):
    l, r = 0, x
    res = 0
    while l <= r:
        mid = l + ((r - l) // 2)
        if mid * mid > x:
            r = mid - 1
        elif mid * mid < x:
            l = mid + 1
            res = mid
        else:
            return mid
    return res

print(sqrt(5))
print(sqrt(12))
print(sqrt(16))


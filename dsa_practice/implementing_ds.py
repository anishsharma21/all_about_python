class _DoublyLinkedBase:
    class Node:
        __slots__ = '_element', '_prev', '_next'
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
        
    def __init__(self):
        self._header = self.Node(None, None, None)
        self._trailer = self.Node(None, None, None)
        self._header._next, self._trailer._next = self._trailer, self._header
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        new = self.Node(e, predecessor, successor)
        predecessor._next = new
        successor._prev = new
        self._size += 1
        return new
    
    def _delete_node(self, node):
        predecessor, successor = node._prev, node._next
        predecessor._next, successor._prev = successor, predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


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

class PositionalList(_DoublyLinkedBase):
    class Position:
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
            raise TypeError('not a valid Position object')
        if p._container is not self:
            raise ValueError('position does not belong to this PositionalList')
        if p._node._next is None:
            raise ValueError('position is no longer valid')
        return p._node
    
    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        return self.Position(self, node)
    
    def first(self):
        return _make_position(self._header._next)
    
    def last(self):
        return _make_position(self._trailer._prev)
    
    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        cur = self.first()
        while cur:
            yield cur.element()
            cur = seld.after(cur)


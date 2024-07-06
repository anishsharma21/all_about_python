def skip():
    class Empty(Exception):
        pass

    class ArrayStack:
        def __init__(self):
            self._data = []
            
        def __len__(self):
            return len(self._data)
        
        def is_empty(self):
            return len(self._data) == 0
        
        def push(self, e):
            self._data.append(e)
            
        def top(self):
            if self.is_empty():
                raise Empty('stack is empty')
            return self._data[-1]
        
        def pop(self):
            if self.is_empty():
                raise Empty('stack is empty')
            self._data.pop()

    def is_matching(expr):
        stack = []
        matches = {'[': ']', '(': ')', '{': '}'}
        for c in expr:
            if c in matches:
                stack.append(c)
            elif c in matches.values():
                if len(stack) == 0:
                    return False
                elif matches[stack[-1]] != c:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0

    string = '[(5+x)-(y+z)]'
    string2 = '[(5+x)-(y+z]'
    print(is_matching(string))
    print(is_matching(string2))

    def romanToInt(self, s: str) -> int:
        mappings = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integer = 0
        for i in range(len(s)):
            value = mappings[s[i]]
            if i < len(s) - 1:
                if value < mappings[s[i+1]]:
                    integer -= value
                    continue
            integer += value
        return integer

    def longestCommonPrefix(strs):
        smallest = min(strs, key=len)
        print(smallest)
        strs.pop(strs.index(smallest))
        return ''.join([smallest[c] for c in range(len(smallest)) for w in range(len(strs)) if smallest[c] != strs[w][c]])

    print(longestCommonPrefix(['flower', 'flow', 'flight']))

    string = 'haystack'
    print(string[0:3])


    def addBinary(a: str, b: str) -> str:
        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            s.append(str(carry % 2))
            carry //= 2

        return ''.join(reversed(s))

    class ArrayQueue:
        def __init__(self, capacity=10):
            self._size = 0
            self._data = [None] * capacity
            self._head = 0
            
        def __len__(self):
            return self._size
        
        def is_empty(self):
            return self._size == 0
        
        def get_head(self):
            if self.is_empty():
                raise Empty('queue is empty')
            return self._data[self._head]
        
        def dequeue(self):
            if self.is_empty():
                raise Empty('queue is empty')
            answer = self._data[self._head]
            self._data[self._head] = None
            self._head = (self._head + 1) % len(self._data)
        
        def resize(self, cap):
            copy = self._data
            self._data = [None] * cap
            walk = self._head
            for k in range(self._size):
                self._data[k] = copy[walk]
                walk = (walk + 1) % len(copy)
            self._head = 0

    def sqrt(x):
        low = 1
        high = x
        vals = set()
        while low < high:
            mid = (low + high) // 2
            if mid in vals:
                return mid
            if mid * mid == x:
                return mid
            if mid * mid < x:
                low = mid
            else:
                high = mid
            vals.add(mid)
        return mid

    print(sqrt(8))
    
def transfer(s, t):
    for element in s:
        t.push(s.pop(element))
    return t

class ArrayStack:
    def __init__(self, cap=4):
        self._size = 0
        self._data = [None] * cap
     
    def is_empty(self):
        return len(self) == 0
    
    def __len__(self):
        return self._size
    
    def push(self, e):
        if self._size >= len(self._data):
            self.resize(self._size * 2)
        self._data[self._size] = e
        self._size += 1
    
    def pop(self):
        if self.is_empty():
            raise Exception('stack is empty')
        if self._size < int(0.25 * len(self._data)):
            self.resize(len(self._data) // 2)
        r = self._data[self._size - 1]
        self._data[self._size] = None
        self._size -= 1
        return r
    
    def resize(self, cap):
        old = self._data
        self._data = [None] * cap
        for k in range(self._size):
            self._data[k] = old[k]
        old = None

# Existing code for context
s = ArrayStack()
print(len(s))  # Should print 0
print(s.is_empty())  # Should print True

# Additional print statements for testing
s.push(10)
print(len(s))  # Should print 1
print(s.is_empty())  # Should print False

s.push(20)
print(len(s))  # Should print 2

s.push(30)
print(len(s))  # Should print 3

s.push(40)
print(len(s))  # Should print 4

s.push(50)
print(len(s))  # Should print 5, triggers resize

print(s.pop())  # Should print 50
print(len(s))  # Should print 4

print(s.pop())  # Should print 40
print(len(s))  # Should print 3

print(s.pop())  # Should print 30
print(len(s))  # Should print 2, triggers resize

print(s.pop())  # Should print 20
print(len(s))  # Should print 1

print(s.pop())  # Should print 10
print(len(s))  # Should print 0

# Trying to pop from an empty stack
try:
    s.pop()
except Exception as e:
    print(e)  # Should print 'stack is empty'

# Pushing again after popping everything
s.push(60)
print(len(s))  # Should print 1
print(s.is_empty())  # Should print False

s.push(70)
print(len(s))  # Should print 2
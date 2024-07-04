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
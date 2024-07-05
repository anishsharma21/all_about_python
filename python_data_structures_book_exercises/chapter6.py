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
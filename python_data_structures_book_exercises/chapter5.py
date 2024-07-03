import sys
import ctypes

def skip():
    n = 10
    data = []
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print(f"Number of items in list: {a} | Size of list in bytes: {b} bytes")
        data.append(None)

class DynamicArray:
    def __init__(self, capacity=1):
        self._n = 0
        self._capacity = capacity
        self._array = self._make_array(self._capacity)
    
    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()
    
    def __len__(self):
        return self._n
    
    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError(f"invalid index: {k}")
        return self._array[k]
    
    def append(self, value):
        if self._n == self._capacity:
            self.resize(self._capacity * 2)
        self._array[self._n] = value
        self._n += 1

    def resize(self, new_capacity):
        new_arr = self._make_array(new_capacity)
        for k in range(self._n):
            new_arr[k] = self._array[k]
        self._array = new_array
        self._capacity = new_capacity

class GameEntry:
    def __init__(self, score, name):
        self._score = score
        self._name = name
    
    def get_score(self):
        return self._score

    def get_name(self):
        return self._name
    
    def __str__(self):
        return f"{self._name}: {self._score}"

class Scoreboard:
    def __init__(self, capacity=10):
        self._n = 0
        self._board = [None] * capacity
    
    def __getitem__(self, k):
        if not 0 <= k < len(self._board):
            raise IndexError('invalid index')
        return self._board[k]
    
    def __str__(self):
        return '\n'.join(str(entry) for entry in self._board)
    
    def add(self, entry):
        score = entry.get_score()
        good = n < len(self._board) or score > self._board[-1].get_score()
        if good:
            if self._n < len(self._board):
                self._n += 1
            j = self._n - 1
            while j > 0 and self.board [j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry

count = 0
def insertion_sort(arr):
    for i in range(1, len(arr)):
        base = i
        track = i - 1
        while track >= 0:
            global count
            count += 1
            if arr[base] < arr[track]:
                arr[base], arr[track] = arr[track], arr[base]
                base -= 1
            else:
                break
            track -= 1

my_arr = [2, 1, 4, 3, 9, 0, -5]
insertion_sort(my_arr)
print(my_arr)
print(count)

class CaesarCipher:
    def __init__(self, shift):
        self._backward = ''.join([chr((k + shift) % 26+ ord('A')) for k in range(26)])
        self._forward = ''.join([chr((k - shift) % 26 + ord('A')) for k in range(26)])
    
    def encrypt(self, secret):
        return self._transform(secret, self._forward)
    
    def decrypt(self, secret):
        return self._transform(secret, self._backward)
    
    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)

cipher = CaesarCipher(3)
message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
coded = cipher.encrypt(message)
print(f"Encrypted message: {coded}")
decoded = cipher.decrypt(coded)
print(f"Decrypted message: {decoded}")

        
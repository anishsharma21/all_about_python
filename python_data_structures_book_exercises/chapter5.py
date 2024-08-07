import sys
import ctypes
from random import randint
from time import time

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

    r, c, = 3, 3
    data = [[' '] * c for _ in range(r)]
    print(data)

    class TicTacToe:
        def __init__(self):
            self._board = [[' '] * 3 for _ in range(3)]
            self._player = 'X'
        
        def mark(self, i, j):
            if not (0 <= i <= 2 and 0 <= j <= 2):
                raise ValueError('invalid position')
            if self._board[i][j] != ' ':
                raise ValueError('board position occupied')
            self._board[i][j] = self._player
            if self._player == 'X':
                self._player = 'O'
            else:
                self._player = 'X'
        
        def _is_winner(self, mark):
            board = self._board
            return (mark == board[0][0] == board[0][1] == board[0][2] or mark == board[1][0] == board[1][1] == board[1][2] or mark == board[2][0] == board[2][1] == board[2][2] or mark == board[0][0] == board[1][0] == board[2][0] or mark == board[1][0] == board[1][1] == board[1][2] or mark == board[2][0] == board[2][1] == board[2][2] or mark == board[0][0] == board[1][1] == board[2][2] or mark == board[2][0] == board[1][1] == board[0][2])
        
        def winner(self):
            for mark in 'XO':
                if self._is_winner(mark):
                    return mark
            return None
        
        def __str__(self):
            rows = ['|'.join(row) for row in self._board]
            return '\n-----\n'.join(rows)

    game = TicTacToe()
    game.mark(1, 1)
    game.mark(0, 0)
    game.mark(1, 0)
    game.mark(1, 2)
    game.mark(0, 2)
    game.mark(2, 1)
    game.mark(2, 0)
    print(game.winner())
    print(str(game))

    last_size = 0
    data = []
    for k in range(1, 100):
        size = sys.getsizeof(data)
        if size != last_size:
            last_size = size
            print(f"Number of elements: {len(data)}, Size in bytes: {size}")
        data.append(None)
    for k in range(1, 100):
        size = sys.getsizeof(data)
        if size != last_size:
            last_size = size
            print(f"Number of elements: {len(data)}, Size in bytes: {size}")
        data.pop()

    class DynamicArray:
        def __init__(self, capacity=1):
            self._n = 0
            self._capacity = capacity
            self._array = self._make_array(self._capacity)
        
        def _make_array(self, capacity):
            return (capacity * ctypes.py_object)()
        
        def __len__(self):
            return self._n
        
        def __getitem__(self, k): # accounts for negative indices
            if not k < self._n or k < 0 and not k + self._n >= 0:
                raise IndexError(f"invalid index: {k}")
            if k < 0:
                k += self._n
            return self._array[k]
        
        def append(self, value):
            if self._n == self._capacity:
                self.resize(self._capacity * 2)
            self._array[self._n] = value
            self._n += 1
        
        def pop(self):
            self._n -= 1
            if self._n < 0.25 * self._capacity:
                self.resize(self._capacity // 2)

        def resize(self, new_capacity):
            new_arr = self._make_array(new_capacity)
            for k in range(self._n):
                new_arr[k] = self._array[k]
            self._array = new_array
            self._capacity = new_capacity

    data = [[randint(1, 10)] * 5 for _ in range(5)]
    print(sum([sum(row) for row in data]))

    last_size = 0
    data = []
    for k in range(1, 100):
        size = sys.getsizeof(data)
        if size != last_size:
            last_size = size
            print(f"Number of elements: {len(data)}, Size in bytes: {size}")
        data.append(randint(1, 100))
    print()
    last_size = 0
    data = []
    for k in range(1, 100):
        size = sys.getsizeof(data)
        if size != last_size:
            last_size = size
            print(f"Number of elements: {len(data)}, Size in bytes: {size}")
        data.append(None)

    string = ''
    time_initial = time()
    for i in range(1000):
        string += 'a'
    time_final = time()
    print(time_final - time_initial)

    string_list = []
    time_initial = time()
    for i in range(1000):
        string_list.append('a')
    string = ''.join(string_list)
    time_final = time()
    print(time_final - time_initial)

    time_initial = time()
    string = ''.join(['a' for _ in range(1000)])
    time_final = time()
    print(time_final - time_initial)

    time_initial = time()
    string_generator = ''.join('a' for _ in range(1000))
    time_final = time()
    print(time_final - time_initial)



import random
import math
import itertools
import os
import time
import numpy as np

def skip():
    random_int = random.random()
    print(random_int)
    random_int = random.randint(1, 6)
    print(random.randrange(1, 10, 2))
    print(random.choice([1, 5, 6, 3, 44, 2, 3]))

    def is_multiple(n, m):
        return True if m % n == 0 else False
    print(is_multiple(2, 4))
    print(is_multiple(2, 5))
    print(is_multiple(6, 48))
    print(is_multiple(6, 4))

    def is_even(k):
        return True if k % 2 == 0 else False

    def minmax(data):
        minval = math.inf
        maxval = -math.inf
        for val in data:
            if val < minval:
                minval = val
            if val > maxval:
                maxval = val
        return minval, maxval

    print(minmax([1, 4, 5, 2, 4, 9, 3, 5]))

    def sum_of_squares(n):
        return sum([val**2 for val in range(n)])

    print(sum_of_squares(12))

    def sum_of_squares_odd(n):
        return sum([val**2 for val in range(1,n,2)])

    def reverse_data(data):
        for i in range(len(data) // 2):
            data[i], data[len(data) - 1 - i] = data[len(data) - 1 - i], data[i]
        return data


    def distinct_values(data):
        return True if len(set(data)) == len(data) else False


    def scale(data, factor):
        for n in range(len(data)):
            data[n] *= factor
        
    interesting_list = [val*(val-1) for val in range(1, 11)]
    print(interesting_list)

    alphabet = [chr(char) for char in range(97, 123)]
    print(alphabet)


    def shuffle(data):
        shuffled_data = []
        for _ in range(len(data)):
            idx = random.randint(0, len(data)-1)
            shuffled_data.append(data[idx])
            data.pop(idx)
        return shuffled_data

    default_list = [1, 2, 5, 8, 12, 17]
    print(shuffle(default_list))

    user_inputs = []
    while True:
        try:
            user_input = input("gonna keep asking for input: ")
            user_inputs.insert(0, user_input)
        except EOFError:
            print()
            for val in user_inputs:
                print(val, end=" ")
            break
        
    def dot_product(a, b):
        for i in range(len(a)):
            a[i] = a[i] * b[i]
        return a

    a = [1, 3, 5, 2, 3]
    b = [2, 5, 8, 1, 2]
    print(dot_product(a, b))
    
    my_list = [1, 2, 5, 6]
    try:
        my_list[5] = 3
        print(my_list)
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")

    def count_vowels(string):
        return len([char for char in string if char in ['a', 'e' ,'i', 'o', 'u']])
    print(count_vowels('python')) # 1
    print(count_vowels('anish')) # 2
    print(count_vowels('dracula')) # 3
    print(count_vowels('tbhh')) # 0

    def remove_punctuation(string: str): 
        punctuation = [',', '.', "'", '"', ';']
        for punc in punctuation:
            string.replace(punc, '')

    def fibonacci():
        a = 0
        b = 1
        while True:
            yield a
            future = a + b
            a = b
            b = future

    fib_gen = fibonacci()
    for _ in range(10):
        print(next(fib_gen))

    def p_norm(v, p):
        totalsum = sum([val**p for val in v])
        print(totalsum)
        root_p = totalsum ** (1/p)
        return root_p

    vectors = [1, 2, 3, 4, 5]
    p = 2
    p_norm_val = p_norm(vectors, p)
    print(p_norm_val)

def generate_permutations(chars, current=''):
    if len(chars) == 0:
        print(current)
    else:
        for i in range(len(chars)):
            new_chars = chars[:i] + chars[i+1:]
            new_current = current + chars[i]
            generate_permutations(new_chars, new_current)

    generate_permutations('catdog')

    characters = 'catdog'
    all_permutations = itertools.permutations(characters, len(characters))
    for perm in all_permutations:
        print(''.join(perm))

    def find_maximum_divisions_by_2(n):
        if n < 2:
            return 0
        divided_by_2 = n / 2
        return 1 + find_maximum_divisions_by_2(divided_by_2)

    print(find_maximum_divisions_by_2(55))

    forms_of_exchange = [0.05, 0.10, 0.20, 0.5, 1, 2, 5]
    def make_change(charged, given):
        diff = round(given - charged, 2)
        if diff < 0:
            return {}
        change = {}
        for coin in reversed(forms_of_exchange):
            if diff >= coin:
                times = diff // coin
                change[coin] = int(times)
                diff -= coin * times
                if not diff:
                    return change
        if not diff:
            return change
        return {}

    print(make_change(5, 18.65))

    def find_counts(sentence):
        words = sentence.split(' ')
        word_counts = {}
        for word in words:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
        return word_counts

    user_input = input("Sentence: ")
    print(find_counts(user_input))

    class Flower:
        def __init__(self, name: str='flower', num_petals: int=5, price: float=5.0):
            self.name = name
            self.num_petals = num_petals
            self.price = price
            
    class Vector:
        """Represent a vector in a multidimensional space."""
        def __init__(self, d):
            self._coords = [0] * d
        
        def __len__(self):
            return len(self._coords)
        
        def __getitem__(self, j):
            return self._coords[j]

        def __setitem__(self, j, val):
            self._coords[j] = val
        
        def __add__(self, other):
            if len(self) != len(other):
                raise ValueError('dimensions must agree')
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] + other[j]
            return result
        
        def __eq__(self, other):
            return self._coords == other._coords
        
        def __ne__(self, other):
            return not self == other
        
        def __str__(self):
            return '<' + str(self._coords)[1:-1] + '>'

        def __sub__(self, other):
            if len(self) != len(other):
                raise ValueError('dimensions must agree')
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] - other[j]
            return result

        def __neg__(self):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = -self[j]
            return result

    v1 = Vector(3)
    v2 = Vector(3)

    v1.__setitem__(0, 1)
    v1.__setitem__(1, 4)
    v1.__setitem__(2, -2)
    v2.__setitem__(0, 4)
    v2.__setitem__(1, 2)
    v2.__setitem__(2, 9)
    print(str(v1))
    print(str(v2))

    print(v1 - v2)
    print(-v1)

    def initialize_board(n):
        return np.random.choice([0, 1], size=(n, n))

    def print_board(board):
        os.system('clear' if os.name == 'posix' else 'cls')
        for row in board:
            print(' '.join('■' if cell else ' ' for cell in row))

    def count_neighbors(board, x, y):
        n = len(board)
        return sum(board[(x + i) % n][(y + j) % n] for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0))

    def update_board(board):
        new_board = np.copy(board)
        n = len(board)
        for x in range(n):
            for y in range(n):
                neighbors = count_neighbors(board, x, y)
                if board[x][y] and not 2 <= neighbors <= 3:
                    new_board[x][y] = 0
                elif not board[x][y] and neighbors == 3:
                    new_board[x][y] = 1
        return new_board

    def game_of_life(n=20, generations=100, sleep_time=0.1):
        board = initialize_board(n)
        for _ in range(generations):
            print_board(board)
            board = update_board(board)
            time.sleep(sleep_time)

    if __name__ == "__main__":
        game_of_life()

    start_time = time.time()
    for _ in range(100000):
        pass
    end_time = time.time()
    print(end_time - start_time)

    my_list = [val for val in range(10000000)]
    start_time = time.time()
    print(max(my_list))
    end_time = time.time()
    print(end_time - start_time)

    def unique(s):
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    return False
        return True

    start_time = time.time()
    print(unique('hi there' * 10000000))
    end_time = time.time()
    print(end_time - start_time)











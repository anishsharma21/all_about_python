import random
import math
"""
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
        
"""

def sum_of_squares_odd(n):
    return sum([val**2 for val in range(1,n,2)])








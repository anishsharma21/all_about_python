import random
import math
import itertools

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
        return change

    print(make_change(5, 18.65))
    
    
    

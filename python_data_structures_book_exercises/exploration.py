import random
import math

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
















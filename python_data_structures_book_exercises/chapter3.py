def skip():
    def factorial(n):
        if n < 2:
            return n
        return n * factorial(n-1)

    print(factorial(5))

    def draw_line(tick_length, tick_label=''):
        line = '-' * tick_length
        if tick_label:
            line += ' ' + tick_label + 'cm'
        print(line)

    def draw_interval(center_length):
        if center_length > 0:
            draw_interval(center_length - 1)
            draw_line(center_length)
            draw_interval(center_length - 1)

    def draw_ruler(num_cms, major_length):
        draw_line(major_length, '0')
        for i in range(1, num_cms + 1):
            draw_interval(major_length - 1)
            draw_line(major_length, str(i))

    draw_ruler(5, 5)

    def binary_search(arr, target, low=None, high=None):
        if low is None:
            low = 0
            high = len(arr) - 1
        if low >= high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            return binary_search(arr, target, low=low, high=mid)
        else:
            return binary_search(arr, target, low=mid+1, high=high)
        
        
    my_arr = [1, 2, 5, 6, 6, 7, 8, 13, 14, 18, 24]
    print(binary_search(my_arr, 24))

    def bad_fibonacci(n):
        if n <= 1:
            return 1
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)

    print(bad_fibonacci(7))

    def good_fibonacci(n):
        if n <= 1:
            return n, 0
        a, b = good_fibonacci(n-1)
        return (a+b, a)

    print(good_fibonacci(7))

    def recursion_sum(arr, idx=0):
        if idx == len(arr) - 1:
            return arr[idx]
        return arr[idx] + recursion_sum(arr, idx+1)

    my_arr = [1, 2, 5, 6, 6, 7, 8, 13, 14, 18, 24]
    print(recursion_sum(my_arr))

    def reverse_arr(arr, idx=0):
        if idx == len(arr) // 2:
            return arr
        arr[idx], arr[len(arr) - 1 - idx] = arr[len(arr) - 1 - idx], arr[idx]
        return reverse_arr(arr, idx+1)

    my_arr = [1, 2, 5, 6, 6, 7, 8, 13, 14, 18, 24, 5]
    print(reverse_arr(my_arr))

    def power(x, n):
        if n == 0:
            return 1
        return x * power(x, n-1)
    print(power(2, 5))

    def power(x, n):
        if n == 0:
            return 1
        partial = power(x, n // 2)
        result = partial * partial
        if result % 2 == 1:
            result *= x
        return result

    def binary_sum(arr, idx=0):
        if idx == len(arr) // 2:
            if len(arr) % 2 == 0:
                return 0
            return arr[idx]
        return arr[idx] + arr[len(arr) - 1 - idx] + binary_sum(arr, idx+1)

    my_arr = [1, 2, 3, 4, 5]
    print(binary_sum(my_arr))

    def binary_sum(arr, start, stop):
        if start >= stop:
            return 0
        elif start == stop - 1:
            return arr[start]
        mid = (start + stop) // 2
        return binary_sum(arr, start, mid) + binary_sum(arr, mid, stop)

    my_arr = [1, 2, 3, 4, 5]
    print(binary_sum(my_arr, 0, 5))

def iterative_binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return -1

my_arr = [1, 2, 5, 6, 6, 7, 8, 13, 14, 18, 24, 55]
print(iterative_binary_search(my_arr, 1))


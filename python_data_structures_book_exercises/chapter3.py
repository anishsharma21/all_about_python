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
    print(binary_search(my_arr, 5))

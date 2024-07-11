def merge_sort(data):
    if len(data) == 1:
        return data
    m = len(data) // 2
    left = merge_sort(data[:m])
    right = merge_sort(data[m:])
    data_sorted = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            data_sorted.append(left[l])
            l += 1
        else:
            data_sorted.append(right[r])
            r += 1
    if l < len(left):
        data_sorted.extend(left[l:])
    else:
        data_sorted.extend(right[r:])
    return data_sorted

def merge_sort_optimized(data):
    if len(data) > 1:
        m = len(data) // 2
        left = data[:m]
        right = data[m:]

        merge_sort_optimized(left)
        merge_sort_optimized(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

    return data

data = [4, 1, 3, 2, -1]
print(merge_sort_optimized(data))

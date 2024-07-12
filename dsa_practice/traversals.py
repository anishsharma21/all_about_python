class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder_traversal(root: TreeNode):
    res = []
    def traverse(node):
        if node:
            traverse(node.left)
            traverse(node.right)
            res.append(node.val)
    traverse(root)
    return res

def mergeSort(data):
    if len(data) <= 1:
        return data
    m = len(data) // 2
    left = mergeSort(data[:m])
    right = mergeSort(data[m:])
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

my_arr = [2, 4, 1, 3, -1]
print(mergeSort(my_arr))
import sys

n = 10
data = []
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print(f"Number of items in list: {a} | Size of list in bytes: {b} bytes")
    data.append(None)

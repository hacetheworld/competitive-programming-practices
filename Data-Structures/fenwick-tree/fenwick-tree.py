def update(Bit, val, idx):
    while idx < len(Bit):
        Bit[idx] += val
        idx += (idx & (-idx))


def query(Bit, idx):
    res = 0
    while idx < len(Bit) and idx > 0:
        res += Bit[idx]
        idx -= (idx & (-idx))
    return res


def getRangeSum(Bit, l, r):
    leftRes = query(Bit, l-1)
    rightRes = query(Bit, r)
    return rightRes-leftRes


Bit = [0 for _ in range(8)]
arr = [1, 2, 3, 4, 5, 6, 8]
print(arr)
for i in range(len(arr)):
    update(Bit, arr[i], i+1)
print(Bit)

print(query(Bit, 6))
print(getRangeSum(Bit, 3, 4))

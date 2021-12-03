def build(arr, l, r, val, idx):
    if l > r:
        return
    if l == r:
        arr[idx] = val[l]
        return
    md = (l+r)//2
    build(arr, l, md, val, (2*idx))
    build(arr, md+1, r, val, (2*idx)+1)
    arr[idx] = arr[(2*idx)]+arr[(2*idx)+1]


segTree = [0 for _ in range(4*5)]
val = [1, 2, 3, 4, 5]
build(segTree, 0, 4, val, 1)
print(segTree)

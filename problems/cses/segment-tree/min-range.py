# import inbuilt standard input output
import sys
import math
from sys import stdin, stdout

# suppose a function called main() and
# all the operations are performed

# ////////// Get integer values in variables \\\\\\\\\\\\\\\\\\\\\\\


def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_string(): return sys.stdin.readline().strip()


# def min_in_seg(tree, start, end, treeNode, left, right):
#     if start > right or end < left:
#         return float("inf")
#     if start >= left and end <= right:
#         return tree[treeNode]
#     mid = (start+end)//2
#     return min_in_seg(tree, start, mid, 2*treeNode+1, left, right) min_in_seg(tree, mid+1, end, 2*treeNode+2, left, right)


# def create_seg(arr, tree, start, end, treeNode):
#     # createHelper(self,arr,)
#     if start == end:
#         tree[treeNode] = arr[start]
#         return
#     mid = (start+end)//2
#     create_seg(arr, tree, start, mid, 2*treeNode+1)
#     create_seg(arr, tree, mid+1, end, 2*treeNode+2)
#     tree[treeNode] = min(tree[2*treeNode+1], tree[2*treeNode+2])


# // Fenwick Tree OR BIT Code

def update(Bit, val, idx):
    while idx < len(Bit):
        Bit[idx] = min(val, Bit[idx])
        idx += (idx & (-idx))


def query(Bit, lidx, idx):
    res = float("inf")
    while lidx <= idx and idx < len(Bit) and idx > 0:
        res = min(res, Bit[idx])
        idx -= (idx & (-idx))
    return res


def getRangeSum(Bit, l, r):
    return query(Bit, l, r)


def main():
    # //TAKE INPUT HERE
    n, q = get_ints_in_variables()
    arr = get_ints_in_list()
    Bit = [float("inf") for _ in range(n+1)]
    for i in range(len(arr)):
        update(Bit, arr[i], i+1)
    for _ in range(q):
        tq, l, r = get_ints_in_variables()
        # FIND ANSWER HERE
        if tq == 1:
            update(Bit, arr[l-1], l)
            Bit[l] = r
            update(Bit, r, l)
            arr[l-1] = r

            print(Bit)
        else:
            print(getRangeSum(Bit, l, r))


# call the main method
if __name__ == "__main__":
    main()

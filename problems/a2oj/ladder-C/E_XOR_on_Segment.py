# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
import sys
import math
import bisect
import heapq
from bisect import bisect_right
from sys import stdin, stdout

# -------------- INPUT FUNCTIONS ------------------


def get_ints_in_variables(): return map(
    int, sys.stdin.readline().strip().split())


def get_int(): return int(sys.stdin.readline())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))
def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()

# -------- SOME CUSTOMIZED FUNCTIONS-----------


def myceil(x, y): return (x + y - 1) // y


# -------------- SOLUTION FUNCTION ------------------
def putBits(arr, idx, v):
    for i in range(20):
        mask = 1 << i
        if((v & mask) > 0):
            arr[idx][1][i] = 1


def makepairUtil(segTree, idx):
    res = makePair(segTree[2*idx], segTree[2*idx+1])
    segTree[idx][0] = res[0]
    for i in range(20):
        segTree[idx][1][i] = res[1][i]


def makePair(l, r):
    tmp = [0 for _ in range(20)]
    sm = 0
    sm = l[0]+r[0]
    for i in range(20):
        tmp[i] = l[1][i]+r[1][i]
    return [sm, tmp]


def build(segTree, arr, i, n, idx):
    if i == n:
        segTree[idx][0] = arr[i]
        putBits(segTree, idx, arr[i])
        return
    md = (i+n)//2
    build(segTree, arr, i, md, 2*idx)
    build(segTree, arr, md+1, n, (2*idx)+1)
    makepairUtil(segTree, idx)


def propagate(segTree, lazy, i, n, idx):
    if lazy[idx] == 0:
        return
    if i == n:
        segTree[idx][0] ^= lazy[idx]
        lazy[idx] = 0
        putBits(segTree, idx, segTree[idx][0])
    else:
        x = lazy[idx]
        lazy[idx] = 0
        lazy[idx*2] ^= x
        lazy[(idx*2)+1] ^= x
        sm = segTree[idx][0]
        for i in range(20):
            mask = 1 << i
            if((x & mask) > 0):
                one = segTree[idx][1][i]
                zero = ((n-i)+1) - one
                diff = (zero-one)
                sm += (diff*mask)
                segTree[idx][1][i] = zero
        segTree[idx][0] = sm


def query(segTree, lazy, i, n, l, r, idx):
    if i > r or n < l:
        return 0
    propagate(segTree, lazy, i, n, idx)
    if i >= l and n <= r:
        return segTree[idx][0]
    md = (i+n)//2
    return query(segTree, lazy, i, md, l, r, 2*idx)+query(segTree, lazy, md+1, n, l, r, (2*idx)+1)


def update(segTree, lazy, i, n, l, r, idx, val):
    if i > r or n < l:
        return
    propagate(segTree, lazy, i, n, idx)
    if i >= l and n <= r:
        lazy[idx] ^= val
        propagate(segTree, lazy, i, n, idx)
        return
    md = (i+n)//2
    update(segTree, lazy, i, md, l, r, 2*idx, val)
    update(segTree, lazy, md+1, n, l, r, (2*idx)+1, val)
    makepairUtil(segTree, idx)


def Solution():
    # Write Your Code Here
    n = get_int()
    arr = get_ints_in_list()
    segTree = [[0, [0 for _ in range(20)]] for _ in range(4*n)]
    lazy = [0 for _ in range(4*n)]
    build(segTree, arr, 0, n-1, 1)
    # print(segTree)
    for _ in range(get_int()):
        inp = get_ints_in_list()
        if inp[0] == 1:
            print(query(segTree, lazy, 0, n-1, inp[1]-1, inp[2]-1, 1))
        else:
            update(segTree, lazy, 0, n-1, inp[1]-1, inp[2]-1, 1, inp[3])


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()

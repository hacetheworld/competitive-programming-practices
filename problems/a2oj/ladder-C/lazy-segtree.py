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


def add(segTree, lazy, i, n, idx, val):
    segTree[idx] += (val)*(n-i+1)
    # print(i, n, val, "jdkdksk")
    if i != n:
        lazy[idx] += val


def pushdown(segTree, lazy, i, n, idx):
    if lazy[idx] != 0:
        md = (i+n)//2
        # print(i, "update")
        add(segTree, lazy, i, md, 2*idx, lazy[idx])
        add(segTree, lazy, md+1, n, 2*idx+1, lazy[idx])
        lazy[idx] = 0


def build(segTree, arr, i, n, idx):
    if i == n:
        segTree[idx] = arr[i-1]
        return
    md = (i+n)//2
    build(segTree, arr, i, md, 2*idx)
    build(segTree, arr, md+1, n, (2*idx)+1)
    segTree[idx] = segTree[2*idx]+segTree[(2*idx)+1]


def update(segTree, lazy, i, n, l, r, val, idx):
    if l > n or r < i:
        return 0
    if i >= l and r >= n:
        # print(i, n, "in")
        add(segTree, lazy, i, n, idx, val)
        return
    pushdown(segTree, lazy, idx, i, n)
    md = (i+n)//2
    update(segTree, lazy, i, md, l, r, val, 2*idx)
    update(segTree, lazy, md+1, n, l, r, val, 2*idx+1)
    segTree[idx] = segTree[2*idx]+segTree[2*idx+1]


def query(segTree, lazy, i, n, l, r, idx):
    if l > n or r < i:
        return 0
    if i >= l and r >= n:
        pushdown(segTree, lazy, idx, i, n)
        return segTree[idx]
    pushdown(segTree, lazy, idx, i, n)
    md = (i+n)//2
    ans = query(segTree, lazy, i, md, l, r, 2*idx)
    ans += query(segTree, lazy, md+1, n, l, r, 2*idx+1)
    return ans


def Solution():
    # Write Your Code Here
    n = get_int()
    arr = get_ints_in_list()
    segTree = [0 for _ in range(4*n)]
    lazy = [0 for _ in range(4*n)]
    # print(segTree)
    build(segTree, arr, 1, n, 1)
    print(segTree)
    q = get_int()
    for _ in range(q):
        inp = get_ints_in_list()
        if inp[0] == 1:
            print(query(segTree, lazy, 1, n, inp[1], inp[2], 1))
        else:
            update(segTree, lazy, 1, n, inp[1], inp[2], inp[3], 1)
            print(segTree)


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()

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


def build(arr, i, n, idx, segTree):
    if i == n:
        segTree[idx] = arr[i-1]
        return
    md = (i+n)//2
    build(arr, i, md, (2*idx), segTree)
    build(arr, md+1, n, (2*idx)+1, segTree)
    segTree[idx] = segTree[2*idx]+segTree[(2*idx)+1]


def update(segTree, i, n, pos, val, idx):
    if i == n:
        segTree[idx] = val
        return
    md = (i+n)//2
    if pos <= md:
        update(segTree, i, md, pos, val, 2*idx)
    else:
        update(segTree, md+1, n, pos, val, 2*idx+1)
    segTree[idx] = segTree[2*idx]+segTree[(2*idx)+1]


def getSum(segTree, i, n, l, r, idx):
    if l > n or r < i:
        return 0
    if l <= i and r >= n:
        return segTree[idx]
    md = (i+n)//2
    return getSum(segTree, i, md, l, r, 2*idx)+getSum(segTree, md+1, n, l, r, 2*idx+1)


def Solution(arr, n):
    # Write Your Code Here
    segTree = [0 for _ in range((4*n)+1)]
    build(arr, 1, n, 1, segTree)
    q = get_int()
    # print(segTree)
    for _ in range(q):
        inp = get_ints_in_list()
        if inp[0] == 1:
            print(getSum(segTree, 1, n, inp[1], inp[2], 1))
        else:
            update(segTree, 1, n, inp[1], inp[2], 1)


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = get_ints_in_list()

    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()

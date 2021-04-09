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

# -------------- SOLUTION FUNCTION ------------------


def lcm(a, b):
    return ((a*b)//math.gcd(a, b))


def update(Bit, val, idx):
    while idx < len(Bit):
        Bit[idx] = lcm(Bit[idx], val)
        idx += (idx & (-idx))


def query(Bit, idx):
    res = 1
    while idx < len(Bit) and idx > 0:
        res = lcm(Bit[idx], res)
        idx -= (idx & (-idx))
    return res


def getRangeQuery(Bit, l, r):
    leftRes = query(Bit, l-1)
    rightRes = query(Bit, r)
    return rightRes//leftRes


def swap(l, r):
    return (r, l)


def Solution(arr, n):
    # Write Your Code Here
    Bit = [1 for _ in range(n+1)]
    for i in range(len(arr)):
        update(Bit, arr[i], i+1)
    # //Answer Queries
    # print(Bit)
    last = 0
    for _ in range(get_int()):
        x, y = get_ints_in_variables()
        l = ((x+last) % n) + 1
        r = ((y+last) % n) + 1
        if l > r:
            l, r = swap(l, r)
        last = getRangeQuery(Bit, l, r)
        print(last)


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = get_ints_in_list()
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()

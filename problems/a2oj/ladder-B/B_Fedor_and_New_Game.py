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


def makeBits(v):
    res = []
    while v:
        if v % 2:
            res.append(1)
        else:
            res.append(0)
        v = v//2
    return res


def check(a, b):
    tmp = 0
    for i in range(len(a)):
        if i >= len(b):
            if a[i] == 1:
                tmp += 1
        else:
            if a[i] != b[i]:
                tmp += 1
    return tmp


def Solution(arr, n, m, k):
    # Write Your Code Here
    bits = []
    for v in arr:
        bits.append(makeBits(v))
    fredo = bits[-1]
    ans = 0
    # print(bits)
    for i in range(len(bits)-1):
        if len(fredo) >= len(bits[i]):
            if check(fredo, bits[i]) <= k:
                ans += 1
        else:
            if check(bits[i], fredo) <= k:
                ans += 1
    print(ans)


def main():
    # Take input Here and Call solution function
    n, m, k = get_ints_in_variables()
    arr = []
    for _ in range(m+1):
        arr.append(get_int())
    Solution(arr, n, m, k)


# calling main Function
if __name__ == '__main__':
    main()

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


def check(a, n, k):
    ka, kb = k-1, 0
    i = 0
    while i < n:
        if a[i][0] >= ka and a[i][1] >= kb:
            k -= 1
            ka -= 1
            kb += 1
        if k <= 0:
            return True
        i += 1
    return False


def Solution(a, n):
    # Write Your Code Here
    l = 1
    r = n
    ans = 1
    while l <= r:
        k = (l+r)//2
        if check(a, n, k):
            ans = k
            l = k+1
        else:
            r = k-1
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        a = []
        for _ in range(n):
            x, y = get_ints_in_variables()
            a.append([x, y])
        Solution(a, n)


# calling main Function
if __name__ == '__main__':
    main()

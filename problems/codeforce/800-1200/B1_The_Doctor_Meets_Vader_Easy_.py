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


def bst(a2, n, key):
    l = 0
    r = n-1
    ans = -1
    while l <= r:
        mid = (l+r)//2
        if a2[mid][0] > key:
            r = mid-1
        else:
            l = mid+1
            ans = mid
    return ans


def Solution(a1, a2, s, b):
    # Write Your Code Here
    prefix = [0]
    a2 = sorted(a2, key=lambda x: x[0])
    for v in a2:
        prefix.append(prefix[-1]+v[1])
    for i in range(s):
        idx = bst(a2, b, a1[i])
        if idx == -1:
            print(0, end=" ")
        else:
            print(prefix[idx+1], end=" ")
    print()


def main():
    # Take input Here and Call solution function
    s, b = get_ints_in_variables()
    a1 = get_ints_in_list()
    a2 = [get_ints_in_list() for _ in range(b)]
    Solution(a1, a2, s, b)


# calling main Function
if __name__ == '__main__':
    main()

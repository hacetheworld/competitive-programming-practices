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


def Solution(a, b, n, k):
    # Write Your Code Here
    a = sorted(a)
    b = sorted(b)
    res = 0
    pt = n-k
    for i in range(k):
        res += a[n-i-1]
        if b[i] == 1:
            res += (a[n-i-1])
        else:
            pt -= (b[i]-1)
            res += (a[pt])
    print(res)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        a = get_ints_in_list()
        w = get_ints_in_list()
        Solution(a, w, n, k)


# calling main Function
if __name__ == '__main__':
    main()

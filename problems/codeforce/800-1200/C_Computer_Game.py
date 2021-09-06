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


def Solution(k, n, a, b):
    # Write Your Code Here
    s = 0
    e = n
    ans = -1
    while s <= e:
        mid = (s+e)//2
        t = mid*a
        t2 = (n-mid)*b
        if t+t2 < k:
            ans = mid
            s = mid+1
        else:
            e = mid-1
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        k, n, a, b = get_ints_in_variables()
        Solution(k, n, a, b)


# calling main Function
if __name__ == '__main__':
    main()

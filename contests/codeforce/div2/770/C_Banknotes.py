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


def Solution(a, n, k):
    # Write Your Code Here
    a = [pow(10, el) for el in a]
    k += 1
    res = 0
    for i in range(n):
        cnt = k
        if i+1 < n:
            cnt = min(cnt, (a[i+1]//a[i])-1)
        res += (a[i]*cnt)
        k -= cnt
    print(res)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        a = get_ints_in_list()
        Solution(a, n, k)


# calling main Function
if __name__ == '__main__':
    main()

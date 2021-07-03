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


def Solution(n, prec):
    # Write Your Code Here
    ans = 0
    while n > 1:
        ans += 1
        idx = bisect_right(prec, n)-1
        if idx == -1:
            break
        n -= prec[idx]
    print(ans)


def main():
    # Take input Here and Call solution function
    prec = [0 for _ in range(100001)]
    for i in range(1, 100001):
        prec[i] = prec[i-1]+(3 * i) - 1
    for _ in range(get_int()):
        Solution(get_int(), prec)


# calling main Function
if __name__ == '__main__':
    main()

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


def findPowers(n):
    r = []
    t = 1
    while n:
        d = n % 2
        if d:
            heapq.heappush(r, -1*t)
        t *= 2
        n = n//2
    return r


def Solution(n, k):
    # Write Your Code Here
    powers = findPowers(n)
    if k < len(powers):
        print("NO")
        return
    while len(powers) != k:
        if powers[0] == -1:
            break
        t = -1 * heapq.heappop(powers)//2
        heapq.heappush(powers, (-1*t))
        heapq.heappush(powers, (-1*t))
    if len(powers) == k:
        print("YES")
        for v in powers:
            print(-1*v, end=" ")
        print()
    else:
        print("NO")


def main():
    # Take input Here and Call solution function
    n, k = get_ints_in_variables()
    Solution(n, k)


# calling main Function
if __name__ == '__main__':
    main()

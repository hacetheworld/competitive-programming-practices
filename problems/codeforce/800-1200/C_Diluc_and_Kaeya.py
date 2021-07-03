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


def Solution(s, n):
    # Write Your Code Here
    dCount = 0
    kCount = 0
    hm = {}
    for c in s:
        if c == "D":
            dCount += 1
        else:
            kCount += 1
        g = math.gcd(dCount, kCount)
        a = dCount//g
        b = kCount//g
        pair = (a, b)
        hm[pair] = hm.get(pair, 0)+1
        print(hm[pair], end=" ")
    print()


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        s = get_string()
        Solution(s, n)


# calling main Function
if __name__ == '__main__':
    main()

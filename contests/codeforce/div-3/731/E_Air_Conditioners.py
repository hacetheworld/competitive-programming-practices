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


def Solution(a, b, n, k):
    # Write Your Code Here
    hm = {}
    for i in range(k):
        hm[a[i]-1] = b[i]
    pref = [float("inf")]
    suffix = [float("inf") for _ in range(n+1)]
    for i in range(n):
        if i in hm:
            pref.append(min(pref[-1]+1, hm[i]))
        else:
            pref.append(pref[-1]+1)
    pref.pop(0)
    for i in range(n-1, -1, -1):
        if i in hm:
            suffix[i] = min(suffix[i+1]+1, hm[i])
        else:
            suffix[i] = suffix[i+1]+1
    suffix.pop()
    for i in range(n):
        print(min(pref[i], suffix[i]), end=" ")
    print()


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        input()
        n, k = get_ints_in_variables()
        a = get_ints_in_list()
        b = get_ints_in_list()
        Solution(a, b, n, k)


# calling main Function
if __name__ == '__main__':
    main()

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


def Solution(a, b, n, m):
    # Write Your Code Here
    ans = 0
    pos = [0 for _ in range(n+1)]
    for i in range(n):
        pos[a[i]] = i
    indx = -1
    for i in range(m):
        if pos[b[i]] > indx:
            ans += (2*(pos[b[i]]-i))+1
            indx = pos[b[i]]
        else:
            ans += 1

    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, m = get_ints_in_variables()
        a = get_ints_in_list()
        b = get_ints_in_list()
        Solution(a, b, n, m)


# calling main Function
if __name__ == '__main__':
    main()

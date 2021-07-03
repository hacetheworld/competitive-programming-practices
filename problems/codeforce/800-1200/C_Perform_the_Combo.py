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


def Solution(s, p, n, m):
    # Write Your Code Here
    ans = [0 for _ in range(26)]
    prefix = [0 for _ in range(n+1)]
    for v in p:
        prefix[v-1] += 1
    for i in range(n-1, 0, -1):
        prefix[i-1] += prefix[i]
    for i in range(n):
        c = s[i]
        ans[ord(c)-97] += prefix[i]+1

    print(*ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, m = get_ints_in_variables()
        s = get_string()
        p = get_ints_in_list()
        Solution(s, p, n, m)


# calling main Function
if __name__ == '__main__':
    main()

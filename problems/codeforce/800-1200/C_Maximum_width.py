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


def Solution(s, t, n, m):
    # Write Your Code Here
    a = []
    b = []
    j = 0
    for i in range(n):
        if t[j] == s[i]:
            a.append(i)
            j += 1
        if j == m:
            break
    k = m-1
    for i in range(n-1, -1, -1):
        if t[k] == s[i]:
            b.append(i)
            k -= 1
        if k < 0:
            break
    ans = -1
    b = list(reversed(b))
    # print(a, b)
    for i in range(1, m):
        ans = max(ans, abs(max(a[i], b[i])-min(a[i-1], b[i-1])))
    print(ans)


def main():
    # Take input Here and Call solution function
    n, m = get_ints_in_variables()
    s = get_string()
    t = get_string()
    Solution(s, t, n, m)


# calling main Function
if __name__ == '__main__':
    main()

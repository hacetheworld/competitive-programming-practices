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


def Solution():
    # Write Your Code Here
    pass


def check(s1, s2, n, m):
    i = 0
    j = 0
    while i < n and j < m:
        if s1[i] != s2[j]:
            return False
        i += 1
        j += 1
        if j == m:
            j = 0
    return (i == n and j == 0)


def multiply(s, n):
    res = []
    i = 0
    j = 0
    m = len(s)
    while j < n:
        res.append(s[i % m])
        i += 1
        if i == m:
            i = 0
        j += 1
    return "".join(res)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        s1 = get_string()
        s2 = get_string()
        a = len(s1)
        b = len(s2)
        lm = ((a*b)//(math.gcd(a, b)))
        s1 = multiply(s1, a*(lm//a))
        s2 = multiply(s2, b*(lm//b))
        # print(s1, s2, "jjjjjjjjjjjjjjj")
        if len(s1) >= len(s2) and check(s1, s2, len(s1), len(s2)):
            print(s1)
        elif len(s1) < len(s2) and check(s2, s1, len(s2), len(s1)):
            print(s2)
        else:
            print(-1)


# calling main Function
if __name__ == '__main__':
    main()

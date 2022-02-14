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


def compliment(c, x):
    return c ^ (x-1)


def Solution(n, k):
    # Write Your Code Here
    a = [0 for _ in range(n//2)]
    b = [0 for _ in range(n//2)]
    if k == 0:
        for i in range(n//2):
            a[i] = i
            b[i] = compliment(i, n)
    elif k > 0 and k < n-1:
        smK = min(k, compliment(k, n))
        for i in range(n//2):
            if i == 0 or i == smK:
                continue
            a[i] = i
            b[i] = compliment(i, n)
        a[0] = 0
        b[0] = compliment(k, n)
        a[smK] = k
        b[smK] = n-1
    else:
        if n == 4:
            print(-1)
            return
        a[0] = n-2
        b[0] = n-1
        a[1] = n-3
        b[1] = 1
        a[2] = 0
        b[2] = 2
        for i in range(3, n//2):
            a[i] = i
            b[i] = compliment(i, n)
    for i in range(n//2):
        print(a[i], b[i])


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        Solution(n, k)


# calling main Function
if __name__ == '__main__':
    main()

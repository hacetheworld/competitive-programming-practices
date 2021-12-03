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


def Solution(n, k):
    # Write Your Code Here
    if (n == 1 and k != 0) or (k == 0 and n != 1) or (k != 0 and (n//2) > k):

        print(-1)
        return
    if k == 0 and n == 1:
        print(1)
        return
    t = n//2
    res = []
    x = k-(t-1)
    hm = {x, 2*x}
    # hm{2*x}=
    res.append(x)
    res.append(2*(x))
    i = 1
    t -= 1
    while t > 0:
        if i in hm or i+1 in hm:
            i += 1
        else:
            res.append(i)
            res.append(i+1)
            t -= 1
            i += 2
    if len(res) < n:
        while i in hm:
            i += 1
        res.append(i)
    print(*res)


def main():
    # Take input Here and Call solution function
    n, k = get_ints_in_variables()
    Solution(n, k)


# calling main Function
if __name__ == '__main__':
    main()

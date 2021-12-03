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


def calc(nb, ns, nc, pb, ps, pc, cb, cs, cc, x):
    return (max(0, (x*cb)-nb)*pb)+(max(0, (x*cs)-ns)*ps)+(max(0, (x*cc)-nc)*pc)


def Solution(s, nb, ns, nc, pb, ps, pc, r):
    # Write Your Code Here
    cb, cs, cc = 0, 0, 0
    for c in s:
        if c == "B":
            cb += 1
        elif c == "S":
            cs += 1
        else:
            cc += 1
    i = 1
    j = pow(10, 13)
    ans = 0
    while i <= j:
        mid = (i+j)//2
        # print(mid, "mid")
        if calc(nb, ns, nc, pb, ps, pc, cb, cs, cc, mid) <= r:
            i = mid+1
            ans = mid
        else:
            j = mid-1
    print(ans)


def main():
    # Take input Here and Call solution function
    s = get_string()
    nb, ns, nc = get_ints_in_variables()
    pb, ps, pc = get_ints_in_variables()
    r = get_int()
    Solution(s, nb, ns, nc, pb, ps, pc, r)


# calling main Function
if __name__ == '__main__':
    main()

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


def Solution(a, b, c, n):
    # Write Your Code Here
    tmp1 = abs(a[1]-b[1])+2
    tmp = tmp1
    ans = 0
    for i in range(2, n):
        if a[i] == b[i]:
            ans = max(tmp1, tmp)
            tmp1 = 2
            tmp = 2
        else:
            tmp += abs(a[i]-b[i])
            if tmp > tmp1:
                ans = tmp
                tmp = abs(a[i]-b[i])+2
                tmp1 += 2
            else:
                tmp1 += 2
                tmp -= abs(a[i]-b[i])
    tmp1 += (c[-1]-1)
    tmp += (c[-1]-1)
    ans = max([ans, tmp1, tmp])
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        c = get_ints_in_list()
        a = get_ints_in_list()
        b = get_ints_in_list()
        Solution(a, b, c, n)


# calling main Function
if __name__ == '__main__':
    main()

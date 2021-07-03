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


def Solution(arr, n):
    # Write Your Code Here
    hm = {}
    for v in arr:
        if v in hm:
            hm[v] += 1
        else:
            hm[v] = 1
    tmpAns = 0
    for key in hm:
        val = hm[key]
        tmpAns += (((val)*(val-1))//2)
    ans = tmpAns
    for i in range(n):
        itm = arr[i]
        hm[itm] -= 1
        val = hm[itm]
        if val >= 1:
            f = (((val+1)*(val))//2)
            s = (((val-1)*(val))//2)
            tmpAns -= f
            tmpAns += s
        ans += ((tmpAns))
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()

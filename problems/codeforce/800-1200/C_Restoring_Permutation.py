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
    nums = {}
    for v in arr:
        nums[v] = True
    hm2 = {}
    for v in arr:
        num = v+1
        while num in nums:
            num += 1
        hm2[v] = num
        nums[num] = True
    res = []
    hm = {}
    for v in arr:
        hm[v] = True
        res.append(v)
        res.append(hm2[v])
        hm[hm2[v]] = True
    flag = True
    for i in range(1, (2*n)+1):
        if not i in hm:
            flag = False
            True
    if flag:
        print(*res)
    else:
        print(-1)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()

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
    cnt = 0
    els = 0
    sm = 0
    flag = True
    res = []
    j = 0
    for i in range(n):
        v = arr[i]
        sm += v
        if v < 0:
            if sm == 0 and els == 1:
                sm = 0
                els = 0
                hm = {}
                res.append((i-j)+1)
                j = i+1
                cnt += 1
            elif (abs(v) in hm) and hm[abs(v)] == abs(v):
                els -= 1
                hm[v] = 0
            else:
                flag = False
                break
        else:
            if v in hm:
                flag = False
                break
            hm[v] = v
            els += 1
    if flag and sm == 0 and els == 0:
        print(cnt)
        print(*res)
    else:
        print(-1)


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = get_ints_in_list()
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()

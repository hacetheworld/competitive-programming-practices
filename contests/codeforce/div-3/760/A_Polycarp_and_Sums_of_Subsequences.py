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


def check(v, arr):
    tmp = [c for c in v]
    for i in range(3):
        for j in range(i+1):
            tmp.append(v[i]+v[j])
    tmp.append(sum(v))
    f = 1
    for c in arr:
        f = 0
        for k in tmp:
            if k == c:
                f = 1
                break
    if f:
        return True
    else:
        return False


def Solution(arr):
    # Write Your Code Here
    res = []
    for i in range(7):
        for j in range(i+1, 7):
            for k in range(j+1, 7):
                res.append([arr[i], arr[j], arr[k]])
    for v in res:
        if check(v, arr):
            print(*v)
            return


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        arr = get_ints_in_list()
        Solution(arr)


# calling main Function
if __name__ == '__main__':
    main()

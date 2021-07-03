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


def Solution(arr1, arr2, n, m):
    # Write Your Code Here
    swapsIdexs = {}
    for v in arr2:
        swapsIdexs[v] = True
    flag = True
    tmp = arr1.copy()
    arr1 = sorted(arr1)
    for i in range(1, n):
        idx = tmp.index(arr1[i-1])
        for j in range(i, idx+1):
            if not j in swapsIdexs:
                flag = False
                break
        tmp[idx] = -1
    if flag:
        print("YES")
    else:
        print("NO")


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, m = get_ints_in_variables()
        arr1 = get_ints_in_list()
        arr2 = get_ints_in_list()
        Solution(arr1, arr2, n, m)


# calling main Function
if __name__ == '__main__':
    main()

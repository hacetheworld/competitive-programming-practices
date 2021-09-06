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


def Solution(arr, n, k):
    # Write Your Code Here
    hm = {}
    flg = 1
    for v in arr:
        if v in hm:
            hm[v] += 1
        else:
            hm[v] = 1
        if hm[v] > k:
            flg = 0
            break
    if flg:
        color = {}
        print("YES")
        colorsUsed = {}
        c = 1
        res = []
        for i in range(n):
            if arr[i] in color:
                res.append(color[arr[i]]+1)
                color[arr[i]] += 1
                colorsUsed[color[arr[i]]] = 1
            else:
                res.append(c)
                color[arr[i]] = c
                colorsUsed[c] = 1
        i = 0
        remaiNColr = []
        for j in range(1, k+1):
            if not j in colorsUsed:
                remaiNColr.append(j)
        hm = {}
        for i in range(n):
            if len(remaiNColr) > 0:
                if res[i] in hm:
                    res[i] = remaiNColr.pop()
                else:
                    hm[res[i]] = 1
            else:
                break
        print(*res)
    else:
        print("NO")


def main():
    # Take input Here and Call solution function
    n, k = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, k)


# calling main Function
if __name__ == '__main__':
    main()

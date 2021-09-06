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


def Solution(hm, adjList, n):
    # Write Your Code Here
    # print(adjList)
    f = 1
    for i in range(1, n+1):
        if hm[i][1] == -1:
            continue
        if hm[i][1] == 1:
            flg = 1
            for child in adjList[i]:
                if hm[child][1] == 0:
                    flg = 0
                    break
            if flg:
                f = 0
                print(i, end=" ")
    if f:
        print(-1)
    else:
        print()


def main():
    # Take input Here and Call solution function
    n = get_int()
    hm = {}
    adjList = [[] for _ in range(n+1)]
    for i in range(n):
        u, v = get_ints_in_variables()
        hm[i+1] = [u, v]
        if u != -1:
            adjList[u].append(i+1)
    Solution(hm, adjList, n)


# calling main Function
if __name__ == '__main__':
    main()

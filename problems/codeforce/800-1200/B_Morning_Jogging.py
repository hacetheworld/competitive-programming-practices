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

# -------------- SOLUTION FUNCTION ------------------


def Solution(arr, n, m):
    # Write Your Code Here
    res = [[-1 for _ in range(m)] for _ in range(n)]
    vv = []
    for i in range(n):
        for j in range(m):
            vv.append([arr[i][j], [i, j]])

    vv = sorted(vv, key=lambda x: x[0])
    for i in range(m):
        x = vv[i][1][0]
        y = vv[i][1][1]
        wt = vv[i][0]
        res[x][i] = wt
        arr[x][y] = -1

    for i in range(n):
        idx = 0
        for j in range(m):
            while(idx < m and res[i][idx] != -1):
                idx += 1
            if(arr[i][j] == -1):
                continue
            res[i][idx] = arr[i][j]
    # print(ans)
    for i in range(n):
        for j in range(m):
            print(res[i][j], end=" ")
        print()


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, m = get_ints_in_variables()
        arr = []
        for _ in range(n):
            arr.append(get_ints_in_list())
        Solution(arr, n, m)


# calling main Function
if __name__ == '__main__':
    main()

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


def Solution(arr):
    # Write Your Code Here
    N = 500 * 1000 + 13
    ans = []
    tmp = [i for i in range(N+1)]
    for i in range(len(arr)-1, -1, -1):
        if arr[i][0] == 1:
            ans.append(tmp[arr[i][1]])
        else:
            tmp[arr[i][1]] = tmp[arr[i][2]]
    print(*list(reversed(ans)))


def main():
    # Take input Here and Call solution function
    arr = []
    for _ in range(get_int()):
        arr.append(get_ints_in_list())
    Solution(arr)


# calling main Function
if __name__ == '__main__':
    main()

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
    arr = sorted(arr, key=lambda x: x[1])
    l = 0
    r = n-1
    ans = 0
    itmBought = 0
    while l <= r:
        if arr[l][1] > itmBought:
            need = min(arr[l][1]-itmBought, arr[r][0])
            arr[r][0] -= need
            itmBought += need
            ans += (2*need)
            if arr[r][0] == 0:
                r -= 1
        else:
            itmBought += arr[l][0]
            ans += arr[l][0]
            l += 1

    print(ans)


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = [get_ints_in_list() for _ in range(n)]
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()

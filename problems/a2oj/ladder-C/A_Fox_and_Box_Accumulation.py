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
    arr = sorted(arr)
    ans = 0
    while len(arr):
        ans += 1
        cnt = 1
        j = 0
        arr.pop(0)
        while j < len(arr):
            if arr[j] >= cnt:
                arr.pop(j)
                cnt += 1
                j -= 1
            j += 1
        # print(arr, "arr")
        if len(arr) and arr[0] == 0 and 0 == arr[-1]:
            ans += len(arr)
            break
    print(ans)


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = get_ints_in_list()
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()

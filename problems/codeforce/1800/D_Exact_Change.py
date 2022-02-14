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
    mx = max(arr)
    m = myceil(mx, 3)
    ans = m+1
    for one in range(0, 3):
        for two in range(0, 3):
            for three in range(max(0, m-4), m+1):
                flg = 1
                for i in range(n):
                    f = 0
                    for j in range(0, one+1):
                        for k in range(0, two+1):
                            left = arr[i]-j-2*k
                            if (left >= 0 and left % 3 == 0 and left//3 <= three):
                                f = 1
                                break
                    if f != 1:
                        flg = False
                        break
                if flg:
                    ans = min(ans, one+two+three)

    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()

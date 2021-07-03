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


def isPeak(arr, n, i):
    return i < n-1 and i > 0 and arr[i] > arr[i-1] and arr[i] > arr[i+1]


def Solution(arr, n, k):
    # Write Your Code Here
    ans = 1
    l = 0
    for i in range(1, k-1):
        if isPeak(arr, n, i):
            ans += 1
    mx = ans
    for j in range(k-1, n-1):
        if isPeak(arr, n, j) and not isPeak(arr, n, (j-k)+2):
            ans += 1
            if ans > mx:
                l = j-k+2
            mx = max(mx, ans)

        if not isPeak(arr, n, j) and isPeak(arr, n, (j-k)+2):
            ans -= 1

    print(mx, l+1)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, k)


# calling main Function
if __name__ == '__main__':
    main()

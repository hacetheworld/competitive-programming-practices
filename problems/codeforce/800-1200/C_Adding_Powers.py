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
    mx = max(arr)
    maxValue = 1
    while maxValue < mx:
        maxValue *= k
    flag = True
    while maxValue > 0:
        pos = []
        for i in range(n):
            if arr[i] >= maxValue:
                pos.append(i)
        if len(pos) >= 1 and arr[pos[0]] == 0:
            flag = False
            break
        elif len(pos) >= 1:
            arr[pos[0]] -= maxValue
        maxValue = maxValue//k
    for v in arr:
        if v != 0:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, k)


# calling main Function
if __name__ == '__main__':
    main()

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
    hm = {}
    for i in range(n):
        if not arr[i] in hm:
            hm[arr[i]] = [i+1]
        else:
            hm[arr[i]].append(i+1)
    ans = [n+1 for _ in range(n+1)]
    for i in range(1, n+1):
        if not i in hm:
            continue
        prev = 0
        diff = -1
        for j in hm[i]:
            diff = max(diff, j-prev)
            prev = j
        diff = max(diff, n-(prev-1))
        ans[diff] = min(ans[diff], i)
    # print(ans)
    prev = n+1
    for i in range(1, n+1):
        prev = min(ans[i], prev)
        if prev > n:
            ans[i] = -1
        else:
            ans[i] = prev

    for i in range(1, n+1):
        print(ans[i], end=" ")
    print()


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()

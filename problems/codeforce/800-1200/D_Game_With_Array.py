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


def Solution(n, s):
    # Write Your Code Here
    arr = []
    for _ in range(n-1):
        arr.append(1)
    left = s-(n-1)
    arr.append(left)
    flag = False
    k = -1
    l = s-arr[-1]
    for i in range(1, n+1):
        if (i <= l) or (i >= arr[-1] and i <= n):
            continue
        flag = True
        k = i
        break
    if flag:
        print("YES")
        print(*arr)
        print(k)
    else:
        print("NO")


def main():
    # Take input Here and Call solution function
    n, s = get_ints_in_variables()
    Solution(n, s)


# calling main Function
if __name__ == '__main__':
    main()

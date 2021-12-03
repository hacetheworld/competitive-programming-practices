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


def Solution():
    # Write Your Code Here
    n = get_int()
    arr = get_ints_in_list()
    pre = [-1 for _ in range(20)]
    pos = [-1 for _ in range(20)]
    ain = [False for _ in range((1 << 20)+1)]
    cnt = 0
    for i in range(n):
        for j in range(20-1, -1, -1):
            if arr[i] & (1 << j):
                pre[j] = i
        val = arr[i]
        if not ain[val]:
            # print("nsd")
            cnt += 1
        ain[val] = True
        for j in range(20):
            pos[j] = pre[j]
        pos = sorted(pos)
        for j in range(20-1, -1, -1):
            if pos[j] != -1:
                val |= arr[pos[j]]
            # print("val", val)
            if not ain[val]:
                cnt += 1
            ain[val] = True
    print(cnt)


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()

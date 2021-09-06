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
    t = get_int()
    leftcnt = 0
    rightcnt = 0
    leftIdx = {}
    l = 1
    rightIdx = {}
    r = 1
    for _ in range(t):
        inp = get_string().split(" ")
        if inp[0] == "L":
            v = int(inp[1])
            leftcnt += 1
            leftIdx[v] = l
            l += 1
        elif inp[0] == "R":
            v = int(inp[1])
            rightcnt += 1
            rightIdx[v] = r
            r += 1
        else:
            v = int(inp[1])
            ans = -1
            if v in leftIdx:
                ans = leftcnt-leftIdx[v]
                ans = min(ans, rightcnt+leftIdx[v]-1)
            else:
                ans = rightcnt-rightIdx[v]
                ans = min(ans, leftcnt+rightIdx[v]-1)
            print(ans)


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()

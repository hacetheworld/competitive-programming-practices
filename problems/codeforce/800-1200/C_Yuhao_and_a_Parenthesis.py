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


def check(s, n):
    stk = []
    right = 0
    left = 0
    for c in s:
        if c == "(":
            stk.append(c)
        else:
            if len(stk) > 0:
                stk.pop()
            else:
                right += 1
    left += len(stk)
    if left > 0 and right > 0:
        return [0, "None"]
    if left > 0:
        return [left, "left"]
    if right > 0:
        return [right, "right"]
    if left == right == 0:
        return[1, "perfectPair"]


def Solution(arr, n):
    # Write Your Code Here
    left = {}
    right = {}
    perfectPair = 0
    for s in arr:
        tmp = check(s, len(s))
        if tmp[1] == "left":
            if tmp[0] in left:
                left[tmp[0]] += 1
            else:
                left[tmp[0]] = 1
        elif tmp[1] == "right":
            if tmp[0] in right:
                right[tmp[0]] += 1
            else:
                right[tmp[0]] = 1
        elif tmp[1] == "perfectPair":
            perfectPair += 1
    ans = 0
    for v in left:
        if v in right and right[v] > 0:
            tmp = min(left[v], right[v])
            ans += tmp
            right[v] -= tmp
    print(ans+(perfectPair//2))


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = [get_string() for _ in range(n)]
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()

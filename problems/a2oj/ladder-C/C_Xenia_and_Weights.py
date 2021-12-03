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


def helper(arr, turn, sm, m, prev, res):
    if m == 0:
        return True
    for el in arr:
        if el == prev:
            continue
        if turn == 0:
            if el+sm > 0:
                res.append(el)
                if helper(arr, 1-turn, sm+el, m-1, el, res):
                    return True
                else:
                    res.pop()
        else:
            if sm-el < 0:
                res.append(el)
                if helper(arr, 1-turn, sm-el, m-1, el, res):
                    return True
                else:
                    res.pop()
    return False


def Solution(s, m):
    # Write Your Code Here
    arr = []
    for i in range(len(s)):
        if s[i] == "1":
            arr.append(i+1)
    # dp = [[False for _ in range(10)] for _ in range(10)]
    res = []
    if helper(arr, 0, 0, m, -1, res):
        print("YES")
        print(*res)
    else:
        print("NO")


def main():
    # Take input Here and Call solution function
    s = get_string()
    m = get_int()
    Solution(s, m)


# calling main Function
if __name__ == '__main__':
    main()

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


def Solution(s):
    # Write Your Code Here
    n = len(s)
    ans = [" " for _ in range(n)]
    cnt1 = 0
    lst = n
    for i in range(n-1, -1, -1):
        if s[i] == "1":
            cnt1 += 1
        if s[i] == "2":
            ans[i+cnt1] = "2"
            j = i+cnt1+1
            while j < n and ans[j] == " ":
                ans[j] = "0"
                j += 1
            lst = i
    cnt = 0
    for i in range(lst):
        if s[i] == "0":
            cnt += 1
    for i in range(n):
        if ans[i] == " ":
            if cnt > 0:
                ans[i] = "0"
                cnt -= 1
            else:
                ans[i] = "1"
    print("".join(ans))


def main():
    # Take input Here and Call solution function
    Solution(get_string())


# calling main Function
if __name__ == '__main__':
    main()

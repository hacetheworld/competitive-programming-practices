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

# -------------- SOLUTION FUNCTION ------------------


def helper(s, k):
    res = []
    while True:
        flag = False
        for c in s:
            res.append(c)
            k -= 1
            if k <= 0:
                flag = True
                break
        if flag:
            break
    return "".join(res)


def Solution(s, n, k):
    # Write Your Code Here
    ans = []
    ans.append(helper(s, k))
    for i in range(n-1, 0, -1):
        ans.append(helper(s[:i], k))
    ans = sorted(ans)
    print(ans[0])


def main():
    # Take input Here and Call solution function
    n, k = get_ints_in_variables()
    s = get_string()
    Solution(s, n, k)


# calling main Function
if __name__ == '__main__':
    main()

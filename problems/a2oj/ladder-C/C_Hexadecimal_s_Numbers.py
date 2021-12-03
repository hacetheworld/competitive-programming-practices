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


def permutaions(s, n, res):
    if len(s) > n:
        return res
    if len(s) == n:
        res.append(s)
    permutaions(s+"0", n, res)
    permutaions(s+"1", n, res)
    return res


def Solution(n):
    # Write Your Code Here
    res = []
    permutaions("", len(str(n)), res)

    ans = 0
    for v in res:
        if int(v) <= n and int(v) > 0:
            ans += 1
    print(ans)


def main():
    # Take input Here and Call solution function
    Solution(get_int())


# calling main Function
if __name__ == '__main__':
    main()

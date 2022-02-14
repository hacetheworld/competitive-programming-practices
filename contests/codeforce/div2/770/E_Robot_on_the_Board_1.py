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


def Solution(s, n, m):
    # Write Your Code Here
    ans = [1, 1]
    r, c = 1, 1
    for cl in s:
        if cl == "L":
            c -= 1
        elif cl == "R":
            c += 1
        elif cl == "U":
            r -= 1
        else:
            r += 1
        if r == 0:
            if ans[0] < n:
                ans[0] += 1
                r = 1
            else:
                break
        elif r > n:
            if ans[0] > 1:
                ans[0] -= 1
                r = n
            else:
                break

        elif c == 0:
            if ans[1] < m:
                ans[1] += 1
                c = 1
            else:
                break
        elif c > m:
            if ans[1] > 1:
                ans[1] -= 1
                c = m
            else:
                break

    print(*ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, m = get_ints_in_variables()
        s = get_string()
        Solution(s, n, m)


# calling main Function
if __name__ == '__main__':
    main()

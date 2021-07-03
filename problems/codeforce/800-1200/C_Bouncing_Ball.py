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


def Solution(s, n, p, k, x, y):
    # Write Your Code Here
    ans = float("inf")
    l = 1
    for _ in range(p-1, (p+k)-1):
        cnt = 0
        for j in range(n-l, p-2, k*-1):
            if s[j] == "0":
                cnt += 1
            ans = min(abs((j+1)-(p))*y+cnt*x, ans)
        l += 1
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, p, k = get_ints_in_variables()

        s = get_string()
        x, y = get_ints_in_variables()
        Solution(s, n, p, k, x, y)


# calling main Function
if __name__ == '__main__':
    main()

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


def Solution(x, y, n):
    # Write Your Code Here
    x = sorted(x)
    y = sorted(y)
    ans = 0
    for i in range(n):
        ans += (math.sqrt(x[i]*x[i]+y[i]*y[i]))
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        x, y = [], []
        for _ in range(2*n):
            a, b = get_ints_in_variables()
            if a == 0:
                y.append(abs(b))
            else:
                x.append(abs(a))
        Solution(x, y, n)


# calling main Function
if __name__ == '__main__':
    main()

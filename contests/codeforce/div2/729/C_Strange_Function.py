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


def lcm(a, b):
    return (a*b)//math.gcd(a, b)


def Solution(n, mod):
    # Write Your Code Here
    ans = 0
    p = 1
    k = 1
    count = n
    while count > 0:
        p = lcm(p, k)
        tmpAns = n//p
        ans += ((count-tmpAns)*(k))
        count = tmpAns
        k += 1
    print(ans % mod)


def main():
    # Take input Here and Call solution function
    mod = pow(10, 9)+7
    for _ in range(get_int()):
        n = get_int()
        Solution(n, mod)


# calling main Function
if __name__ == '__main__':
    main()

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


def Solution(n, mod):
    # Write Your Code Here
    s = str(n)
    ln = len(s)
    prefix = [n % mod]
    suffix = []
    for i in range(1, ln):
        prefix.append(s[i:])
    for i in range(1, ln):
        suffix.append(s[:i])
    suffix.append(n % mod)
    ans = 0
    print(prefix)
    print(suffix)
    for i in range(1, len(prefix)):
        ans = ((ans % mod)+(int(prefix[i]) % mod)) % mod
    for i in range(len(suffix)-1):
        ans = ((ans % mod)+(int(suffix[i]) % mod)) % mod
    # mul = 10
    for i in range(1, len(suffix)-1):
        ans = ((ans % mod) + (int(prefix[i]+suffix[i]) % mod)) % mod
    print(ans)


def main():
    # Take input Here and Call solution function
    n = get_int()
    mod = pow(10, 9)+7
    Solution(n, mod)


# calling main Function
if __name__ == '__main__':
    main()

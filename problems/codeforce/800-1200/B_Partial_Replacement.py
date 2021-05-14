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


def check(s, st, end):
    for i in range(st, end):
        if s[i] == "x":
            return True
    return False


def Solution(s, n, k):
    # Write Your Code Here
    s = [c for c in s]
    f = 0
    s1 = n-1
    for i in range(n):
        if s[i] == "*":
            f = i
            break
    for i in range(n-1, -1, -1):
        if s[i] == "*":
            s1 = i
            break
    ans = 0
    if f == s1:
        ans += 1
        s[f] = "x"
    else:
        ans += 2
        s[f] = "x"
        s[s1] = "x"
        while f+k < s1:
            for j in range(f+k, f, -1):
                if s[j] == "*":
                    s[j] = "x"
                    ans += 1
                    f = j
                    break
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        s = get_string()
        Solution(s, n, k)


# calling main Function
if __name__ == '__main__':
    main()

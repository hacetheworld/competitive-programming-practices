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


def Solution(s, n):
    # Write Your Code Here
    res = []
    i = n-1
    while i >= 0:
        c = s[i]
        if c == "1":
            res.append("1")
        else:
            f = -1
            for j in range(i):
                if s[j] == "1":
                    f = j
                    break
            if f == -1:
                for _ in range(i+1):
                    res.append("0")
                break
            if f == 0:
                res.append("0")
                break
            else:
                res.append("0")
                i = f
        i -= 1
    print("".join(list(reversed(res))))


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        s = get_string()
        Solution(s, n)


# calling main Function
if __name__ == '__main__':
    main()

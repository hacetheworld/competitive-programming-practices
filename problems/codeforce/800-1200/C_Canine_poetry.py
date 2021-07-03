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


def Solution():
    # Write Your Code Here
    pass


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        s = [c for c in get_string()]
        if len(s) == 1:
            print(0)
        elif len(s) == 2:
            if s[0] == s[1]:
                print(1)
            else:
                print(0)
        else:
            ans = 0
            i = 1
            while i < (len(s)):
                if s[i] == s[i-1] or ((i - 2 >= 0) and s[i] == s[i-2]):
                    s[i] = "?"
                i += 1
            for c in s:
                if c == "?":
                    ans += 1
            print(ans)


# calling main Function
if __name__ == '__main__':
    main()

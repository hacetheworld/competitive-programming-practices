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


def Solution():
    # Write Your Code Here
    color = ["R", "G", "B"]
    ans = 0
    n = get_int()
    s = [c for c in get_string()]
    for i in range(n-2):
        if s[i] == s[i+1] == s[i+2]:
            for co in color:
                if co != s[i] and co != s[i+2]:
                    break
            s[i+1] = co
            ans += 1
    for i in range(n-1):
        if s[i] == s[i+1]:
            for co in color:
                if i >= 1:
                    if co != s[i-1] and co != s[i+1]:
                        break
                else:
                    if co != s[i+1]:
                        break
            s[i] = co
            ans += 1
    print(ans)
    print("".join(s))


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()

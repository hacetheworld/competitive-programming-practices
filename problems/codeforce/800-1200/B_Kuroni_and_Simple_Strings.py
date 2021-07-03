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
    pass


def main():
    # Take input Here and Call solution function
    s = get_string()
    n = len(s)
    ans = []
    k = 0
    i = 0
    j = n-1
    while i < j:
        if s[i] == "(" and s[j] == ")":
            k += 1
            ans.append(i+1)
            ans.append(j+1)
            i += 1
            j -= 1
        # if j-i <= 1 and n-len(ans) <= 2:
        #     break
        if s[i] != "(":
            i += 1
        if s[j] != ")":
            j -= 1
    if k == 0:
        print(0)
    else:
        print(1)
        ans = sorted(ans)
        print(len(ans))
        print(*ans)


# calling main Function
if __name__ == '__main__':
    main()

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


def Solution(s):
    # Write Your Code Here
    n = len(s)
    op = 0
    indices = []
    i = 0
    while i < n-2:
        tmp = s[i:i+3]
        flg = True
        if i < n-4:
            tmp2 = s[i:i+5]
            if tmp2 == "twone":
                flg = False
                op += 1
                indices.append(i+3)
                i += 5
        if flg:
            if tmp == "one" or tmp == "two":
                op += 1
                indices.append(i+2)
                i += 3
            else:
                i += 1
    if len(indices) and indices[-1] < n and s[indices[-1]] == s[indices[-1]-1]:
        indices[-1] -= 1
    print(op)
    print(*indices)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        Solution(get_string())


# calling main Function
if __name__ == '__main__':
    main()

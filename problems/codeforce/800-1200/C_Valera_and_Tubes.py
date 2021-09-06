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


def Solution(n, m, k):
    # Write Your Code Here
    res = []
    for i in range(n):
        if i % 2 == 0:
            for j in range(m):
                res.append(i+1)
                res.append(j+1)
        else:
            for j in range(m-1, -1, -1):
                res.append(i+1)
                res.append(j+1)
    i = 0
    j = 0
    for k in range(k-1):
        tmp = [2]
        tmp.append(res[i])
        tmp.append(res[i+1])
        tmp.append(res[i+2])
        tmp.append(res[i+3])
        i += 4
        print(*tmp)
    t = 0
    tmp = []
    for j in range(i, len(res)):
        t += 1
        tmp.append(res[j])
    tmp.insert(0, t//2)
    print(*tmp)


def main():
    # Take input Here and Call solution function
    n, m, k = get_ints_in_variables()
    Solution(n, m, k)


# calling main Function
if __name__ == '__main__':
    main()

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


def check(tmp, res, n):
    cnt = 0
    for i in range(n):
        if tmp[i] == res[i]:
            cnt += 1
            continue
        if tmp[i] < res[i]:
            cnt += 1
            return [True, cnt]
        else:
            return [False, cnt]
    return [True, cnt]


def Solution(s, n):
    # Write Your Code Here
    res = s
    k = 1
    for j in range(2, n+1):
        tmp = []
        for i in range(j-1, n):
            tmp.append(s[i])
        if (len(s)-(j-1)) % 2:
            for i in range(j-2, -1, -1):
                tmp.append(s[i])
        else:
            for i in range(j-1):
                tmp.append(s[i])
        r = check(tmp, res, n)
        if r[0] and r[1] != n:
            res = tmp.copy()
            k = j
    print("".join(res))
    print(k)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        s = get_string()
        Solution(s, n)


# calling main Function
if __name__ == '__main__':
    main()

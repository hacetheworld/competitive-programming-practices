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


def Solution(a, b, n):
    # Write Your Code Here
    res = []
    for i in range(n):
        if a[i] == b[i]:
            continue
        req = abs(a[i]-b[i])
        for j in range(n):
            if req == 0:
                break
            if i == j:
                continue
            if a[i] < b[i] and a[j] > b[j]:
                tmp = min(req, abs(a[j]-b[j]))
                req -= (tmp)
                a[i] += tmp
                a[j] -= tmp
                for _ in range(tmp):
                    res.append([j+1, i+1])
            elif a[i] > b[i] and a[j] < b[j]:
                tmp = min(req, abs(a[j]-b[j]))
                req -= (tmp)
                a[i] -= tmp
                a[j] += tmp
                for _ in range(tmp):
                    res.append([i+1, j+1])

    # print(*a, "a")
    for i in range(n):
        if a[i] != b[i]:
            print(-1)
            return
    print(len(res))
    for v in res:
        print(*v)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        a = get_ints_in_list()
        b = get_ints_in_list()
        Solution(a, b, n)


# calling main Function
if __name__ == '__main__':
    main()

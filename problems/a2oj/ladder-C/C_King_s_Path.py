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
    x0, y0, x1, y1 = get_ints_in_variables()
    n = get_int()
    g = {}
    for _ in range(n):
        r, a, b = get_ints_in_variables()
        for i in range(a, b+1):
            g[(r, i)] = -1
    g[(x0, y0)] = 0
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [0, -1, 1, -1, 1, 0, -1, 1]
    queue = [(x0, y0)]
    while len(queue):
        node = queue.pop(0)
        for j in range(8):
            v = (node[0]+dx[j], node[1]+dy[j])
            # print(v, "v")
            if not v in g:
                continue
            if v in g and g[v] != -1:
                continue
            g[v] = g[node]+1
            queue.append(v)
    print(g[(x1, y1)])


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()

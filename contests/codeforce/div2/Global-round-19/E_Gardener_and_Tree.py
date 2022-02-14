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
    for _ in range(get_int()):
        input()
        n, k = get_ints_in_variables()
        g = [[] for _ in range(n)]
        remOp = [0 for _ in range(n)]
        layer = [0 for _ in range(n)]
        for _ in range(n-1):
            u, v = get_ints_in_variables()
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)
            remOp[u] += 1
            remOp[v] += 1
        queue = []
        for i in range(n):
            if remOp[i] == 1:
                queue.append(i)
                layer[i] = 1
        while len(queue) > 0:
            node = queue.pop(0)
            for child in g[node]:
                if remOp[child] != 1:
                    remOp[child] -= 1
                    if remOp[child] == 1:
                        queue.append(child)
                        layer[child] = (layer[node]+1)
        ans = 0
        for vi in range(n):
            if layer[vi] > k:
                ans += 1
        print(ans)


# calling main Function
if __name__ == '__main__':
    main()

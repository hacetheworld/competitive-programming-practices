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


def Solution(arr, n, m, k):
    # Write Your Code Here
    grid = [[0 for _ in range(m+1)] for _ in range(n+1)]
    queue = []
    for i in range(len(arr)):
        if i % 2 == 0:
            grid[arr[i]][arr[i+1]] = 1
            queue.append((i, i+1))
    visted = {}
    ans = queue[0]
    while len(queue) > 0:
        node = queue.pop(0)
        if node in visted:
            continue
        ans = node
        visted[node] = True
        x, y = node[0], node[1]
        if x+1 <= n and y <= m:
            queue.append((x+1, y))
        if x <= n and y+1 <= m:
            queue.append((x, y+1))
        if x-1 > 0 and y <= m:
            queue.append((x-1, y))
        if x <= n and y-1 > 0:
            queue.append((x, y-1))
    print(*ans)


def main():
    # Take input Here and Call solution function
    out = open('output.txt', 'w')
    inp = open('input.txt', 'r')

    n, m = map(int, inp.readline().split())
    k = int(inp.readline())
    arr = list(map(int, inp.readline().split()))

    Solution(arr, n, m, k)


# calling main Function
if __name__ == '__main__':
    main()

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


def Solution(arr, n):
    a = arr
    mini = [a[0]]
    maxi = [a[0]]
    s = set(a)
    vis = [i for i in range(1, n+1) if i not in s]
    vis2 = vis[:]
    i = 0
    j = len(vis)-1
    for k in range(1, n):
        if a[k] == a[k-1]:
            mini.append(vis[i])
            i += 1
            pos = bisect.bisect_left(vis2, a[k])
            if pos == 0:
                maxi.append(vis2[pos+1])
                vis2.pop(pos+1)
            else:
                maxi.append(vis2[pos-1])
                vis2.pop(pos-1)
        else:
            mini.append(a[k])
            maxi.append(a[k])
    print(*mini)
    print(*maxi)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()

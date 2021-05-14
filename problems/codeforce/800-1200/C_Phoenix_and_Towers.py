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


def Solution(arr, n, m, x):
    # Write Your Code Here
    print("YES")
    hp = []
    for i in range(m):
        heapq.heappush(hp, [0, i+1])
    for i in range(n):
        v = arr[i]
        p = heapq.heappop(hp)
        print(p[1], end=" ")
        heapq.heappush(hp, [p[0]+v, p[1]])
    print()


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, m, x = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, m, x)


# calling main Function
if __name__ == '__main__':
    main()

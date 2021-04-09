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


def Solution():
    # Write Your Code Here
    n, m = get_ints_in_variables()
    col = [0 for _ in range(n*m+1)]
    row = [0 for _ in range(n*m+1)]
    for i in range(n):
        s = sys.stdin.readline().strip().split()
        for j in range(m):
            col[int(s[j])] = j
    for i in range(m):
        s = sys.stdin.readline().strip().split()
        for j in range(n):
            row[int(s[j])] = j
    res = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, ((n*m)+1)):
        res[row[i]][col[i]] = i
    # print("ans")
    for i in range(n):
        for j in range(m):
            print(res[i][j], end=" ")
        print()


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        Solution()


# calling main Function
if __name__ == '__main__':
    main()

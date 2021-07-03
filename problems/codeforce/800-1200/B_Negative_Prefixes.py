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


def Solution(arr, pos, n):
    # Write Your Code Here
    ans = [arr[i] if pos[i] == 1 else "_" for i in range(n)]
    tmpArr = []
    for i in range(n):
        if pos[i] == 0:
            tmpArr.append(arr[i])
    tmpArr = sorted(tmpArr)
    for i in range(n):
        if ans[i] == "_":
            ans[i] = tmpArr.pop()
    print(*ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        pos = get_ints_in_list()
        Solution(arr, pos, n)


# calling main Function
if __name__ == '__main__':
    main()

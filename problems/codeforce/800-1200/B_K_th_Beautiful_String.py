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


def Solution(n, k):
    # Write Your Code Here
    move = 0
    ans = 0
    for i in range(1, k+1):
        ans += i
        move += 1
        if ans >= k:
            break
    f = n-move-1
    s = (f+1)+(ans-k)
    # print(f, s)
    for i in range(n):
        if f == i or s == i:
            print("b", end="")
        else:
            print("a", end="")
    print()


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        Solution(n, k)


# calling main Function
if __name__ == '__main__':
    main()

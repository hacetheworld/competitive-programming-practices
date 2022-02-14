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


def Solution(arr, n):
    # Write Your Code Here
    # print(arr)
    s = arr[0]
    for i in range(1, len(arr)):
        if s[-1]+arr[i][0] != arr[i] and s[-1]+arr[i][1] != arr[i]:
            s += arr[i][0]+arr[i][1]
        elif s[-1]+arr[i][0] == arr[i]:
            s += arr[i][0]
        else:
            s += arr[i][1]
    if len(s) != n:
        s += "a"
    print("".join(s))


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_string().split(" ")
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()

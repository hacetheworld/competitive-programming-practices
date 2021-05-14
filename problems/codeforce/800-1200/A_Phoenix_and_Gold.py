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
    pass


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, x = get_ints_in_variables()
        arr = get_ints_in_list()
        s = sum(arr)
        if s == x:
            print("NO")
        else:
            print("YES")
            s1 = 0
            for i in range(n):
                s1 += arr[i]
                if s1 == x:
                    tmp = arr[i]
                    arr[i] = arr[-1]
                    arr[-1] = tmp
                    s1 -= tmp
                    s1 += arr[i]
            print(*arr)


# calling main Function
if __name__ == '__main__':
    main()

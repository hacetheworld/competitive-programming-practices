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


def Solution(arr, n, k):
    # Write Your Code Here
    s1 = 0
    s2 = 0
    for i in range(1, n):
        s2 = s2 + arr[i - 1]
        s1 = s1 + arr[i - 1]
        if (((arr[i] / s1*(1.0*100))) > k):
            s = math.ceil((arr[i] * (1.0*100)) / k) - s1
            s1 = s1 + s
    print(s1-s2)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, k)


# calling main Function
if __name__ == '__main__':
    main()
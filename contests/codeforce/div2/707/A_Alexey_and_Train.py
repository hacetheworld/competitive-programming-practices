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


def Solution(arr, tm, n):
    # Write Your Code Herea
    arr.insert(0, [0, 0])
    arrival = 0
    # tm.insert(0, 0)
    pervisDep = 0
    for i in range(1, n+1):
        trvaelTime = abs(arr[i][0]-arr[i-1][1])
        arrival = pervisDep+trvaelTime+tm[i-1]
        wait = abs(arr[i][0]-arr[i][1])
        wait = math.ceil(wait/2)
        pervisDep = arrival+wait
        pervisDep = max(pervisDep, arr[i][1])

    print(arrival)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = [get_ints_in_list() for _ in range(n)]
        tm = get_ints_in_list()
        Solution(arr, tm, n)


# calling main Function
if __name__ == '__main__':
    main()

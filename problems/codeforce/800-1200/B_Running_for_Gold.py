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

    i = 0
    champ = 0
    while i < n:
        j = i+1
        f = 1
        while j < n:
            cnt = 0
            for l in range(5):
                if arr[i][l] < arr[j][l]:
                    cnt += 1
                if cnt == 3:
                    break
            if cnt != 3:
                f = 0
                i = j
                champ = j
                break
            else:
                j += 1
        if f:
            break
    flg = 1
    for i in range(n):
        if champ == i:
            continue
        cnt = 0
        for l in range(5):
            if arr[i][l] > arr[champ][l]:
                cnt += 1
            if cnt == 3:
                break
        if cnt != 3:
            flg = 0
            break
    if flg:
        print(champ+1)
    else:
        print(-1)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = [get_ints_in_list() for _ in range(n)]
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()

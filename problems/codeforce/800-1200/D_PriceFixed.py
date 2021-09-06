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


def Solution(a, n):
    # Write Your Code Here
    arr = sorted(a, key=lambda x: x[1])
    # print(arr)
    i = 0
    j = n-1
    atLeast = arr[0][1]
    BoughtProduct = 0
    ans = 0
    while i <= j:
        if BoughtProduct < atLeast:
            tmp = min([atLeast-BoughtProduct, arr[j][0]])
            BoughtProduct += (tmp)
            arr[j][0] -= tmp
            ans += (2*tmp)
        if BoughtProduct >= atLeast:
            tmp = arr[i][0]
            ans += tmp
            BoughtProduct += (tmp)
            arr[i][0] = 0
            i += 1
            if i <= j:
                atLeast = arr[i][1]
            else:
                break
        else:
            j -= 1
    print(ans)


def main():
    # Take input Here and Call solution function
    n = get_int()
    arr = get_list_of_list(n)
    Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()

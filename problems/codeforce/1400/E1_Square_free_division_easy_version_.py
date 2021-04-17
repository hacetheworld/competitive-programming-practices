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


def Solution(arr, n, l, perfectSquares):
    # Write Your Code Here
    ans = 1
    i = 0
    temp = []
    while i < n:
        f = 0
        temp.append(arr[i])
        # print(temp)
        for j in range(i+1, n):
            flag = True
            f = 1
            for k in range(len(temp)):
                if (arr[j]*temp[k]) in perfectSquares:
                    flag = False
                    break
            if flag:
                temp.append(arr[j])
                i += 1
            else:
                temp = []
                i += 1
                ans += 1
                break
        if not f:
            break
    print(ans)


def main():
    # Take input Here and Call solution function
    perfectSquares = {}
    for v in range(1, pow(10, 5)):
        perfectSquares[v*v] = True
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, k, perfectSquares)


# calling main Function
if __name__ == '__main__':
    main()

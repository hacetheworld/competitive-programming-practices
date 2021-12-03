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


def swapCol(arr, i, j, k):
    tmp = arr[i][j]
    arr[i][j] = arr[i][k]
    arr[i][k] = tmp


def swapRow(arr, i, j):
    tmp = [v for v in arr[i]]
    for k in range(len(arr[0])):
        arr[i][k] = arr[j][k]
    for k in range(len(arr[0])):
        arr[j][k] = tmp[k]


def Solution(arr, n):
    # Write Your Code Here
    ans = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                for k in range(j, n):
                    if arr[i][k] == 1:
                        ans.append([2, j+1, k+1])
                        swapCol(arr, i, j, k)
    for i in range(n-1, -1, -1):
        prev = -1
        id = i
        for j in range(i):
            if sum(arr[j]) > prev:
                prev = sum(arr[j])
                id = j
        if prev != -1 and prev > sum(arr[i]):
            ans.append([1, i+1, id+1])
            swapRow(arr, i, id)
    for i in range(n-1, 0, -1):
        j = i-1
        k = 0
        while k < j:
            if arr[i][j] == 1 or arr[i][k] == 0:
                break
            if arr[i][k] == 1:
                ans.append([2, j+1, k+1])
                arr[i][k], arr[i][j] = arr[i][j], arr[i][k]
                j -= 1
                k += 1

    print(len(ans))
    for v in ans:
        print(*v)


def main():
    # Take input Here and Call solution function
    n = get_int()
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(n-1):
        x, y = get_ints_in_variables()
        matrix[x-1][y-1] = 1
    Solution(matrix, n)


# calling main Function
if __name__ == '__main__':
    main()

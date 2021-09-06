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


def Solution(arr, k):
    # Write Your Code Here
    tmpArr = []
    for i in range(k):
        sm = sum(arr[i])
        for j in range(len(arr[i])):
            tmp = [sm-arr[i][j], i+1, j+1]
            tmpArr.append(tmp)
    tmpArr = sorted(tmpArr, key=lambda x: x[0])
    for i in range(len(tmpArr)-1):
        if tmpArr[i][0] == tmpArr[i+1][0] and tmpArr[i][1] != tmpArr[i+1][1]:
            print("YES")
            print(tmpArr[i][1], tmpArr[i][2])
            print(tmpArr[i+1][1], tmpArr[i+1][2])
            return
    print("NO")


def main():
    # Take input Here and Call solution function
    k = get_int()
    arr = []
    for _ in range(k):
        get_int()
        tmp = get_ints_in_list()
        arr.append(tmp)
    Solution(arr, k)


# calling main Function
if __name__ == '__main__':
    main()

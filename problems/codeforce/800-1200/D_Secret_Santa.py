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
    hm = {}
    for v in arr:
        if v in hm:
            hm[v] += 1
        else:
            hm[v] = 1
    cnt = 0
    for v in hm:
        if hm[v] > 1:
            cnt += (hm[v]-1)
    nums = []
    for i in range(1, n+1):
        if i in hm:
            continue
        nums.append(i)
    bArr = [-1 for _ in range(n)]
    for i in range(n):
        if hm[arr[i]] > 0:
            bArr[i] = arr[i]
            hm[arr[i]] = 0
        else:
            bArr[i] = nums.pop()
    for i in range(n):
        if arr[i] == bArr[i]:
            continue
        if bArr[i] == i+1:
            idx = -1
            for j in range(n):
                if j == i:
                    continue
                if arr[i] == arr[j]:
                    idx = j
                    break
            tmp = bArr[i]
            bArr[i] = bArr[idx]
            bArr[idx] = tmp
            break
    print(n-cnt)
    print(*bArr)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()

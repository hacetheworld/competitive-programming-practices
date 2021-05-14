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
    n, k = get_ints_in_variables()
    arr = get_ints_in_list()
    res = []
    tmpArr = []
    for j in range(n):
        for i in range(1, arr[j]+1):
            tmpArr.append(i)
    tmp = 0
    for i in range(k):
        tmp += tmpArr[i]
    res.append(tmp)
    for i in range(1, len(tmpArr)):
        tmp -= tmpArr[i-1]
        tmp += (tmpArr[((i+k)-1) % len(tmpArr)])
        res.append(tmp)
    print(max(res))


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()

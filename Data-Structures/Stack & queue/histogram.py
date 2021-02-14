# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638

# import inbuilt standard input output
import sys
import math
from sys import stdin, stdout


def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_string(): return sys.stdin.readline().strip()


def get_signle_int(): return int(input())


def Solution(arr, n):
    leftNearestSmallElStk = []
    rightNearesSmalltElStk = []
    leftNearestSmallEl = []
    rightNearestSmallEl = []
    i = 0
    j = n-1
    while i < n and j >= 0:
        leftEl = arr[i]
        while len(leftNearestSmallElStk) > 0 and leftNearestSmallElStk[-1][0] >= leftEl:
            leftNearestSmallElStk.pop()
        if len(leftNearestSmallElStk) == 0:
            leftNearestSmallEl.append(-1)
        else:
            leftNearestSmallEl.append(leftNearestSmallElStk[-1][1])

        leftNearestSmallElStk.append([leftEl, i])
        i += 1
        # //Right nearest Smalll el
        rightEl = arr[j]
        while len(rightNearesSmalltElStk) > 0 and rightNearesSmalltElStk[-1][0] >= rightEl:
            rightNearesSmalltElStk.pop()
        if len(rightNearesSmalltElStk) == 0:
            rightNearestSmallEl.append(n)
        else:
            rightNearestSmallEl.append(rightNearesSmalltElStk[-1][1])

        rightNearesSmalltElStk.append([rightEl, j])
        j -= 1
    rightNearestSmallEl = list(reversed(rightNearestSmallEl))
    res = []
    for i in range(n):
        l = leftNearestSmallEl[i]+1
        r = rightNearestSmallEl[i]-1
        v = max((abs(i-l)+abs(r-i)+1)*arr[i], arr[i])
        res.append(v)
    print(res)


def main():
    # //TAKE INPUT HERE
    n = get_signle_int()
    arr = get_ints_in_list()
    Solution(arr, n)


#  call the main method  pa
if __name__ == "__main__":
    main()

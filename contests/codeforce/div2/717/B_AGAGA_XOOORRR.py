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
    pass


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        ans = arr[0]
        for i in range(1, n):
            ans ^= arr[i]
        if ans == 0:
            print("YES")
        else:
            pre = [arr[0]]
            for i in range(1, n):
                pre.append(pre[-1] ^ arr[i])
            flag = 0
            for i in range(n-2):
                st = pre[i]
                for j in range(i+1, n-1):
                    mid = pre[j] ^ pre[i]
                    en = pre[n-1] ^ pre[j]
                    if(st == mid and mid == en):
                        flag = 1
                        break
                if(flag):
                    break

            if flag:
                print("YES")
            else:
                print("NO")


# calling main Function
if __name__ == '__main__':
    main()

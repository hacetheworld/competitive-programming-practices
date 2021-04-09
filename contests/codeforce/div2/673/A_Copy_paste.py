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


def Solution(arr,n,k):
    # Write Your Code Here
    mn = min(arr)
    ans=0
    flag = False
    for v in arr:
        if not flag and v==mn:
            flag=True
        else:
            ans+=(math.floor((k-v)/mn))
    print(ans)



def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n,k=get_ints_in_variables()
        arr=get_ints_in_list()
        Solution(arr,n,k)


# calling main Function
if __name__ == '__main__':
    main()

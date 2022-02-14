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

def Solution(n,c):
    # Write Your Code Here
    res=[0 for _ in range(n)]
    if c<n-1:
        return "IMPOSSIBLE"
    if c>(n//2)*n:
        return "IMPOSSIBLE"
    i=0
    j=n-1
    while i<=j:
        res[i]=j+1
        res[j]=i+1
        c-=((j-i)+1)
        if c




def main():
    # Take input Here and Call solution function
    for t in range(get_int()):
        n,c=get_ints_in_variables()
        print("Case #{}: {}".format(t+1, Solution(n,c)))


# calling main Function
if __name__ == '__main__':
    main()

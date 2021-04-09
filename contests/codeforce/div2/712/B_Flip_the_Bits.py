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


def Solution(a, b, n):
    # Write Your Code Here
    onesCount = 0
    zeroCount = 0
    for c in a:
        if c == "1":
            onesCount += 1
        else:
            zeroCount += 1

    if a == b:
        print("YES")
    else:
        flag = True
        changed = False
        for i in range(n-1, -1, -1):
            if ((a[i] != b[i] and not changed) or (a[i] == b[i] and changed)):
                if(zeroCount == onesCount):
                    changed = not changed
                else:
                    flag = False
                    break
            if a[i] == "1":
                onesCount -= 1
            else:
                zeroCount -= 1
        if flag:
            print("YES")
        else:
            print("NO")


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        a = get_string()
        b = get_string()
        Solution(a, b, n)


# calling main Function
if __name__ == '__main__':
    main()

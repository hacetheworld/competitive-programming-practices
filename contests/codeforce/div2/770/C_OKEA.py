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


def Solution(n, k):
    # Write Your Code Here
    if n == 1 and k == 1:
        print("YES")
        print(1)
        return
    if k == 1:
        print("YES")
        for i in range(n):
            print(i+1)
        return
    if n == 1 or n % 2:
        print("NO")
        return
    else:
        frm = 1
        print("YES")
        for i in range(2, n+2, 2):
            for j in range(frm, ((i)*k)+1):
                if j % 2:
                    print(j, end=" ")
            print()
            for j in range(frm, ((i)*k)+1):
                if j % 2 == 0:
                    print(j, end=" ")
            frm = ((i)*k)+1
            print()


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        Solution(n, k)


# calling main Function
if __name__ == '__main__':
    main()

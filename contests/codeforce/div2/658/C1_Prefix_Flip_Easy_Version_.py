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


def operation(s, i):
    l = 0
    r = i
    while l <= r:
        tmp = s[l]
        s[l] = s[r]
        s[r] = tmp
        l += 1
        r -= 1
    for j in range(i+1):
        s[j] = "0" if s[j] == "1" else "1"
    return s


def Solution(a, b, n):
    # Write Your Code Here
    a = [c for c in a]
    j = 0
    count = 0
    op = []
    for i in range(n-1, -1, -1):
        if a[i] != b[i]:
            if a[j] == b[i]:
                count += 1
                op.append(j+1)
                a = operation(a, j)
            count += 1
            op.append(i+1)
            a = operation(a, i)
        # j += 1
    print(count, *op)


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

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


def Solution(s, n):
    # Write Your Code Here
    if s[0] == "0" or s[-1] == "0":
        print("NO")
        return
    one = 0
    zero = 0

    for c in s:
        if c == "1":
            one += 1
        else:
            zero += 1
    if one % 2 != 0 or zero % 2 != 0:
        print("NO")
        return
    a = []
    b = []
    c1 = 1
    c2 = 0
    for c in s:
        if c == "1":
            if c1 <= one//2:
                a.append("(")
                b.append("(")

            else:
                a.append(")")
                b.append(")")
            c1 += 1
        else:
            if c2 == 0:
                a.append("(")
                b.append(")")
            else:
                a.append(")")
                b.append("(")
            c2 ^= 1
    print("YES")
    print("".join(a))
    print("".join(b))


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        s = get_string()
        Solution(s, n)


# calling main Function
if __name__ == '__main__':
    main()

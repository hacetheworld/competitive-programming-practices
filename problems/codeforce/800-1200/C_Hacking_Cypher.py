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


def power(a, b, mod):
    res = 1
    while b > 0:
        if b & 1:
            res = (res*a) % mod
        a = (a*a) % mod
        b = b//2
    return res


def Solution(z, a, b):
    # Write Your Code Here
    tmp = 0
    left = []
    right = {}
    for i in range(len(z)-1):
        tmp *= 10
        tmp += int(z[i])
        tmp = tmp % a
        if tmp == 0 and z[i+1] != "0":
            left.append(i)
    rem = 0
    for i in range(len(z)-1, -1, -1):
        if z[i] != "0":
            rem_contb = power(10, len(z)-i-1, b)*int(z[i])
            rem_contb = rem_contb % b
            rem += rem_contb
            rem = rem % b
            if rem == 0:
                right[i] = i
    for i in left:
        if i+1 in right:
            print("YES")
            for j in range(i+1):
                print(z[j], end="")
            print()
            for j in range(right[i+1], len(z)):
                print(z[j], end="")
            print()
            return
    print("NO")


def main():
    # Take input Here and Call solution function
    z = input()
    a, b = get_ints_in_variables()
    Solution(z, a, b)


# calling main Function
if __name__ == '__main__':
    main()

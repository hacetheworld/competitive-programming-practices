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


def isPalindrome(s, n):
    i = 0
    j = n-1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def Solution(s, n):
    # Write Your Code Here
    s = [c for c in s]
    zeroCount = 0
    for c in s:
        if c == "0":
            zeroCount += 1
    if isPalindrome(s, n):
        if zeroCount == 1 or zeroCount % 2 == 0:
            print("BOB")
        else:
            print("ALICE")
    else:
        idx = 0
        if zeroCount == 2:
            for i in range(n):
                tmp = s.copy()
                if s[i] == "0":
                    tmp[i] = "1"
                if isPalindrome(tmp, n):
                    idx = 1
                    break
        if idx == 1:
            print("DRAW")
        else:
            print("ALICE")


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        Solution(get_string(), n)


# calling main Function
if __name__ == '__main__':
    main()

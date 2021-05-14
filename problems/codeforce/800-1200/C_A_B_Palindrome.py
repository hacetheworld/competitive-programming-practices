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


def isPalindrome(s):
    i = 0
    j = len(s)-1
    flag = True
    while i <= j:
        if s[i] != s[j]:
            flag = False
            break
        i += 1
        j -= 1
    return flag


def Solution(s, a, b):
    # Write Your Code Here
    s = [c for c in s]
    n = len(s)
    for i in range(n//2):
        if s[i] == "?" and s[n-i-1] != "?":
            s[i] = s[n-i-1]
        if s[i] != "?" and s[n-i-1] == "?":
            s[n-i-1] = s[i]
    countZero = 0
    countOne = 0
    countMark = 0
    for c in s:
        if c == "0":
            countZero += 1
        elif c == "1":
            countOne += 1
        else:
            countMark += 1
    a = a-countZero
    b = b-countOne
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] == "?":
            if a > b:
                s[i] = "0"
                s[j] = "0"
                a -= 2
            else:
                s[i] = "1"
                s[j] = "1"
                b -= 2
        i += 1
        j -= 1
    for i in range(n):
        if s[i] == "?":
            if a > b:
                s[i] = "0"
                s[n-i-1] = "0"
                a -= 1
            else:
                s[i] = "1"
                s[n-i-1] = "1"
                b -= 1
    if a == 0 and b == 0 and isPalindrome(s):
        print("".join(s))
    else:
        print(-1)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        a, b = get_ints_in_variables()
        s = get_string()
        Solution(s, a, b)


# calling main Function
if __name__ == '__main__':
    main()

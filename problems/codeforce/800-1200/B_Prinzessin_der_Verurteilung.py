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
    res = [0 for _ in range(26)]
    for c in s:
        res[ord(c)-97] = 1
    for i in range(26):
        if res[i] == 0:
            print(chr(i+97))
            return
    res = []
    for i in range(n-1):
        temp = ""
        temp += s[i]
        temp += s[i+1]
        res.append(temp)
    for i in range(26):
        for j in range(26):
            st = chr(97+i)
            st += chr(97+j)
            if s.find(st) == -1:
                print(st)
                return
    res = []
    for i in range(n-2):
        temp = ""
        temp += s[i]
        temp += s[i+1]
        temp += s[i+2]
        res.append(temp)
    for i in range(26):
        for j in range(26):
            for k in range(26):
                st = chr(97+i)
                st += chr(97+j)
                st += chr(97+k)
                if s.find(st) == -1:
                    print(st)
                    return


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        s = get_string()
        Solution(s, n)


# calling main Function
if __name__ == '__main__':
    main()

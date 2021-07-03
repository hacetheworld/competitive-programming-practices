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


def helper(s, tmp):
    pass


def Solution(s):
    # Write Your Code Here
    hm = {}
    chars = "ATON"
    for c in chars:
        hm[c] = 0
    for c in s:
        if c in hm:
            hm[c] += 1
        else:
            hm[c] = 0
    ans = float("inf")
    ansStr = ""
    permutaions = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    permstr = chars[i]+chars[j]+chars[k]+chars[l]
                    permutaions.append(permstr)

    while len(permutaions):
        tmp = []
        newStr = permutaions.pop()
        for c in newStr:
            for _ in range(hm[c]):
                tmp.append(c)
        tmpAns = helper(s, tmp)
        if tmpAns < ans:
            ansStr = tmp
            ans = tmpAns
    print("".join(ansStr))


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        Solution(get_string())


# calling main Function
if __name__ == '__main__':
    main()

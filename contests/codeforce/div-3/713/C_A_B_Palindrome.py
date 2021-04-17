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


def Solution(s, a, b):
    # Write Your Code Here
    if a % 2 != 0 and b % 2 != 0:
        print(-1)
        return
    zeroCount = 0
    oneCount = 0
    for c in s:
        if c == "0":
            zeroCount += 1
        elif c == "1":
            oneCount += 1
    temp = [c for c in s]
    quest = len(s)-(zeroCount+oneCount)
    zeroCount = a-zeroCount
    oneCount = a-oneCount
    l = 0
    r = len(s)-1
    flag = True
    while l <= r:
        if temp[l] == temp[r]:
            if temp[l] == "1":
                oneCount -= 2
            elif temp[r] == "0":
                zeroCount -= 2
            else:
                quest -= 2
                if oneCount > 2:
                    temp[l] = "1"
                    temp[r] = "1"
                else:
                    temp[l] = "0"
                    temp[r] = "0"
        else:
            if temp[l] == "1" and temp[r] == "0" or temp[l] == "0" and temp[r] == "1":
                flag = False
                break
            elif temp[l] == "?" and temp[r] == "0":
                temp[l] = "0"
                zeroCount -= 2
            elif temp[l] == "0" and temp[r] == "?":
                temp[r] = "0"
                zeroCount -= 2
            elif temp[l] == "?" and temp[r] == "1":
                temp[l] = "1"
                oneCount -= 2
            elif temp[l] == "1" and temp[r] == "?":
                temp[r] = "1"
                oneCount -= 2
        if zeroCount < 0 or oneCount < 0:
            flag = False
            break
        l += 1
        r -= 1
    if flag:
        print("".join(temp))
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

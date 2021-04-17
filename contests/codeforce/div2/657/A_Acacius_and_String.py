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
    op = "abacaba"
    count = 0
    for i in range((n-len(op))+1):
        l = 0
        flag = 1
        while l < len(op):
            if s[i+l] != op[l]:
                flag = 0
                break
            l += 1
        if flag:
            count += 1
    if count > 1:
        print("NO")
        return

    if count == 1:
        temp = [c for c in s]
        for i in range(n):
            if temp[i] == "?":
                temp[i] = "z"
        print("YES")
        print("".join(temp))
        return

    for i in range((n-len(op))+1):
        temp = [c for c in s]
        for j in range(7):
            if temp[j+i] == '?':
                temp[j+i] = op[j]
        count = 0
        for j in range((n-len(op))+1):
            l = 0
            flag = 1
            while l < len(op):
                if temp[j+l] != op[l]:
                    flag = 0
                    break
                l += 1
            if flag:
                count += 1
        if count == 1:
            for k in range(n):
                if temp[k] == "?":
                    temp[k] = "z"
            print("YES")
            print("".join(temp))
            return
    print("NO")


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        s = get_string()
        Solution(s, n)


# calling main Function
if __name__ == '__main__':
    main()

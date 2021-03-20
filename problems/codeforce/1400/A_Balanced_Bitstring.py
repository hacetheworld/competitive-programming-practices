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


def Solution(s, n, k):
    s = [c for c in s]
    flag = False
    for i in range(k):
        temp = s[i]
        j = i+k
        while j < n:
            if temp == "0" and s[j] == "1":
                flag = True
                break
            elif temp == "1" and s[j] == "0":
                flag = True
                break
            elif temp == "?" and s[j] != "?":
                temp = s[j]
            j += k
        if flag:
            break
        s[i] = temp
    if flag:
        print("NO")
        return
    else:
        one = 0
        zero = 0
        questionMark = 0
        for i in range(k):
            if s[i] == "0":
                zero += 1
            elif s[i] == "1":
                one += 1
            else:
                questionMark += 1
        if zero > (k//2) or one > (k//2):
            print("NO")
        else:
            print("YES")


def main():
    # //Write Your Code Here
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        s = get_string()
        Solution(s, n, k)
        # print("HELLO")


# calling main Function
if __name__ == '__main__':
    main()

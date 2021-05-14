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


def Solution(a, b):
    # Write Your Code Here
    ans = 0
    for i in range(len(a)):
        for j in range(len(b)):
            temp = 0
            if a[i] == b[j]:
                k = j
                l = i
                while l < len(a) and k < len(b) and a[l] == b[k]:
                    temp += 1
                    k += 1
                    l += 1
                ans = max(temp, ans)
    # print(ans)
    print((len(a)+len(b))-(2*ans))


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        a = get_string()
        b = get_string()
        Solution(a, b)


# calling main Function
if __name__ == '__main__':
    main()

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


def Solution(p, q):
    # Write Your Code Here
    if p % q != 0 or q > p:
        print(p)
        return
    res = 1
    for i in range(1, round(math.sqrt(q))+1):
        if q % i == 0:
            x = p
            while i != 1 and x % i == 0:
                x = x//i
                if x % q != 0:
                    res = max(res, x)
                    break
            x = p
            while x % (q//i) == 0:
                x = x//(q//i)
                if x % q != 0:
                    res = max(res, x)
                    break
    print(res)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        p, q = get_ints_in_variables()
        Solution(p, q)


# calling main Function
if __name__ == '__main__':
    main()

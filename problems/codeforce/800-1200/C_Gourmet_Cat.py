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


def Solution():
    # Write Your Code Here
    pass


def main():
    # Take input Here and Call solution function
    a, b, c = get_ints_in_variables()
    a1 = a//3
    b1 = b//2
    c1 = c//2
    t = min(a1, b1, c1)
    ans = t*7
    a -= (t*3)
    b -= (t*2)
    c -= (t*2)
    idx = [0, 1, 2, 3, 1, 3, 2, 1]
    arr = [a, b, c]
    newANs = ans
    for i in range(1, 8):
        tmpArr = [c for c in arr]
        tmpArr.insert(0, 0)
        day = i
        tmpAns = 0
        while tmpArr[idx[day]] > 0:
            tmpAns += 1
            tmpArr[idx[day]] -= 1
            day = (day % 7)+1
        ans = max(newANs+tmpAns, ans)

    print(ans)


# calling main Function
if __name__ == '__main__':
    main()

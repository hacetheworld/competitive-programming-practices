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


def Solution(a, b, n):
    # Write Your Code Here
    mod = pow(10, 9)+7
    aPos = {}
    for i in range(n):
        aPos[a[i]] = i
    st = set()
    for i in range(n):
        st.add(i)
    ans = 0
    while len(st):
        tmpRes = []
        for x in st:
            y = aPos[b[x]]
            tmpRes.append(x)
            while y != x:
                tmpRes.append(y)
                y = aPos[b[y]]
            break
        for v in tmpRes:
            st.remove(v)
        ans += 1
    print(2**ans % mod)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        a = get_ints_in_list()
        b = get_ints_in_list()
        Solution(a, b, n)


# calling main Function
if __name__ == '__main__':
    main()

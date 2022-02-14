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
    if a == b:
        print(0)
        return
    if ((not "1" in a) and "1" in b) or (not "0" in a and not"1" in b):
        print(-1)
        return
    oz = 0
    zo = 0
    for i in range(n):
        if a[i]+b[i] == "10":
            oz += 1
        elif a[i]+b[i] == "01":
            zo += 1

    ans = float("inf")
    if zo == oz == 0:
        print(0)
        return
    if zo == oz:
        ans = min(2*zo, ans)
    a = [c for c in a]
    j = -1
    for i in range(n):
        if a[i] == b[i] == "1":
            j = i
            break
    if j != -1:
        oz = 0
        zo = 0
        for i in range(n):
            if i == j:
                continue
            a[i] = "1" if a[i] == "0" else "0"
        for i in range(n):
            if a[i]+b[i] == "10":
                oz += 1
            elif a[i]+b[i] == "01":
                zo += 1
        if zo == oz:
            ans = min((2*zo)+1, ans)
    print(-1 if ans == float("inf") else ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        a = get_string()
        b = get_string()
        Solution(a, b, n)


# calling main Function
if __name__ == '__main__':
    main()

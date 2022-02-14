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


def Solution(a, n):
    # Write Your Code Here
    i = 1
    j = n-2
    ans = 0
    while i <= j:
        while i < n and a[i] % 2 == 0:
            i += 1
        while j > 0 and a[j] % 2 == 0:
            j -= 1
        if i > j:
            break
        if i < j:
            if max(a[i], a[j]) > 1 and (a[i] >= a[j] or a[j] >= a[i]):
                a[i] -= 1
                a[j] -= 1
                ans += 2
            else:
                f = 0
                for k in range(i+1, j):
                    if a[k] >= 2:
                        f = 1
                        break
                if f:
                    a[i] += 1
                    a[j] += 1
                    a[k] -= 2
                    ans += 1
                else:
                    f = 1
                    for k in range(1, n-1):
                        if k == i:
                            continue
                        if a[k] >= 2:
                            f = 0
                            break
                    if f:
                        print(-1)
                        return
                    a[k] -= 2
                    a[i] -= 1
                    a[j] += 1
                    ans += 2
        elif i == j:
            f = 1
            for k in range(1, n-1):
                if k == i or k == j:
                    continue
                if a[k] >= 2:
                    f = 0
                    break
            if f:
                print(-1)
                return
            a[k] -= 2
            a[i] += 1
            ans += 1
        i += 1
        j -= 1
    for i in range(1, n-1):
        ans += (a[i]//2)
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        a = get_ints_in_list()
        Solution(a, n)


# calling main Function
if __name__ == '__main__':
    main()

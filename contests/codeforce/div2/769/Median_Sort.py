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


def query(i, j, k):
    print(i, j, k)
    return get_int()


def findPos(arr, el):
    l = 0
    r = len(arr)-1
    while l <= r:
        m1 = l+(r-l)//3
        m2 = r-(r-l)//3
        x = query(arr[l], el, arr[m1])
        if x == el:
            if m2-m1 == 1:
                arr.insert(l, el)
                break
            l = m1+1
            r = m2
        elif x == arr[m1]:
            r = m1
        else:
            l = m2
        if r <= l:
            arr.insert(r, el)
            break


def Solution(t, n, q):
    # Write Your Code Here

    for _ in range(t):
        ans = []
        x = query(1, 2, 3)
        ans = [1+x % 3, x, 1+(x+1) % 3]
        for el in range(4, n+1):
            findPos(ans, el)
        print(*ans)


def main():
    # Take input Here and Call solution function
    t, n, q = get_ints_in_variables()
    Solution(t, n, q)


# calling main Function
if __name__ == '__main__':
    main()

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
    for _ in range(get_int()):
        ch, ca = get_ints_in_variables()
        mc, ma = get_ints_in_variables()
        k, w, a = get_ints_in_variables()
        f = 0
        mat = myceil(ch, ma)
        chat = myceil(mc, ca)
        if mat >= chat:
            f = 1
            print("YES")
            continue
        for i in range(k):
            wup = k-i
            aup = i
            mat = myceil(ch+(wup*a), ma)
            chat = myceil(mc, ca+(aup*w))
            if mat >= chat:
                f = 1
                print("YES")
                break
            wup = i
            aup = k-i
            mat = myceil(ch+(wup*a), ma)
            chat = myceil(mc, ca+(aup*w))
            # print(mat, chat, ca+(aup*a), "jkj")
            if mat >= chat:
                f = 1
                print("YES")
                break

        if f == 0:
            print("NO")


# calling main Function
if __name__ == '__main__':
    main()

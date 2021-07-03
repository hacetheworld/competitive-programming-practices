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


def Solution(s, a, b, p):
    # Write Your Code Here
    # 3 2 8
    # AABBBBAABB
    # [0,2,6,8]
    n = len(s)
    store = []
    prev = s[0]
    store.append(0)
    for i in range(1, n):
        if prev != s[i]:
            store.append(i)
            prev = s[i]
    store.append(n-1)
    money = 0
    ans = 0
    # print(store)
    m = len(store)-2
    if s[-1] != s[n-2]:
        m = len(store)-3
    for i in range(m, -1, -1):
        if s[store[i]] == "B":
            if b+money <= p:
                money += b
            else:
                ans = store[i+1]
                break
        else:
            if a+money <= p:
                money += a
            else:
                ans = store[i+1]
                break
    # print(store)
    print(ans+1)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        a, b, p = get_ints_in_variables()
        s = get_string()
        Solution(s, a, b, p)


# calling main Function
if __name__ == '__main__':
    main()

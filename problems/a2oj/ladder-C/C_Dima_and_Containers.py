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
    n = get_int()
    arr = [get_int() for _ in range(n)]
    u = [0 for _ in range(n)]
    hp = []
    # print(arr,"arr")
    for i, x in enumerate(arr):
        if x:
            heapq.heappush(hp, (-x, i))
        else:
            for t in [1, 2, 3]:
                if len(hp) > 0:
                    x, j = heapq.heappop(hp)
                    u[j] = t
                    u[i] += 1
            hp = []
    push = ['pushBack', 'pushStack', 'pushQueue', 'pushFront']
    pop = ['popStack', 'popQueue', 'popFront']
    for i, x in enumerate(arr):
        if x:
            print(push[u[i]])
        else:
            if u[i]:
                print(str(u[i])+" "+" ".join(pop[:u[i]]))
            else:
                print("0")


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()

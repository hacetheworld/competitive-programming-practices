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


def Solution(arr, n, m, hm):
    # Write Your Code Here
    limt = myceil(m, 2)
    # print(limt, "limt")
    res = [-1 for _ in range(m)]
    flag = True
    # print(hm)
    # print(arr)
    arr = sorted(arr)
    for friend in arr:
        day = friend.pop()
        for i in range(1, len(friend)):
            if hm[friend[i]][1] < limt:
                res[day] = friend[i]
                hm[friend[i]][1] += 1
                flag = False
                break
        if flag:
            flag = False
            break
        else:
            flag = True
    # print(hm)

    if flag:
        print("YES")
        print(*res)
    else:
        print("NO")


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, m = get_ints_in_variables()
        hm = {}
        arr = []
        for day in range(m):
            friend = get_ints_in_list()

            for i in range(1, len(friend)):
                if friend[i] in hm:
                    hm[friend[i]][0] += 1
                else:
                    hm[friend[i]] = [1, 0]
            friend.append(day)
            arr.append(friend)
        # print(hm)
        Solution(arr, n, m, hm)


# calling main Function
if __name__ == '__main__':
    main()

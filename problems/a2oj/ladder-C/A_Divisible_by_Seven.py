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


def permutaion(s, permt):
    if len(s) == 4:
        permt.append(s)
        return
    if not "1" in s:
        permutaion(s+"1", permt)
    if not "6" in s:
        permutaion(s+"6", permt)
    if not "8" in s:
        permutaion(s+"8", permt)
    if not "9" in s:
        permutaion(s+"9", permt)


def Solution():
    # Write Your Code Here
    n = get_string()
    remArr = ["1869", "6198", "1896", "9186", "9168", "6189", "8691"]
    arr = [0 for _ in range(10)]
    for c in n:
        arr[int(c)] += 1
    for c in "1689":
        arr[int(c)] -= 1
    rem = 0
    for i in range(1, 10):
        while arr[i] > 0:
            print(i, end="")
            rem = rem*10+i
            rem = rem % 7
            arr[i] -= 1
    print(remArr[rem], end="")
    for c in range(arr[0]):
        print(0, end="")
    print()


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()

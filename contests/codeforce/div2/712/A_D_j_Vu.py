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

# -------------- SOLUTION FUNCTION ------------------


def Solution(s, n):
    # Write Your Code Here
    count = 0
    for c in s:
        if c == "a":
            count += 1
    if count == n:
        print("NO")
    else:
        print("YES")

        r = []
        for i in range(n):
            r.append(s[i])
        i = 0
        for c in s:
            if c == "a":
                i += 1
            else:
                break
        for j in range(n-1, -1, -1):
            if s[j] == "a":
                i -= 1
            else:
                break
        if i <= 0:
            r.append("a")
        else:
            r.insert(0, "a")
        print("".join(r))


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        s = get_string()
        Solution(s, len(s))


# calling main Function
if __name__ == '__main__':
    main()

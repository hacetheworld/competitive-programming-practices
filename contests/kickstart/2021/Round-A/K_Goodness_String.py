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


def Solution(s, n, k):
    # Write Your Code Here
    notMatched = 0
    matched = 0
    i = 0
    j = n-1
    while i < j:
        if s[i] != s[j]:
            notMatched += 1
        else:
            matched += 1
        i += 1
        j -= 1
    ans = 0
    if notMatched == k:
        return ans
    elif notMatched > k:
        ans = abs(notMatched-k)
    else:
        ans = abs((k-notMatched))
    return ans


def main():
    # Take input Here and Call solution function
    for t in range(get_int()):
        n, k = get_ints_in_variables()
        s = get_string()
        # strArr = [input() for _ in range(N)]
        print("Case #{}: {}".format(t+1, Solution(s, n, k)))


# calling main Function
if __name__ == '__main__':
    main()

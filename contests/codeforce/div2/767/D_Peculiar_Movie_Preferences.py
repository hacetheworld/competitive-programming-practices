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


def reverIt(a, i, n):
    j = n
    while i < j:
        t = a[i]
        a[i] = a[j]
        a[j] = t
        i += 1
        j -= 1


def Solution(n, c):
    # Write Your Code Here
    ans = [i for i in range(n)]
    if c < n-1 or c >= ((n*(n+1))//2):
        return "IMPOSSIBLE"
    a = [i for i in range(n)]
    # c -= (n-1)
    for i in range(n-1):
        l = (n-2-i)
        cost = min(c-l, n-i)
        c -= cost
        reverIt(a, i, i+cost-1)
        ans[a[i]] = i+1
    ans[a[-1]] = n
    return ans


def main():
    # Take input Here and Call solution function
    for t in range(get_int()):
        x, y = get_ints_in_variables()
        ans = Solution(x, y)
        if ans == "IMPOSSIBLE":
            print("Case #{}: {}".format(t+1, ans))
        else:
            print("Case #{}:".format(t+1), end=" ")
            print(*ans)


# calling main Function
if __name__ == '__main__':
    main()

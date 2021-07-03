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


def Solution():
    # Write Your Code Here
    n = get_int()
    arr = get_ints_in_list()
    if n == 2:
        print((arr[0]*arr[1])//math.gcd(arr[0], arr[1]))
        return
    suffix = [arr[-1]]
    for i in range(n-2, -1, -1):
        suffix.append(math.gcd(suffix[-1], arr[i]))
    suffix = list(reversed(suffix))
    ans = -1
    for i in range(n-1):
        tmp = (arr[i]*suffix[i+1])//math.gcd(suffix[i+1], arr[i])
        if ans == -1:
            ans = tmp
        else:
            ans = math.gcd(ans, tmp)
    print(ans)


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()

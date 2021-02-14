# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638

# import inbuilt standard input output
import sys
import math
from sys import stdin, stdout


def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_string(): return sys.stdin.readline().strip()


def Solution(n, k):
    x = [0]
    for i in range(1, n+1):
        x.append(x[-1]+i*5)
    x.pop(0)
    l = 0
    r = n-1
    target = 240-k
    ans = 0
    while l <= r:
        mid = (l+r)//2
        if x[mid] == target:
            ans = mid+1
            break
        if x[mid] > target:
            r = mid-1
        else:
            ans = mid+1
            l = mid+1

    print(ans)


def main():
    # //TAKE INPUT HERE
    n, k = get_ints_in_variables()
    Solution(n, k)


#  call the main method  pa
if __name__ == "__main__":
    main()

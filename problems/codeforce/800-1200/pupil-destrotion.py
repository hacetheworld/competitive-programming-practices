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


def Solution(arr1, arr2, n):
    cnt = [0 for _ in range(6)]
    for v in arr1:
        cnt[v] += 1
    for u in arr2:
        cnt[u] -= 1
    ans = 0
    for c in cnt:
        if c % 2 != 0:
            print(-1)
            return
        else:
            ans += abs(c)
    print(ans//4)


def main():
    # //TAKE INPUT HERE
    n = int(input())
    arr1 = get_ints_in_list()
    arr2 = get_ints_in_list()
    Solution(arr1, arr2, n)


#  call the main method  pa
if __name__ == "__main__":
    main()

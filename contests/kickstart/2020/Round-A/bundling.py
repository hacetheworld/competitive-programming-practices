# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638

import sys
import math
from sys import stdin, stdout


# TAKE INPUT

def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_int(): return int(input())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()


def Solution(arr, n, k):
    ans = 0
    i = 0
    arr = sorted(arr, reverse=True)
    # print(arr)
    while i <= n-k:
        tmpAns = 0
        s1 = arr[i]
        mp = [1 for _ in range(len(s1))]
        for j in range(i+1, k+i):
            s = arr[j]
            l = 0
            for m in range(len(s)):
                if s1[l] == s[m]:
                    mp[l] += 1
                    l += 1
                else:
                    break
            i += 1
        for count in mp:
            if count == k:
                tmpAns += 1
            else:
                break
        ans += tmpAns
        i += 1
    return ans


def main():
    # //Write Your Code Here
    for t in range(get_int()):
        n, k = get_ints_in_variables()
        arr = [input() for _ in range(n)]
        ans = Solution(arr, n, k)
        print("Case #{}: {}".format(t+1, ans))


# for printing format
# print("Case #{}: {}".format(t+1, ans))
#  calling main Function
if __name__ == "__main__":
    main()

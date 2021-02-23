# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638

# import inbuilt standard input output
import sys
import math
from sys import stdin, stdout


def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_int(): return int(input())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()


def Solution(arr, n, k):
    arr = sorted(arr, key=lambda x: x[0])
    res = 0
    aliceCount = 0
    bobCount = 0
    print(arr)
    for v in arr:
        if v[1] == 1 and v[2] == 1:
            res += v[0]
            aliceCount += 1
            bobCount += 1
        elif aliceCount < k and v[1] == 1:
            res += v[0]
            aliceCount += 1
        elif bobCount < k and v[2] == 1:
            res += v[0]
            bobCount += 1
        if aliceCount == k and bobCount == k:
            break
    print(res) if (aliceCount == k and bobCount == k) else print(-1)


def main():
    # //TAKE INPUT HERE
    n, k = get_ints_in_variables()
    arr = get_list_of_list(n)
    Solution(arr, n, k)


#  call the main method  pa
if __name__ == "__main__":
    main()

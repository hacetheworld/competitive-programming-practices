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


def Solution(arr, dis, dissum, n, q, k):
    for i in range(n):
        if(i == 0):
            if(n != 1):
                dis[i] = arr[1]-2
        if(i != 0 and i != n-1):
            dis[i] = arr[i+1]-arr[i-1]-2
    for i in range(1, n-1):
        dissum[i] = dissum[i-1]+dis[i]


def main():
    # //TAKE INPUT HERE
    # for _ in range(int(input())):
    n, q, k = get_ints_in_variables()
    arr = get_ints_in_list()
    prefix = [0 for _ in range(n)]
    dissum = [0 for _ in range(n)]
    Solution(arr, dissum, prefix, n, q, k)
    # print(prefix)
    for _ in range(q):
        l, r = get_ints_in_variables()
        l -= 1
        r -= 1
        if l == r:
            print(k-1)
            continue
        print(arr[l+1]-2+(prefix[r-1]-prefix[l])+(k-arr[r-1])-1)


#  call the main method  pa
if __name__ == "__main__":
    main()

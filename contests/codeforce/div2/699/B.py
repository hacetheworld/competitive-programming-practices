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


def Solution(arr, n, k):
    flag = False
    id = -1
    while True:
        i = 0
        k -= 1
        while i < n-1 and arr[i] >= arr[i+1]:
            i += 1
        if i == n-1:
            flag = True
            break
        arr[i] += 1
        if k == 0:
            id = i+1
            break
    if flag:
        print(-1)
    else:
        print(id)


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        n, k = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, k)

        #  call the main method  pa
if __name__ == "__main__":
    main()

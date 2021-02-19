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


def Solution(arr, n):
    res = []
    odd = []
    even = []
    for v in arr:
        if v % 2 != 0:
            odd.append(v)
        else:
            even.append(v)
    if len(odd) % 2 == 1:
        odd.pop()
        even.pop()
    elif len(even) >= 2:
        even.pop()
        even.pop()
    else:
        odd.pop()
        odd.pop()
    counter = n-1
    while counter > 0 and len(odd) > 1:
        r1 = odd.pop()
        r2 = odd.pop()
        res.append([r1, r2])
        counter -= 1
    while counter > 0 and len(even) > 1:
        r1 = even.pop()
        r2 = even.pop()
        res.append([r1, r2])
        counter -= 1
    if counter > 0:
        res.append([even[-1], odd[-1]])
    print
    for i in range(len(res)):
        print(res[i][0], res[i][1])


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        n = int(input())
        arr = get_ints_in_list()
        Solution(arr, n)


#  call the main method  pa
if __name__ == "__main__":
    main()

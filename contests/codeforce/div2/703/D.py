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


def findPostion(subArr, target):
    l = 0
    r = len(subArr)-1
    pos = len(subArr)-1
    while l <= r:
        mid = (l+r)//2
        if subArr[mid] <= target:
            l = mid+1
            pos = mid
        else:
            r = mid-1
    return pos


def Solution(arr, n, k):
    subArr = []
    for i in range(k):
        subArr.append(arr[i])
    subArr = sorted(subArr)
    id = (k+1)//2
    res = subArr[id-1]

    for j in range(k, n):
        pos = findPostion(subArr, arr[j])
        subArr.insert(pos, arr[j])
        subArr.remove(arr[j-k])
        res = max(res, subArr[id-1])
    print(res)


def main():
    # //TAKE INPUT HERE
    # op = []
    n, k = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, k)
    # print(op)


#  call the main method  pa
if __name__ == "__main__":
    main()

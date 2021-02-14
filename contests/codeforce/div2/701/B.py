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


def createSeg(arr, tree, start, end, treeNode, k):
    # createHelper(arr,)
    if start == end:
        tree[treeNode] = k-1
        return
    mid = (start+end)//2
    createSeg(arr, tree, start, mid, 2*treeNode+1, k)
    createSeg(arr, tree, mid+1, end, 2*treeNode+2, k)
    tree[treeNode] = arr[end-1]-1 + k-arr[start-1]-1


def getRange(tree, start, end, treeNode, left, right):
    if start > right or end < left:
        return 0
    if start >= left and end <= right:
        return tree[treeNode]
    mid = (start+end)//2
    return getRange(tree, start, mid, 2*treeNode+1, left, right)+getRange(tree, mid+1, end, 2*treeNode+2, left, right)


def main():
    # //TAKE INPUT HERE
    # for _ in range(int(input())):
    n, q, k = get_ints_in_variables()
    seg = [0 for _ in range(4*n)]
    arr = get_ints_in_list()
    createSeg(arr, seg, 1, n, 1, k)
    print(seg)

    # for _ in range(q):
    #     li, ri = get_ints_in_variables()
    #     print(getRange(seg, 1, n, 1, li, ri))


#  call the main method  pa
if __name__ == "__main__":
    main()

# import inbuilt standard input output
import sys
import math
from sys import stdin, stdout

# suppose a function called main() and
# all the operations are performed

# ////////// Get integer values in variables \\\\\\\\\\\\\\\\\\\\\\\


def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_string(): return sys.stdin.readline().strip()


def create_seg(arr, tree, start, end, treeNode):
    # createHelper(self,arr,)
    if start == end:
        tree[treeNode] = arr[start]
        return
    mid = (start+end)//2
    create_seg(arr, tree, start, mid, 2*treeNode+1)
    create_seg(arr, tree, mid+1, end, 2*treeNode+2)
    tree[treeNode] = tree[2*treeNode+1]+tree[2*treeNode+2]


def update_seg(tree, start, end, treeNode, idx, value):
    if start == end:
        tree[treeNode] = value
        return
    mid = (start+end)//2
    if idx <= mid:
        update_seg(tree, start, mid, 2*treeNode+1, idx, value)
    else:
        update_seg(tree, mid+1, end, 2*treeNode+2, idx, value)
    tree[treeNode] = tree[2*treeNode+1]+tree[2*treeNode+2]


def rangeQuery(tree, start, end, treeNode, left, right):
    if start > right or end < left:
        return 0
    if start >= left and end <= right:
        return tree[treeNode]
    mid = (start+end)//2
    return rangeQuery(tree, start, mid, 2*treeNode+1, left, right) + \
        rangeQuery(tree, mid+1, end, 2*treeNode+2, left, right)


def main():
    # //TAKE INPUT HERE
    n, q = get_ints_in_variables()
    arr = get_ints_in_list()
    seg = [0 for _ in range(4*n)]
    create_seg(arr, seg, 0, n-1, 0)
    # print(seg)
    # print(t)
    for _ in range(q):
        qt, l, r = get_ints_in_variables()
        # FIND ANSWER HERE
        if qt == 1:
            update_seg(seg, 0, n-1, 0, l-1, r)
        else:
            ans = rangeQuery(seg, 0, n-1, 0, l-1, r-1)
            # PRINT OUTPUT HERE
            stdout.write(str(ans)+"\n")


# call the main method
if __name__ == "__main__":
    main()

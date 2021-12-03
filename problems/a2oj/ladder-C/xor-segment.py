# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
import sys
import math
import bisect
import heapq
from bisect import bisect_right
from sys import stdin, stdout

# -------------- INPUT FUNCTIONS ------------------


def get_ints_in_variables(): return map(
    int, sys.stdin.readline().strip().split())


def get_int(): return int(sys.stdin.readline())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))
def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()

# -------- SOME CUSTOMIZED FUNCTIONS-----------


def myceil(x, y): return (x + y - 1) // y

# -------------- SOLUTION FUNCTION ------------------


def updateRangeUtil(tree, lazy, si, ss, se, us, ue, diff):
    if (lazy[si] != 0):
        tree[si] += (se - ss + 1) * lazy[si]
        if (ss != se):
            lazy[si * 2 + 1] += lazy[si]
            lazy[si * 2] += lazy[si]
        lazy[si] = 0
    if (ss > se or ss > ue or se < us):
        return
    if (ss >= us and se <= ue):
        tree[si] += (se - ss + 1) * diff

        if (ss != se):
            lazy[si * 2 + 1] += diff
            lazy[si * 2] += diff
        return

    mid = (ss + se) // 2
    updateRangeUtil(tree, lazy, si * 2 + 1, ss,
                    mid, us, ue, diff)
    updateRangeUtil(tree, lazy, si * 2, mid + 1,
                    se, us, ue, diff)
    tree[si] = tree[si * 2 + 1] + tree[si * 2]


def getSumUtil(tree, lazy, ss, se, qs, qe, si):

    if (lazy[si] != 0):
        tree[si] += (se - ss + 1) * lazy[si]
        if (ss != se):
            lazy[si * 2 + 1] += lazy[si]
            lazy[si * 2] += lazy[si]
        lazy[si] = 0

    if (ss > se or ss > qe or se < qs):
        return 0
    if (ss >= qs and se <= qe):
        return tree[si]
    mid = (ss + se) // 2
    return (getSumUtil(tree, lazy, ss, mid, qs, qe, 2 * si + 1) +
            getSumUtil(tree, lazy, mid + 1, se, qs, qe, 2 * si))


def constructSTUtil(tree, arr, ss, se, idx):
    if (ss > se):
        return
    if (ss == se):
        tree[idx] = arr[ss]
        return
    mid = (ss + se) // 2
    constructSTUtil(tree, arr, ss, mid, idx * 2 + 1)
    constructSTUtil(tree, arr, mid + 1, se, idx * 2)
    tree[idx] = tree[idx * 2 + 1] + tree[idx * 2]


def Solution():
    n = get_int()
    arr = get_ints_in_list()
    segTree = [[0, [0 for _ in range(20)]] for _ in range((4*n)+1)]
    lazy = [0 for _ in range((4*n)+1)]
    constructSTUtil(segTree, arr, 0, n-1, 1)
    for _ in range(get_int()):
        inp = get_ints_in_list()
        if inp[0] == 1:
            print(getSumUtil(segTree, lazy, 0, n-1, inp[1]-1, inp[2]-1, 1))
        else:
            updateRangeUtil(segTree, lazy, 0, n-1,
                            inp[1]-1, inp[2]-1, 1, inp[3])


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()

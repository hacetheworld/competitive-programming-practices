# import inbuilt standard input output
import sys
from sys import stdin, stdout

# suppose a function called main() and
# all the operations are performed

# ////////// Get integer values in variables \\\\\\\\\\\\\\\\\\\\\\\


def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_string(): return sys.stdin.readline().strip()


def isSubsequence(S, t, op, key):
    tmp = [c for c in S]
    for j in range(0, key+1):
        tmp[op[j]-1] = "$"
    j = 0
    for i in range(len(tmp)):
        if tmp[i] == t[j]:
            j += 1
        if j == len(t):
            return True
    return j == len(t)


def Solution(s, p, op):
    l = 0
    r = len(op)
    ans = 0
    while l <= r:
        mid = (l+r)//2
        if isSubsequence(s, p, op, mid):
            l = mid+1
        else:
            ans = mid
            r = mid-1
    return ans


def main():
    # //TAKE INPUT HERE
    S = get_string()
    t = get_string()
    arr = get_ints_in_list()
    print(Solution(S, t, arr))


# call the main method
if __name__ == "__main__":
    main()

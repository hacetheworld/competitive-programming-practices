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


def Solution(arr, n):
    hm = {}
    for v in arr:
        if v in hm:
            hm[v] += 1
        else:
            hm[v] = 1
    ans = -1
    for u in hm:
        if hm[u] > ans:
            ans = hm[u]
    print(ans)


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        n = int(input())
        arr = get_ints_in_list()
        Solution(arr, n)


# call the main method  pa
if __name__ == "__main__":
    main()

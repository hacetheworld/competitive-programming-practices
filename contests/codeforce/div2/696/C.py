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
    arr = sorted(arr)
    res = []
    for i in range(len(arr)-1):
        x = arr[i]+arr[-1]
        tmp = [].copy(arr)
        tmp.pop(0)
        tmp.pop()
        if isThrown(tmp, x):
            pass


def main():
    # //TAKE INPUT HERE
    for t in range(int(input())):
    n = int(input())
    arr = get_ints_in_list()
    # strArr = [input() for _ in range(N)]
    print(Solution(arr, n))


# call the main method  pa
if __name__ == "__main__":
    main()

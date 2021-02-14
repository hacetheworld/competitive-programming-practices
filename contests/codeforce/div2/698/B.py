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


def Solution(arr, q, d):
    if d == 1:
        for v in arr:
            print("YES")
        return
    for v in arr:
        flag = 0
        if v >= d*10:
            flag = 1

        if flag == 0:
            while v >= d:
                if v % d == 0:
                    flag = True
                    break
                v -= 10
        if flag:
            print("YES")
        else:
            print("NO")


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        q, d = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, q, d)


# call the main method  pa
if __name__ == "__main__":
    main()

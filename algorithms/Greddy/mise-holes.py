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


def Solution(mise, holes):
    mise = sorted(mise)
    holes = sorted(holes)
    ans = -1
    for i in range(len(mise)):
        ans = max(ans, abs(mise[i]-holes[i]))
    print(ans)


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        mise = get_ints_in_list()
        holes = get_ints_in_list()
        Solution(mise, holes)


# call the main method  pa
if __name__ == "__main__":
    main()

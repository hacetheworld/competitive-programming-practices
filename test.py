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


def Solution(S, n):
    count = 0
    i = n-1
    while i >= 0 and S[i] == ")":
        count += 1
        i -= 1
    return True if count > (n-count) else False


def main():
    # //TAKE INPUT HERE
    t = int(stdin.readline())
    # print(t)
    for _ in range(t):
        n = int(stdin.readline())
        S = get_string()
        # FIND ANSWER HERE
        ans = Solution(S, n)
        # PRINT OUTPUT HERE
        if ans:
            stdout.write("Yes")
        else:
            stdout.write("No")
        print("\n")


# call the main method
if __name__ == "__main__":
    main()

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


def Solution(S):
    hm = {}
    i = 0
    j = 0
    ans = 0
    while i <= j and j < len(S):
        char = S[j]
        if not char in hm:
            hm[char] = True
            j += 1
        else:
            c = S[i]
            hm.pop(c)
            i += 1
        ans = max(ans, len(hm))
    print(ans)


def main():
    # //TAKE INPUT HERE
    S = get_string()
    Solution(S)


# call the main method  pa
if __name__ == "__main__":
    main()

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


def findChar(s, x, y):
    xConuter = 0
    yConuter = 0
    for c in s:
        if c == x:
            xConuter += 1
        elif c == y:
            yConuter += 1
    return [xConuter, yConuter]


def Solution(s, px, py):
    x, y = "", ""
    if px > 0:
        x = "R"
    else:
        x = "L"
    if py > 0:
        y = "U"
    else:
        y = "D"
    res = findChar(s, x, y)
    if res[0] >= abs(px) and res[1] >= abs(py):
        return True
    else:
        return False


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        px, py = get_ints_in_variables()
        s = get_string()
        if Solution(s, px, py):
            print("YES")
        else:
            print("NO")


#  call the main method  pa
if __name__ == "__main__":
    main()

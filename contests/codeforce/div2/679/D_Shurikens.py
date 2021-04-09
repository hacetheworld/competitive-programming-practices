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

# -------------- SOLUTION FUNCTION ------------------


def Solution():
    # Write Your Code Here
    n = get_int()
    pq = []
    a = []
    ans = []
    s = ""
    idnx = n-1
    for i in range(2*n):
        sr = sys.stdin.readline().strip()
        if sr[0] == "+":
            s += "+"
        else:
            s += "-"
            a.append(int(sr[2]))
    for i in range((2*n)-1, -1, -1):
        if s[i] == "+":
            if len(pq) == 0:
                print("NO")
                return
            else:
                ans.append(heapq.heappop(pq))
        else:
            if len(pq) == 0:
                heapq.heappush(pq, a[idnx])
                idnx -= 1
            else:
                if pq[0] < a[idnx]:
                    print("NO")
                    return
                else:
                    heapq.heappush(pq, a[idnx])
                    idnx -= 1
    print("YES")
    ans = list(reversed(ans))
    for v in ans:
        print(v, end=" ")
    print()


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()

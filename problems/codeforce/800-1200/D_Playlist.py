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


def Solution(arr,n):
    # Write Your Code Here
    tmp=arr
    res = []
    i=0
    j=1
    if n==1:
        if arr[0]==1:
            print(1)
        else:
            print(0)
        return
    flag=False
    while True:
        if flag:
            break
        i=i%len(tmp)
        j=j%len(tmp)
        while i<len(tmp)-2 and j<len(tmp)-1:
            tmpArr=[]
            tmpArr.append(tmp[i])
            if math.gcd(tmp[i],tmp[j])==1:
                res.append(tmp[j])
                i+=1
                j+=1
            i+=1
            j+=1
        tmp = tmpArr
        i+=1
        j+=1






def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n=get_int()
        arr=get_ints_in_list()
        Solution(arr,n)


# calling main Function
if __name__ == '__main__':
    main()

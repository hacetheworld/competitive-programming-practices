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


def Solution(A, B, N, monstersPower, monsterHealth):
    id = -1
    mx = -1
    for i in range(len(monstersPower)):
        if monstersPower[i] > mx:
            mx = monstersPower[i]
            id = i
    for j in range(len(monstersPower)):
        if j == id:
            continue
        if B < 1:
            break
        rounds = math.ceil(monsterHealth[j]/A)
        B = B-(monstersPower[j]*rounds)
    if B < 1:
        print("NO")
        return
    lastMonster = math.ceil(monsterHealth[id]/A)
    heroRound = math.ceil(B/monstersPower[id])
    if lastMonster > heroRound:
        print("NO")
    else:
        print("YES")


def main():
    # //TAKE INPUT HERE
    for _ in range(int(input())):
        A, B, N = get_ints_in_variables()
        monstersPower = get_ints_in_list()
        monsterHealth = get_ints_in_list()
        Solution(A, B, N, monstersPower, monsterHealth)


#  call the main method  pa
if __name__ == "__main__":
    main()

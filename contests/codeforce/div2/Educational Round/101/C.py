def Solution(n):
    s = str(n)
    slen = len(s)
    fc = s[0]
    res = 10*(int(fc)-1)
    if slen == 4:
        res += 10
    elif slen == 3:
        res += 6
    elif slen == 2:
        res += 3
    else:
        res += 1
    print(res)


for t in range(int(input())):
    N = int(input())
    Solution(N)

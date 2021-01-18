def Solution(S):
    target = "2020"
    for i in range(4+1):
        t1 = ""
        t = 0
        for j in range(0, i):
            t1 += S[j]
            t += 1
        t2 = ""
        for k in range((len(S)-(4-t)), len(S)):
            t2 += S[k]
        if (t1+t2) == target:
            return True
    return False


for t in range(int(input())):
    N = int(input())
    S = input()
    # strArr = [input() for _ in range(N)]
    if Solution(S):
        print("YES")
    else:
        print("NO")

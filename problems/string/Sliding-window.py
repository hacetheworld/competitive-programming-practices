def SlidingWindow(S, p):
    res = []

    for j in range(len(S)-len(p)+1):
        if isPatternMatched(S, p, j):
            res.append(j)
    return res


def isPatternMatched(S, p, i):
    if S[i] != p[0] and S[i+(len(p)-1)] != p[-1]:
        return False
    for idx in range(i, len(p)):
        if S[idx] != p[idx]:
            return False
    return True


S = input()
P = input()
print(SlidingWindow(S, P))

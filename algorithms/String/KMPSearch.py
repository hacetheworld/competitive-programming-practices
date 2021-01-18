def KmpSearch(S, P):
    M = len(S)
    N = len(P)
    lps = [0]*N
    computeLpsArr(P, N, lps)
    i = 0
    j = 0
    while i < M:
        if S[i] == P[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == N:
            print(i-j, (i-1))
            j = lps[j-1]


def computeLpsArr(P, N, lps):
    l = 0
    i = 1
    lps[0] = 0
    while i < N:
        if P[l] == P[i]:
            lps[i] = l+1
            l += 1
            i += 1
        else:
            if l != 0:
                l = lps[l-1]
            else:
                lps[i] = 0
                i += 1


P = input()
S = input()

KmpSearch(S, P)

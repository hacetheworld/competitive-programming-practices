def longestBracketSequence(S):
    stack = []
    pairIdxs = [-1 for _ in range(len(S))]
    extends = [-1 for _ in range(len(S))]
    frequence = [0 for _ in range(len(S)+1)]

    l = 0
    for i in range(len(S)):
        c = S[i]
        if c == "(":
            stack.append(i)
        else:
            if len(stack) > 0:
                idx = stack.pop()
                pairIdxs[i] = idx
                extends[i] = idx
                if idx > 0 and S[idx-1] == ")" and extends[idx-1] >= 0:
                    extends[i] = extends[idx-1]
                j = i-extends[i]+1
                frequence[j] += 1
                l = max(l, j)
    frequence[0] = 1
    print(l, frequence[l])


S = input()
longestBracketSequence(S)

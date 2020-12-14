def Saviour(S):
    stack = []
    i = len(S)-1
    while not(i < 0):
        if S[i] == "0":
            stack.append("0")
        else:
            j = 0
            while j < 2 and len(stack) > 0:
                stack.pop()
                j += 1
        i -= 1
    return len(stack) == 0


for t in range(int(input())):
    S = input()
    if Saviour(S):
        print("YES")
    else:
        print("NO")

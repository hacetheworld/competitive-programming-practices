def Solution(S):
    if len(S) & 1:
        print("NO")
        return
    if S[0] == ")" or S[-1] == "(":
        print("NO")
    else:
        print("YES")


for t in range(int(input())):
    S = input()
    Solution(S)

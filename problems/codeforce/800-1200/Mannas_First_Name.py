def Solution(S):
    flag = False
    for i in range(len(S)):
        if flag == False and S[i] == '1':
            flag = True
        elif flag and S[i] == '1' and S[i-1] == '0':
            return False
    return flag


for t in range(int(input())):
    S = input()
    # strArr = [input() for _ in range(N)]
    if Solution(S):
        print("YES")
    else:
        print("NO")

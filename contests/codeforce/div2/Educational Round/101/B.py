def Solution(r, b):
    lr = [0]
    for i in range(len(r)):
        lr.append((lr[-1]+r[i]))
    br = [0]
    for i in range(len(b)):
        br.append((br[-1]+b[i]))
    ans = 0
    for k in range(len(lr)):
        for l in range(len(br)):
            ans = max(ans, lr[k]+br[l])
    return ans


for t in range(int(input())):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    print(Solution(r, b))

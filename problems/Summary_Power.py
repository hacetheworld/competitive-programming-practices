def Solution(S, N, K):
    # Solution
    frm_I = 0
    frm_J = K-1
    count = 0
    for i in range(1, len(S)-K+1):
        temp = countPower(S, frm_I, frm_J, i, i+K-1)
        count += temp
        frm_I = i
        frm_J = i+K-1
    return count


def countPower(S, frm_I, frm_J, to_I, to_J):
    counter = 0
    while frm_I <= frm_J and to_I <= to_J:
        if S[frm_I] != S[to_I]:
            counter += 1
        frm_I += 1
        to_I += 1
    return counter


for t in range(int(input())):
    N, K = map(int, input().split())
    S = input()
    # strArr = [input() for _ in range(N)]
    # print("Output Is : ", Solution(S, N, K))
    print(Solution(S, N, K))

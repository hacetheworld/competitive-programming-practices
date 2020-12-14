def Solution(S):
    # Solution
    count = 0
    for i in range(2, len(S)+1):
        cnt_0 = 0
        cnt_1 = 0
        substr = []
        for j in range(0, i):
            substr.append(S[j])
            if S[j] == "0":
                cnt_0 += 1
            else:
                cnt_1 += 1
        if cnt_0 == cnt_1*cnt_1:
            count += 1
        for k in range(i, len(S)):
            firstChar = substr[0]
            curr_char = S[k]
            if firstChar == "0":
                cnt_0 -= 1
            else:
                cnt_1 -= 1
            if curr_char == "0":
                cnt_0 += 1
            else:
                cnt_1 += 1
            if cnt_0 == cnt_1*cnt_1:
                count += 1
            substr.pop(0)
            substr.append(curr_char)

    return count


for t in range(int(input())):
    S = input()
    print(Solution(S))

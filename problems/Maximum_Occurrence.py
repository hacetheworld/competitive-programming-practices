from collections import Counter


def Solution(S):
    setArr = sorted(list(Counter(S).items()), key=lambda x: x[1], reverse=True)
    return setArr[0]


S = input()
char = Solution(S)
print(char[0], char[1])

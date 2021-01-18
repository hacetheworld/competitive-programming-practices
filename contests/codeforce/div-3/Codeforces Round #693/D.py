def Solution(arr, n):
    evenArr = []
    oddArr = []
    for v in arr:
        if v & 1:
            oddArr.append(v)
        else:
            evenArr.append(v)

    turn = 0
    aliceScore = 0
    bobScore = 0
    i, j = 0, 0
    evenArr = sorted(evenArr, reverse=True)
    oddArr = sorted(oddArr, reverse=True)
    while i < len(evenArr) and j < len(oddArr):
        itm = 0
        if evenArr[i] < oddArr[j]:
            itm = oddArr[j]
            j += 1
        else:
            itm = evenArr[i]
            i += 1
        if turn == 0:
            if itm & 1 == 0:
                aliceScore += itm
            turn = 1
        else:
            if itm & 1:
                bobScore += itm
            turn = 0
    while i < len(evenArr):
        itm = 0
        itm = evenArr[i]
        i += 1
        if turn == 0:
            if itm & 1 == 0:
                aliceScore += itm
            turn = 1
        else:
            if itm & 1:
                bobScore += itm
            turn = 0
    while j < len(oddArr):
        itm = 0
        itm = oddArr[j]
        j += 1
        if turn == 0:
            if itm & 1 == 0:
                aliceScore += itm
            turn = 1
        else:
            if itm & 1:
                bobScore += itm
            turn = 0

    if aliceScore > bobScore:
        return "Alice"
    elif bobScore > aliceScore:
        return "Bob"
    else:
        return "Tie"


# op = []
for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    # op.append(Solution(arr, N))
    print(Solution(arr, N))
# print(op)

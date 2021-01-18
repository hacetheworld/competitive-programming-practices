def Solution(arr, n):
    count1 = 0
    count2 = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count1 += 1
        else:
            count2 += 1
    a1 = 0
    if count2 % 2 == 1:
        a1 += 2
    if a1 == 0:
        if count1 % 2 == 0:
            return "YES"
        else:
            return "NO"
    else:
        if count1 >= 2:
            if (count1-2) % 2 == 0:
                return "YES"
            else:
                return "NO"
        else:
            return "NO"


# op = []
for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    # op.append(Solution(arr, N))
    print(Solution(arr, N))
# print(op)
#

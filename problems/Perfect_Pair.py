def Solution(arr):
    # Solution
    nums = dict()
    firstMax = float("-inf")
    secondMax = float("-inf")
    for v in arr:
        if v > firstMax:
            secondMax = firstMax
            firstMax = v
        elif v > secondMax:
            secondMax = v
        nums[v] = True
    maxRange = firstMax+secondMax
    i = 2
    perfectSquares = []
    while i*i <= maxRange:
        sqaure = pow(i, 2)
        cube = pow(i, 3)
        if sqaure <= maxRange:
            perfectSquares.append(sqaure)
        if cube <= maxRange:
            perfectSquares.append(cube)
        i += 1
    counter = 0
    for j in arr:
        for k in perfectSquares:
            if k-j > j and nums.get(k-j) == True:
                counter += 1
    return counter


for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    print(Solution(arr))

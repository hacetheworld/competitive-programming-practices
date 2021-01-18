def Solution(n, x, y):
    # Solution
    if n == 2:
        print(x, y)
        return
    b = [0 for _ in range(n)]
    b[-1] = float("inf")
    a = [0 for _ in range(n)]
    a[-1] = float("inf")

    for i in range(n):
        for j in range(i+1, n):
            b[i] = x
            b[j] = y
            d = y-x
            diff = j-i
            if d % diff == 0:
                d = d//diff
                k = i-1
                while k >= 0:
                    b[k] = b[k+1]-d
                    k -= 1
                l = i+1
                while l < n:
                    b[l] = b[l-1]+d
                    l += 1
                if b[0] > 0 and b[-1] < a[-1]:
                    a = [u for u in b]

    for v in a:
        print(v, end=" ")
    print()


for t in range(int(input())):
    n, x, y = map(int, input().split())
    Solution(n, x, y)

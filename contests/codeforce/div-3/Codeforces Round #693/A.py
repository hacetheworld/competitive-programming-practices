def Solution(w, h, n):
    count = 1
    while w & 1 == 0:
        w = w//2
        count *= 2
    while h & 1 == 0:
        h = h//2
        count *= 2
    if count >= n:
        return "YES"
    else:
        return "NO"


# op = []
for t in range(int(input())):
    w, h, n = map(int, input().split())
    # arr = list(map(int, input().split()))
    # op.append(Solution(w, h, n))
    print(Solution(w, h, n))
# print(op)

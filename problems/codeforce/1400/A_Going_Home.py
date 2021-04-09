n = int(input())
a = list(map(int, input().split()))
d = {}
f = True
for i in range(n):
    if(not f):
        break
    for j in range(i):
        if(a[i]+a[j] in d):
            ii, jj = d[a[i]+a[j]]
            if(len(set([i, j, ii, jj])) == 4):
                print('YES')
                f = False
                print(i+1, j+1, ii+1, jj+1)
                break
        else:
            d[a[i]+a[j]] = (i, j)
if(f):
    print('NO')

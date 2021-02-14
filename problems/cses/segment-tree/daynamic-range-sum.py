class FT:
    def __init__(self, n):
        self.ft = [0] * (n + 1)
        self.n = n

    def qry(self, i):
        res = 0
        while i:
            res += self.ft[i]
            i -= i & -i
        return res

    def upd(self, i, v):
        while i <= self.n:
            self.ft[i] += v
            i += i & -i


n, q = map(int, input().split())
ft = FT(n)
a = list(map(int, input().split()))
for i in range(n):
    ft.upd(i+1, a[i])
for i in range(q):
    op, l, r = map(int, input().split())
    if op == 1:
        ft.upd(l, -a[l-1])
        ft.upd(l, r)
        a[l-1] = r
    else:
        print(ft.qry(r) - ft.qry(l-1))

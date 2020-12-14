class _minMaxStack():
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.length = len(self.stack)

    def getMin(self):
        if not self.isEmpty():
            mn = self.stack[-1]
            return mn[1]

    def getMax(self):
        if not self.isEmpty():
            mx = self.stack[-1]
            return mx[2]

    def push(self, val):
        if self.isEmpty():
            self.stack.append([val, val, val])
            return
        if self.isOverflow():
            return "Stack Overflow"
        mx = self.getMax()
        mn = self.getMin()
        self.stack.append([val, min(mn, val), max(val, mx)])

    def pop(self,):
        if not self.isEmpty():
            return self.stack.pop()

    def isEmpty(self,):
        return len(self.stack) == 0

    def isOverflow(self):
        return self.size == self.length


# Intialize ....
stk = _minMaxStack(size=10)
stk.push(2)
stk.push(1)
stk.push(0)
stk.push(5)
stk.push(1)


print("Min , Max", stk.getMin(), stk.getMax())

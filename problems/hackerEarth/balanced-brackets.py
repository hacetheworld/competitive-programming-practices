def isBalancedBrackets(brackets):
    stack = []
    leftClosingBrackets = set()
    leftClosingBrackets.add("(")
    leftClosingBrackets.add("{")
    leftClosingBrackets.add("[")
    rightClosingBrackets = set()
    rightClosingBrackets.add(")")
    rightClosingBrackets.add("}")
    rightClosingBrackets.add("]")
    for char in brackets:
        if char in leftClosingBrackets:
            stack.append(char)
        else:
            getLastCharFromStack = stack.pop()
            if char == ")" and getLastCharFromStack != "(":
                return False
            elif char == "}" and getLastCharFromStack != "{":
                return False
            elif char == "]" and getLastCharFromStack != "[":
                return False
    return len(stack) == 0


s = input()
if isBalancedBrackets(s):
    print("YES")
else:
    print("NO")

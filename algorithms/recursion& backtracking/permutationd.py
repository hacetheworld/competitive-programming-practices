def permutations(s, n, op):
    if len(op) == n:
        print(op)
    for c in s:
        if c in op:
            continue
        permutations(s, n, op+c)


permutations("ABC", 3, "")

def printBianryString(n, i, osf):
    if i >= n:
        if len(osf) > n:
            osf = [c for c in osf]
            osf.pop()
            osf = "".join(osf)
        print(osf)
        return
    printBianryString(n, i+2,  osf+"10")
    printBianryString(n, i+1,  osf+"0")


printBianryString(4, 0, "")

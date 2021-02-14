def printSubset(arr, i, n, osf):
    if i == n:
        print("[", osf, "]")
        return
    printSubset(arr, i+1, n, osf+str(arr[i])+" ")
    printSubset(arr, i+1, n, osf)


printSubset([1, 2, 3], 0, 3, "")

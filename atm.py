def atmPinGenerator():
    res = []
    count = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    count += 1
                    if i == 7 and j == 8:
                        res.append([i, j, k, l])
    # for pin in res:
    #     print(pin)
    return count


print(atmPinGenerator())

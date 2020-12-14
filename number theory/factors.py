# Print Factors of any Number
import math


def _factor(N):
    sqrN = round(math.sqrt(N))
    factors = []
    for i in range(1, sqrN+1):

        if N % i == 0:
            if sqrN != i:
                factors.append(i)
            factors.append(N//i)
    counter = len(factors)
    return counter


print(_factor(int(input())))

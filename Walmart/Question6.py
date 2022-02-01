import math


def power(N, R):

    M = 1000000007

    N %= M

    if R == 0:
        return 1

    if R == 1:
        return N

    tmp = power(N, R // 2)
    res = (tmp * tmp) % M

    if R % 2 != 0:
        res = (res * N) % M

    return res


N = input()
R = N[::-1]
print(power(int(N), int(R)))

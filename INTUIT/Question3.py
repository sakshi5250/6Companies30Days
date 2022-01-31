import math
MAX_DIGITS = 6


def getVal(s, i, m):
    if i + m > len(s):
        return -1
    value = 0
    for j in range(m):
        c = (ord(s[i + j]) - ord('0'))
        if c < 0 or c > 9:
            return -1
        value = value * 10 + c
    return value


def missingNumber(string):

    for m in range(1, MAX_DIGITS + 1):
        n = getVal(string, 0, m)
        if n == -1:
            break
        missingNo = -1
        fail = False
        i = m
        while i != len(string):
            if missingNo == -1 and getVal(string, i, 1 + int(math.log10(n + 2))) == n + 2:
                missingNo = n + 1
                n += 2
            elif getVal(string, i, 1 + int(math.log10(n + 1))) == n + 1:
                n += 1
            else:
                fail = True
                break
            i += 1 + int(math.log10(n))
        if not fail:
            return missingNo
    return -1


if __name__ == '__main__':
    String = "9899100102"
    print(missingNumber(String))

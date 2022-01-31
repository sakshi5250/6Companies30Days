def helper(s, k, maxstr, ctr):

    if k == 0 or ctr == len(s):
        return

    n = len(s)

    maxx = s[ctr]

    for i in range(ctr+1, n):

        if int(maxx) < int(s[i]):
            maxx = s[i]

    if maxx != s[ctr]:
        k -= 1

        for j in range(n-1, ctr, -1):

            if int(s[j]) == int(maxx):
                s[j], s[ctr] = s[ctr], s[j]

                if int(maxstr[0]) < int("".join(map(str, s))):
                    maxstr[0] = "".join(map(str, s))

                helper(s, k, maxstr, ctr+1)

                s[j], s[ctr] = s[ctr], s[j]
    else:
        helper(s, k, maxstr, ctr+1)


def findMaximumNum(s, k):
    maxx = [s]
    s = list(map(str, s.strip()))
    helper(s, k, maxx, 0)

    return maxx[0]


if __name__ == "__main__":
    k = 4
    s = "1234567"
    print(findMaximumNum(s, k))

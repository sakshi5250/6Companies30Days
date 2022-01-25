def amendSentence(s):
    res = ""
    p = s[0].lower()
    for i in range(1, len(s)):
        if s[i] >= 'A' and s[i] <= 'Z':
            res += p
            res += " "
            p = s[i].lower()
            continue
        p += s[i]

    res += p
    return res


if __name__ == '__main__':
    s = "BruceWayneIsBatman"

    print(amendSentence(s))

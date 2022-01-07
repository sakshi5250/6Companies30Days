from collections import defaultdict


def Pairs(arr, n, k):

    if (n & 1):
        return 0
    freq = defaultdict(lambda: 0)

    for i in range(0, n):
        freq[((arr[i] % k) + k) % k] += 1

    for i in range(0, n):

        rem = ((arr[i] % k) + k) % k

        if (2 * rem == k):

            if (freq[rem] % 2 != 0):
                return 0

        elif (rem == 0):
            if (freq[rem] & 1):
                return 0

        elif (freq[rem] != freq[k - rem]):
            return 0

    return 1


arr = [91, 74, 66, 48]
k = 10
n = len(arr)

if (Pairs(arr, n, k)):
    print("True")
else:
    print("False")

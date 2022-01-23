
def lenghtOfLongestAP(set, n):

    if (n <= 2):
        return n

    L = [[0 for x in range(n)]
         for y in range(n)]
    llap = 2

    for i in range(n):
        L[i][n - 1] = 2

    for j in range(n - 2, 0, -1):

        i = j - 1
        k = j + 1
        while(i >= 0 and k <= n - 1):

            if (set[i] + set[k] < 2 * set[j]):
                k += 1

            elif (set[i] + set[k] > 2 * set[j]):
                L[i][j] = 2
                i -= 1

            else:

                L[i][j] = L[j][k] + 1

                llap = max(llap, L[i][j])

                i -= 1
                k += 1

                while (i >= 0):
                    L[i][j] = 2
                    i -= 1
    return llap


if __name__ == "__main__":

    set1 = [1, 7, 10, 13, 14, 19]
    n1 = len(set1)
    print(lenghtOfLongestAP(set1, n1))

    set2 = [1, 7, 10, 15, 27, 29]
    n2 = len(set2)
    print(lenghtOfLongestAP(set2, n2))

    set3 = [2, 4, 6, 8, 10]
    n3 = len(set3)
    print(lenghtOfLongestAP(set3, n3))

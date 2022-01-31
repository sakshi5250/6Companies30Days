def findMinimumRec(arr, i, sumCalculated,
                   sumTotal):

    if (i == 0):
        return abs((sumTotal - sumCalculated) -
                   sumCalculated)

    return min(findMinimumRec(arr, i - 1,
                              sumCalculated+arr[i - 1],
                              sumTotal),
               findMinimumRec(arr, i - 1,
                              sumCalculated, sumTotal))


def findMinDiff(arr, n):

    sumTotal = 0
    for i in range(n):
        sumTotal += arr[i]

    return findMinimumRec(arr, n,
                          0, sumTotal)


if __name__ == "__main__":

    arr = [1, 6, 11, 5]
    n = len(arr)
    print("The minimum difference " +
          "between two sets is ",
          findMinDiff(arr, n))

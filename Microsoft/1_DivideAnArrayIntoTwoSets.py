
def findMinRec(arr, i, sumCalculated,
               sumTotal):

    if (i == 0):
        return abs((sumTotal - sumCalculated) -
                   sumCalculated)

    return min(findMinRec(arr, i - 1,
                          sumCalculated+arr[i - 1],
                          sumTotal),
               findMinRec(arr, i - 1,
                          sumCalculated, sumTotal))


def findMin(arr,  n):

    sumTotal = 0
    for i in range(n):
        sumTotal += arr[i]

    return findMinRec(arr, n,
                      0, sumTotal)


arr = [3, 1, 4, 2, 2, 1, 7]
n = len(arr)
print("The minimum difference between two sets is ", findMin(arr, n))

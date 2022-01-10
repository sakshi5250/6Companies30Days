def maxSubArray(arr):
    subArr = [0 for i in range(len(arr))]
    subArr[0] = arr[0]
    for i in range(1, len(arr)):
        subArr[i] = max(subArr[i-1]+arr[i], arr[i])
    print(subArr)
    return max(subArr)


print(maxSubArray([-2, 1, -3, 7, -2, 2, 1, -5, 4]))

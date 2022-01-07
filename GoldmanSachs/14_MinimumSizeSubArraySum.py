def MinimumSubWithSum(arr, n, x):

    min_len = n + 1

    for start in range(0, n):

        curr_sum = arr[start]

        if (curr_sum > x):
            return 1

        for end in range(start+1, n):

            curr_sum += arr[end]

            if curr_sum > x and (end - start + 1) < min_len:
                min_len = (end - start + 1)

    return min_len


arr1 = [1, 10, 5, 2, 7]
x = 9
n1 = len(arr1)
print(MinimumSubWithSum(arr1, n1, x))

def longestMountain(arr):
    i = 1
    list = []
    if len(arr) < 3:
        return 0
    if (len(arr) == 3 and arr[0] >= arr[1] and arr[1] <= arr[2]):
        return 0
    while i < len(arr):
        count = 1
        if arr[i] <= arr[i-1]:
            i += 1
        while (i < len(arr) and arr[i] > arr[i-1]):
            count += 1
            i += 1
        if count == 1 or count == len(arr):
            return 0
        while (i < len(arr) and arr[i] < arr[i-1]):
            count += 1
            i += 1
        list.append(count)
    return max(list)


print(longestMountain([2, 1, 4, 7, 3, 2, 5]))

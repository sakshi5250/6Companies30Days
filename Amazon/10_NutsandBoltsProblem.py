def printArray(arr):
    for i in range(6):
        print(" {}".format(arr[i]), end=" ")
    print()


def partition(arr, low, high, pivot):
    i = low
    j = low
    while j < high:
        if (arr[j] < pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif (arr[j] == pivot):
            arr[j], arr[high] = arr[high], arr[j]
            j -= 1
        j += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def matchPairs(nuts, bolts, low, high):
    if (low < high):
        pivot = partition(nuts, low, high, bolts[high])
        partition(bolts, low, high, nuts[pivot])
        matchPairs(nuts, bolts, low, pivot - 1)
        matchPairs(nuts, bolts, pivot + 1, high)


if __name__ == "__main__":

    nuts = ['@', '#', '$', '%', '^', '&']
    bolts = ['$', '%', '&', '^', '@', '#']

    matchPairs(nuts, bolts, 0, 5)
    print("Matched nuts and bolts are : ")
    printArray(nuts)
    printArray(bolts)

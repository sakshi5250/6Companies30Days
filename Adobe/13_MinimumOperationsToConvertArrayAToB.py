def checkArray(a, b, n):

    operations = 0
    i = 0

    while (i < n):

        if (a[i] - b[i] == 0):
            i += 1
            continue

        diff = a[i] - b[i]
        i += 1

        while (i < n and a[i] - b[i] == diff):
            i += 1

        operations += 1

    print(operations)


if __name__ == "__main__":

    a = [3, 7, 1, 4, 1, 2]
    b = [3, 7, 3, 6, 3, 2]
    size = len(a)

    checkArray(a, b, size)

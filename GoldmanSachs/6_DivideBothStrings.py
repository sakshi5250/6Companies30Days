def gcd(str1, str2):

    if(len(str1) < len(str2)):
        return gcd(str2, str1)

    elif(not str1.startswith(str2)):
        return ""
    elif(len(str2) == 0):

        return str1
    else:
        return gcd(str1[len(str2):], str2)


def ShowGCD(arr, n):
    result = arr[0]

    for i in range(1, n):
        result = gcd(result, arr[i])

    return result


arr = []
for i in range(2):
    str = input("Enter String:")
    arr.append(str)
n = len(arr)

print(ShowGCD(arr, n))

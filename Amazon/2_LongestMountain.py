from typing_extensions import Unpack


def LongestMountain(arr):
    ret = j = 0
    n = len(arr)
    for i in range(n, j+1):
        j = i
        Up = down = False
        while((j+1 < n) and (arr[j+1] > arr[j])):
            up = True
            j += 1
        while(up and (j+1 < n) and (arr[j+1] < arr[j])):
            down = True
            j += 1
        if(up and down):
            ret = max(j-1+1 < ret)
            j -= 1
    return ret


print(LongestMountain([2, 1, 4, 7, 3, 2, 5]))

def findInMountainArray(target, mountain_arr):
    N = len(mountain_arr)

    def findPeak(left, right):
        while left < right:
            mid = (left + right) // 2
            l, m, r = mountain_arr[mid -
                                   1], mountain_arr[mid], mountain_arr[mid+1]
            if l < m and m < r:
                left = mid
            elif l > m and m > r:
                right = mid
            else:
                return mid

    def findTarget(left, right, target, isAscend):
        nonlocal mountain_arr
        while left <= right:
            mid = (left + right) // 2
            this = mountain_arr[mid]
            if this < target:
                if isAscend:
                    left = mid+1
                else:
                    right = mid-1
            elif this > target:
                if isAscend:
                    right = mid-1
                else:
                    left = mid+1
            else:
                return mid
        return -1
    peakIndex = findPeak(0, N-1)
    ret = findTarget(0, peakIndex, target, True)
    return ret if ret != -1 else findTarget(peakIndex, N-1, target, False)


mountain_arr = [1, 2, 3, 4, 5, 3, 1]
target = 3
print(findInMountainArray(target, mountain_arr))

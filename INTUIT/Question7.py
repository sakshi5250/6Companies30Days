def isPossible(weights, load, days):
    cnt = 1
    weigtAllocated = 0
    for i in range(len(weights)):
        if(weigtAllocated > load):
            return False
        weigtAllocated += weights[i]
        if(weigtAllocated > load):
            cnt += 1
            weigtAllocated = weights[i]
    return cnt <= days


def shipWithinDays(weights, days):
    if days > len(weights):
        return -1
    low = max(weights)
    high = sum(weights)
    res = 0
    while low <= high:
        mid = (low+high) >> 1
        if isPossible(weights, mid, days):
            res = mid
            high = mid-1
        else:
            low = mid+1
    return res


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(shipWithinDays(weights, days))

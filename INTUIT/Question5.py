def splitArray(nums, m):

    def min_subarrays_required(max_sum_allowed):
        current_sum = 0
        splits_required = 0

        for element in nums:
            if current_sum + element <= max_sum_allowed:
                current_sum += element
            else:
                current_sum = element
                splits_required += 1
        return splits_required + 1

    left = max(nums)
    right = sum(nums)
    while left <= right:
        max_sum_allowed = (left + right) // 2
        if min_subarrays_required(max_sum_allowed) <= m:
            right = max_sum_allowed - 1
            minimumSplitSum = max_sum_allowed
        else:
            left = max_sum_allowed + 1

    return minimumSplitSum


nums = [7, 2, 5, 10, 8]
m = 2
print(splitArray(nums, m))

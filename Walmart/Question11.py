import heapq


class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        sum_, ans = 0, 0
        heap, pairlist = [], zip(efficiency, speed)

        pairlist = sorted(pairlist, key=lambda x: x[0], reverse=True)
        for val in pairlist:
            if len(heap) >= k:
                mi = heapq.heappop(heap)
                sum_ -= mi
            heapq.heappush(heap, val[1])
            sum_ += val[1]
            ans = max(ans, sum_ * val[0])
        return ans % (10 ** 9 + 7)


n = 6
speed = [2, 10, 3, 1, 5, 8]
efficiency = [5, 4, 3, 9, 7, 2]
k = 2
obj = Solution()
print(obj.maxPerformance(n, speed, efficiency, k))

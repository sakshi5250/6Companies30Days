class Solution:
    def minEatingSpeed(self, piles, h):

        def isPossible(k):

            numOfHours = 0
            for pile in piles:

                numOfHours += pile // k

                if pile % k:
                    numOfHours += 1

                if numOfHours > h:
                    return False

            return True

        low = 1
        high = max(piles)

        while low < high:
            k = (low + high) // 2

            if isPossible(k):
                high = k

            else:
                low = k + 1

        return low


piles = [3, 6, 7, 11]
h = 8
obj = Solution()
print(obj.minEatingSpeed(piles, h))

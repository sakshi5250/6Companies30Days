class Solution:
    def kthLargestNumber(self, nums, k):

        return str((sorted(nums, key=lambda p: int(p)))[-k])


nums = ["3", "6", "7", "10"]
k = 4
obj = Solution()
print(obj.kthLargestNumber(nums, k))

class Solution:
    def height(self, N):
        i = 1
        res = 1
        while res <= N:
            res += i+1
            i += 1
        return i-1


obj = Solution()
n = int(input())
print(obj.height(n))

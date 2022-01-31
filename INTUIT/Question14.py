class Solution():
    def maxDistance(self, grid):

        m, n = len(grid), len(grid[0])
        dp = [[float("inf")]*n for _ in range(m)]
        all_land = all_water = True
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    all_water = False
                    dp[i][j] = 0
                else:
                    all_land = False

        if all_land or all_water:
            return -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                up = dp[i-1][j] if i-1 >= 0 else float("inf")
                left = dp[i][j-1] if j-1 >= 0 else float("inf")
                dp[i][j] = min(dp[i][j], up+1, left+1)

        ret = -1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    continue
                down = dp[i+1][j] if i+1 < m else float("inf")
                right = dp[i][j+1] if j+1 < n else float("inf")
                dp[i][j] = min(dp[i][j], down+1, right+1)
                ret = max(ret, dp[i][j])

        return ret


arr = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
obj = Solution()
print(obj.maxDistance(arr))

import sys


class Solution:
    def dp(self, start, end, lookup):
        if start >= end:
            return 0
        if (start, end) not in lookup:
            money = sys.maxsize
            for penalty in range(start, end+1):
                money = min(money, penalty + max(self.dp(start, penalty -
                            1, lookup), self.dp(penalty+1, end, lookup)))
            lookup[(start, end)] = money
        return lookup[(start, end)]

    def getMoneyAmount(self, n: int) -> int:
        return self.dp(1, n, {})


obj = Solution()
n = int(input())
print(obj.getMoneyAmount(n))

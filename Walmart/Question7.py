import sys


class Solution:
    def find3number(self, A, n):
        new = []
        stack = []
        if n < 3:
            return new
        for i in range(len(A)-1, -1, -1):
            while len(stack) != 0 and stack[0] <= A[i]:
                stack.pop(0)
            stack.insert(0, A[i])
            if len(stack) == 3:
                new = stack
                break
        return new


sys.setrecursionlimit(100000)


def isSubSeq(arr, lis, n, m):
    if m == 0:
        return True
    if n == 0:
        return False
    if arr[n-1] == lis[m-1]:
        return isSubSeq(arr, lis, n-1, m-1)
    return isSubSeq(arr, lis, n-1, m)


N = 5
A = [1,2,1,1,3]
lis = Solution().find3number(A, N)

if len(lis) != 0 and len(lis) != 3:
    print(-1)
if len(lis) == 0:
    print(0)
elif lis[0] < lis[1] and lis[1] < lis[2] and isSubSeq(A, lis, N, len(lis)):
    print(1)
else:
    print(-1)


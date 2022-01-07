class Solution:
    def printMinNumberForPattern(ob, s):
        n = len(s)
        l = [i for i in range(1, n+2)]
        i = 0
        while i < n:
            if s[i] == 'D':
                j = i + 1
                while j < n and s[j] == "D":
                    j += 1
                strt = i
                end = j
                while strt <= end:
                    l[strt], l[end] = l[end], l[strt]
                    strt += 1
                    end -= 1
                i = j
            else:
                i += 1

        ans = ""
        for i in l:
            ans += str(i)
        return ans


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        S = str(input())

        obj = Solution()
        print(obj.printMinNumberForPattern(S))

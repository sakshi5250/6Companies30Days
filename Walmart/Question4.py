class Solution:
    def NumberOfPaths(self, a, b):
        mat = [[0]*b for j in range(a)]
        for i in range(a):
            for j in range(b):
                if(i == 0 or j == 0):
                    mat[i][j] = 1
                else:
                    mat[i][j] = (mat[i-1][j]+mat[i][j-1])
        return mat[a-1][b-1]


if __name__ == '__main__':
    A = 2
    B = 2
    ob = Solution()
    print(ob.NumberOfPaths(A, B))

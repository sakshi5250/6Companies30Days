class Solution:
    def is_valid_row(self, mat, i, j):
        for col in range(9):
            if j != col and mat[i][col] == mat[i][j]:
                return False
        return True

    def is_valid_column(self, mat, i, j):
        for row in range(9):
            if i != row and mat[row][j] == mat[i][j]:
                return False
        return True

    def is_valid_square(self, mat, i, j):
        si = i // 3 * 3
        sj = j // 3 * 3
        for row in range(3):
            for col in range(3):
                if i != si + row and j != sj + col and mat[si + row][sj + col] == mat[i][j]:
                    return False
        return True

    def isValid(self, mat):
        for i in range(9):
            for j in range(9):
                if not (self.is_valid_row(mat, i, j) and self.is_valid_column(mat, i, j) and self.is_valid_square(mat, i, j)) and mat[i][j] != 0:
                    return 0
        return 1

# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        mat = [[0]*9 for x in range(9)]
        for i in range(81):
            mat[i//9][i % 9] = int(arr[i])

        ob = Solution()
        print(ob.isValid(mat))
# } Driver Code Ends

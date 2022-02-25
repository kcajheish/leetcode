"""
73. Set Matrix Zeroes
"""

class Solution:
    def setZeroes(self, matrix):
        """
        Brute Force Approach
        time complexity:
        space complexity
        """
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    for i in range(len(matrix[row])):
                        matrix[row][i] = 0
                        print(row, i)

                    for j in range(len(matrix)):
                        matrix[j][col] = 0
                        print(j, col)

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    expect = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    s.setZeroes(matrix)
    print(matrix)
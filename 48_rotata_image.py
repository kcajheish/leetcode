from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        thought: It is not straightforward to implement 90 rotation. try to combine a series of inversion and flip.

        time complexity: O(n^2)
        """
        size = len(matrix)
        for row in range(size):
            for col in range(row, size):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]

        for row in range(size):
            for col in range(size//2):
                matrix[row][col], matrix[row][size-col-1] = matrix[row][size-col-1], matrix[row][col]

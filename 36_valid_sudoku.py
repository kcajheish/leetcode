from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        time complexity: O(MN)

        performance seems decent, how can we improve the coding style and simplify code?
        https://leetcode.com/problems/valid-sudoku/discuss/15464/My-short-solution-by-C%2B%2B.-O(n2)
        https://leetcode.com/problems/valid-sudoku/discuss/15451/A-readable-Python-solution
        """
        digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        for row in range(len(board)):
            seen = set()
            for col in range(len(board[0])):
                val = board[row][col]
                if val not in digits:
                    continue
                if val in seen:
                    return False
                seen.add(val)

        for col in range(len(board[0])):
            seen = set()
            for row in range(len(board)):
                val = board[row][col]
                if val not in digits:
                    continue
                if val in seen:
                    return False
                seen.add(val)

        for i in range(3):
            for j in range(3):
                seen = set()
                for k in range(i*3, i*3+3):
                    for h in range(j*3, j*3+3):
                        val = board[k][h]
                        if val not in digits:
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

board2 = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]
]
s = Solution()
assert s.isValidSudoku(board) == True
assert s.isValidSudoku(board2) == False
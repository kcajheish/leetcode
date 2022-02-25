class Solution:
    def exist(self, board, word):
        self.W = len(board[0])
        self.L = len(board)
        self.visited = set()
        print(board)
        for j in range(self.L):
            for i in range(self.W):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True

        if i < 0 or j < 0 or i >= self.W or j >= self.L:
            # out of boarder
            return False

        if board[j][i] != word[0]:
            return False

        if (i,j) in self.visited:
            return False

        self.visited.add((i,j))
        res = self.dfs(board, i+1, j, word[1:]) or \
                self.dfs(board, i-1, j, word[1:]) or \
                self.dfs(board, i, j+1, word[1:]) or \
                self.dfs(board, i, j-1, word[1:])
        self.visited.discard((i,j))
        return res
s = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
r = s.exist(board, word)
print(r)
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
r = s.exist(board, word)
print(r)
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
r = s.exist(board, word)
print(r)
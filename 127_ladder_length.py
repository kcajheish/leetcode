from typing import List

class Solution:
    def ladderLengthBFS(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        queue = [(beginWord, 1)]
        while queue:
            current, num = queue.pop(0)
            if current == endWord:
                return num
            for i in range(len(current)):
                for change in 'abcdefghijklmnopqrstuvwxyz':
                    change_word = current[:i] + change + current[i+1:]
                    if change_word in word_set:
                        word_set.remove(change_word)
                        queue.append((change_word, num+1))
        return 0

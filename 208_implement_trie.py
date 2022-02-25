"""
implement trie
M: length of the word, N: number of nodes in trie, ln(N): height of the tire
time complexity: O(M * ln(N))
space complexity: O(N)

use dictionary to memorize child
https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58834/AC-Python-Solution
"""
import string
class Node:
    def __init__(self, val):
        self.val = val
        self.childs = [None]*26
        self.is_word = False # to mark the word

class Trie:
    def __init__(self):
        self.root = Node(None)
        self.alphabets = string.ascii_lowercase

    def insert(self, word: str) -> None:
        next_node = self.root
        for char in word:
            pos = self.alphabets.find(char)
            if not next_node.childs[pos]:
                next_node.childs[pos] = Node(char)
            next_node = next_node.childs[pos]
        next_node.is_word = True

    def search(self, word: str) -> bool:
        next_node = self.root
        for char in word:
            pos = self.alphabets.find(char)
            next_node = next_node.childs[pos]
            if next_node == None:
                return False

        return next_node.is_word


    def startsWith(self, prefix: str) -> bool:
        next_node = self.root
        for char in prefix:
            pos = self.alphabets.find(char)
            next_node = next_node.childs[pos]
            if next_node == None:
                return False
        return True
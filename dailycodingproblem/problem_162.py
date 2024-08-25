"""
This problem was asked by Square.

Given a list of words, return the shortest unique prefix of each word. For example, given the list:

dog
cat
apple
apricot
fish
Return the list:

d
c
app
apr
f

i. create a dictionary to contain tries for each word
ii. iterate through the list building a trie based on each first letter
iii. iterate through the list again
iv. traverse through the word until path becomes a single branch, pass prefix into res array
v. return res
"""
from collections import defaultdict

class TrieNode:
    def __init__(self) -> None:
        self.kids = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()


    def _traverse(self, string: str):
        current = self.root

        for char in string:
            if char not in current.kids:
                return (False, None)
            current = current.kids[char]

        return (True, current)
    

    def insert(self, word: str) -> None:
        current_node = self.root

        for char in word:
            if char not in current_node.kids:
                current_node.kids[char] = TrieNode()
            current_node = current_node.kids[char]

        current_node.isEndOfWord = True


    def search(self, word: str) -> bool:
        res, node = self._traverse(word)
        if res:
            return node.isEndOfWord
        return res
    

    def startsWith(self, prefix: str) -> bool:
        return self._traverse(prefix)[0]

class Solution:
    def shortestUniquePrefixes(self, words: list[str]) -> list[str]:
        def _isSingleBranch(root: TrieNode) -> bool:
            if root.isEndOfWord:
                return True
            
            if len(root.kids) > 1:
                return False
            for kid in root.kids:
                return _isSingleBranch(root.kids[kid])

        letters = defaultdict(Trie)

        for word in words:
            letters[word[0]].insert(word)
        
        res = []

        for word in words:
            prefix = ""
            current = letters[prefix].root
            next = 0

            while next < len(word) and not _isSingleBranch(current):
                next_char = word[next]
                current = current.kids[next_char]
                prefix += next_char
                next += 1
            res.append(prefix)

        return res
    
solution = Solution()

print(solution.shortestUniquePrefixes(["dog", "cat", "apple", "apricot", "fish"])) # -> ["d", "c", "app", "apr", "f"]
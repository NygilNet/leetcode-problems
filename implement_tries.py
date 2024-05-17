"""
link to leetcode: https://leetcode.com/problems/implement-trie-prefix-tree/description/

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

"""


class TrieNode:
    def __init__(self) -> None:
        self.kids = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()    
    

    def _traverse(self, string: str) -> tuple[bool, TrieNode | None]:
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
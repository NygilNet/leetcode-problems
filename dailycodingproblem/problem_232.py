"""
This problem was asked by Google.

Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.
For example, you should be able to run the following code:

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5



"""

class TrieNode:
    def __init__(self) -> None:
        self.kids = {}
        self.isEndOfWord = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    
    def _traverse(self, word: str):
        current = self.root

        for letter in word:
            if letter not in current.kids:
                return (False, None)
            current = current.kids[letter]

        return (True, current)
    

    def insert(self, word: str) -> None:
        current_node = self.root

        for letter in word:
            if letter not in current_node.kids:
                current_node.kids[letter] = TrieNode()
            current_node = current_node.kids[letter]

        current_node.isEndOfWord = True


    def search(self, word: str) -> bool:
        res, node = self._traverse(word)
        if res:
            return node.isEndOfWord
        return res


    def startsWith(self, prefix: str) -> bool:
        return self._traverse(prefix)[0]


from collections import deque
class PrefixMapSum:
    def __init__(self) -> None:
        ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
        self.map = {}
        self.word_pool = { letter : Trie() for letter in ALPHABET }


    def insert(self, key: str, value: int) -> None:
        if key not in self.map:
            self.word_pool[key[0]].insert(key)
        self.map[key] = value


    def sum(self, prefix: str) -> int:
        _, root = self.word_pool[prefix[0]]._traverse(prefix)
        all_words_match_prefix = []
        queue = deque()
        queue.append((root, prefix))

        while queue:
            current_node, current_word = queue.popleft()

            if current_node and current_node.isEndOfWord:
                all_words_match_prefix.append(current_word)

            for kid in current_node.kids:
                queue.append((current_node.kids[kid], current_word + kid))

        total = 0
        for word in all_words_match_prefix:
            total += self.map[word]

        return total
    
mapsum = PrefixMapSum()

mapsum.insert("columnar", 3)
print(mapsum.sum("col")) # -> 3

mapsum.insert("column", 2)
print(mapsum.sum("col")) # -> 5
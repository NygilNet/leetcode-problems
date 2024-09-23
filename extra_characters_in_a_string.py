"""
link to leetcode: https://leetcode.com/problems/extra-characters-in-a-string/description/?envType=daily-question&envId=2024-09-23

You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

 

Example 1:

Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

Example 2:

Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
 

Constraints:

1 <= s.length <= 50
1 <= dictionary.length <= 50
1 <= dictionary[i].length <= 50
dictionary[i] and s consists of only lowercase English letters
dictionary contains distinct words


Input: string, array of strings
Output: int


i. convert dictionary array into dict of tries
ii. initialize leftovers @ 0
iii. iterate over s
    iv. if char is the start of one of our tries
        v. find the longest string that is continuous in the substring, jumping to that point in s
            vi. if string is broken before hitting the end of any word in the trie, increment leftovers at continue to next letter
    vii. if char is NOT the start of one of our tries
        viii. increment leftovers and continue to next char
ix. return leftovers

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

from collections import defaultdict
class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        tries = defaultdict(Trie)
        for word in dictionary:
            tries[word[0]].insert(word)
        
        leftover_chars = 0
        pointer = 0

        while pointer < len(s):
            char = s[pointer]
            if char in tries:
                possible_words = []
                substring = char
                idx = pointer
                while idx < len(s) and tries[char].startsWith(substring):
                    if tries[char].search(substring):
                        possible_words.append(substring)
                    if idx == len(s) - 1:
                        break
                    substring += s[idx + 1]
                    idx += 1
                if not possible_words:
                    leftover_chars += 1
                    continue
                pointer += (len(possible_words[-1]) - 1)
            else:
                leftover_chars += 1
            pointer += 1

        return leftover_chars

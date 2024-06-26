"""
link to leetcode: https://leetcode.com/problems/find-common-characters/?envType=daily-question&envId=2024-06-05


Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.


Input: array of strings
Output: array of chars that all strings share




"""

from collections import defaultdict

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common_string = words[0]

        for i in range(1, len(words)):
            temp = ""
            
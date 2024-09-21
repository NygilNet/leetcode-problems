"""
link to leetcode: https://leetcode.com/problems/shortest-palindrome/description/?envType=daily-question&envId=2024-09-20

You are given a string s. You can convert s to a 
palindrome
 by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"
 

Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.


first idea:
    iterate from the front and back of the string at the same time
    if the two characters are not the same, append the last character before front pointer and decrement the back pointer without moving the front pointer
    if the two characters are the same, increment the front pointer and decrement the back pointer
    when the front and back pointer meet or pass each other we can return the mutated string

this idea doesn't fully work since we can ONLY add characters to the front of the string

second idea:
    pointer at end of string
    check if string is a palindrome
    if not add the character the pointer is pointing at and decrement the pointer
    repeat until palindrome is found

method will work but in the worst case will take over 5 * 10^4 loops

shortest -> shortest path -> bfs??:
    problem doesn't really create any choices so bfs is not helpful

binary search?:
    you can allows create a palindrome by reversing the characters from the first index on and adding it to the beginning of the string
    unclear what the target for the binary search would be, but...

mid point:
    start from the mid point of the current string
    check the left side and right side of the mid point to see the difference of characters we need to make the palindrome

"""

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N = len(s)
        midpoint = N // 2 
        def _inbounds(idx: int) -> bool:
            return 0 <= idx < N
        
        while midpoint > 0:
            left, right = midpoint - 1, midpoint + 1
            reached_left = False
            while _inbounds(left) and _inbounds(right):
                if left == 0:
                    reached_left = True
                if s[left] != s[right]:
                    break
            if reached_left:
                return s[right::-1] + s
            else:
                midpoint -= 1

        return s[1::-1] + s
"""
link to leetcode: https://leetcode.com/problems/lexicographical-numbers/description/?envType=daily-question&envId=2024-09-21

Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 

Constraints:

1 <= n <= 5 * 104
"""

class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        def sortingFunc(i: int) -> str:
            return str(i)
        
        return sorted(list(range(1, n + 1)), key=sortingFunc)
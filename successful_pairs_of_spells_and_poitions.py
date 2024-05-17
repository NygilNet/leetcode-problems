"""
link to leetcode:https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

"""

def successfulPairs(spells: list[int], potions: list[int], success: int) -> list[int]:
        res = []
        potions.sort()
        n = len(potions)
           
        def _binary_search(spell):
            left, right = 0, n - 1

            while left <= right:
                mid = left + (right - left) // 2

                if spell * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1
                        
            return left

        for spell in spells:
            idx = _binary_search(spell)
            res.append(n - idx)

        return res
"""
This problem was asked by Google.

Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.

"""

class Solution:
    def canMakeAPalindromeInK(self, string: str, k: int) -> bool:
        left = 0
        right = len(string) - 1
        deletes_left = k

        def _checkRange(l: int, r: int, dels_left: int, going_left: bool) -> tuple[int, int]:
            while dels_left <= 0 and l < r and string[l] != string[r]:
                dels_left -= 1
                if going_left:
                    l += 1
                else:
                    r -= 1
            new_index = -1 if dels_left < 0 else l if going_left else r
            return (new_index, dels_left)
            

        while left < right:
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                l, check_left = _checkRange(left, right, deletes_left, True)
                r, check_right = _checkRange(left, right, deletes_left, False)
                deletes_left = max(check_left, check_right)
                if deletes_left < 0:
                    return False
                elif deletes_left == check_left:
                    left = l + 1
                    right -= 1
                    continue
                else:
                    left += 1
                    right = r - 1

        return True

solution = Solution()

print(solution.canMakeAPalindromeInK('waterrfetawx', 2)) # -> True
print(solution.canMakeAPalindromeInK('racecar', 2)) # -> True
print(solution.canMakeAPalindromeInK('waterrfetawxxx', 2)) # -> False
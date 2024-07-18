"""
Good morning! Here's your coding interview problem for today.

Given a real number n, find the square root of n. For example, given n = 9, return 3.

Input
"""

class Solution:
    def findSquareRoot(self, i: float) -> float:
        if i < 0:
            return -1
        
        left, right = 0, i // 2

        # find answer if perfect square or get close
        while left <= right:
            mid = left + ((right - left) // 2)
            current = mid ** 2

            if current == i:
                return mid
            elif current < i:
                left = mid + 1
            else:
                right = mid - 1
        
        # if input is not a perfect square, approximate to actual square
        prev_guess = min(left, right)

        while True:
            guess = (prev_guess + i / prev_guess) / 2
            if abs(guess - prev_guess) < 0.00001:
                break
            prev_guess = guess

        return guess 
        
    
solution = Solution()
print(solution.findSquareRoot(9)) # -> 3
print(solution.findSquareRoot(10)) # -> ~ 3.1622776601683795
print(solution.findSquareRoot(10.23)) # -> ~ 3.1984371183438953
print(solution.findSquareRoot(-10)) # -> -1
print(solution.findSquareRoot(16)) # -> 4
print(solution.findSquareRoot(0)) # -> 0
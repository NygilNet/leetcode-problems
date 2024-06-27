"""
This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.

input: two strings
output: boolean

"""

class Solution:
    def canBeShifted(self, stringA: str, stringB: str) -> bool:
        if len(stringA) != len(stringB):
            return False
        if stringA == stringB:
            return True
        N = len(stringA)

        for i in range(N):
            new_string = stringA[i + 1:] + stringA[0 : i + 1]
            if new_string == stringB:
                return True
        
        return False
    

solution = Solution()
print(solution.canBeShifted('abcde', 'cdeab')) # -> True
print(solution.canBeShifted('abc', 'acb')) # -> False
"""
This problem was asked by LinkedIn.

Given a string, return whether it represents a number. Here are the different kinds of numbers:

"10", a positive integer
"-10", a negative integer
"10.1", a positive real number
"-10.1", a negative real number
"1e5", a number in scientific notation
And here are examples of non-numbers:

"a"
"x 1"
"a -2"
"-"
"""

class Solution:
    def isStringANumber(self, string: str) -> str:
        if string.isdigit():
             return "positive integer" if int(string) >= 0 else "negative integer"
        try:
            is_float = float(string)
            if "e" in string.lower():
                return "number in scientific notation"
            return "positive real number" if is_float >= 0 else "negative real number"
        except ValueError:
                return "non-number"
            
solution = Solution()

print(solution.isStringANumber("10")) # -> positive integer
print(solution.isStringANumber("-10")) # -> negative integer
print(solution.isStringANumber("10.1")) # -> positive real number
print(solution.isStringANumber("-10.1")) # -> negative real number
print(solution.isStringANumber("1e5")) # -> number in scientific notation
print(solution.isStringANumber("a")) # -> non-number
print(solution.isStringANumber("-")) # -> non-number
print(solution.isStringANumber("a-2")) # -> non-number

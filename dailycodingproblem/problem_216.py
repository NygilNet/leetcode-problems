"""
This problem was asked by Facebook.

Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.

For the input XIV, for instance, you should return 14.


Input: string in valid Roman numeral format
Output: int


i. iterate through the string
    ii. if index is less than length of the string and the character at index + 1 has a greater value than character at the current index add ((val @ index + 1) - (val @ current index))
    iii. else add val of character @ current index
iv. return total sum
"""

class Solution:
    def convertRomanToDecimal(self, numeral: str) -> int:
        N = len(numeral)
        total_sum, i = 0, 0
        conversions = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        while i < N:
            if i < N - 1 and conversions[numeral[i + 1]] > conversions[numeral[i]]:
                total_sum += (conversions[numeral[i + 1]] - conversions[numeral[i]])
                i += 1
            else:
                total_sum += conversions[numeral[i]]
            i += 1

        return total_sum
    
solution = Solution()
print(solution.convertRomanToDecimal("XIV")) # -> 14
print(solution.convertRomanToDecimal("V")) # -> 5
print(solution.convertRomanToDecimal("MMXXIV")) # -> 2024
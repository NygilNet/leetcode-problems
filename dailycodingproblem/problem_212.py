"""
This problem was asked by Dropbox.

Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".
"""

class Solution:
    def getColumnID(self, id_num: int) -> str:
        ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n = id_num
        res = ""

        while n > 0:
            rem = n % 26

            if rem == 0:
                res += "Z"
                n = (n // 26) - 1
            else:
                res += ALPHABET[rem - 1]
                n = n // 26

        return res[::-1]
        
           
solution = Solution()
print(solution.getColumnID(1)) # -> "A"
print(solution.getColumnID(2)) # -> "B"
print(solution.getColumnID(26)) # -> "Z"
print(solution.getColumnID(27)) # -> "AA"
print(solution.getColumnID(28)) # -> "AB"
print(solution.getColumnID(705)) # -> "AAC"
print(solution.getColumnID(676)) # -> "YZ"
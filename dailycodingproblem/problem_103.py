"""
This problem was asked by Square.

Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.

input: string and a set
output: shortest substring that has all characters or None


"""

class Solution:
    def shortestSubstringContainingCharacters(self, s: str, chars: set[str]) -> (str | None):
        N = len(s)
        self.shortest_substring = "x" * (N + 1)
        print(self.shortest_substring)
        def _backtracking(idx: int, remainingChars: set[str], substring: str = ""):
            if len(remainingChars) == 0:
                if len(substring) < len(self.shortest_substring):
                    self.shortest_substring  = substring
                return
            if idx == N:
                return
            
            char = s[idx]
            substring += char

            if char in remainingChars:
                remainingChars.remove(char)

            _backtracking(idx + 1, remainingChars, substring)
        
        for i in range(N):
            _backtracking(i, chars)

        return self.shortest_substring if self.shortest_substring is not "x" * (N + 1) else None
    

print(Solution.shortestSubstringContainingCharacters("figehaeci", set(['a', 'e', 'i'])))
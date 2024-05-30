"""
link to problem: 


"""

class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        n = len(s)
        permutations = []

        def _backtracking(i: int, res: str):
            if i == n:
                permutations.append(res)
                return
            
            current_chars = s[i]

            _backtracking(i + 1, res + current_chars.lower())
            if not current_chars.isnumeric():
                _backtracking(i + 1, res + current_chars.upper())

        _backtracking(0, "")
        return permutations
    
    # def letterCasePermutation(self, s: str) -> list[str]:
    #     n = len(s)

    #     def _backtracking(i: int, res: str) -> list[str]:
    #         if i == n:
    #             return [res]
            
    #         arr = []
    #         current_char = s[i]
    #         arr = arr + _backtracking(i + 1, res + current_char.lower())
    #         if not current_char.isnumeric():
    #            arr = arr + _backtracking(i + 1, res + current_char.upper())

    #         return arr
        
    #     return _backtracking(0, "")
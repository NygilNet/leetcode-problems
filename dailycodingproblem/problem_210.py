"""
This problem was asked by Apple.

A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?
"""

class Solution:
    def collatzSequence(self, n: int) -> int:
        cycles = 0

        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = (3 * n) + 1
            cycles += 1

        return cycles

    def longestCollatzSequence(self) -> int:
        memo = [0] * 1000001
        longest_sequence = (0, 0)
        memo[1] = 1

        for i in range(2, 1000001):
            cycles = 0
            n = i
            while n != 1:
                if n <= 1000000 and memo[n]:
                    cycles += memo[n]
                    break
                if n % 2 == 0:
                    n = n // 2
                else:
                    n = (3 * n) + 1
                cycles += 1
            memo[i] = cycles
            if memo[i] > longest_sequence[0]:
                longest_sequence = (memo[i], i)

        return longest_sequence[1]
    
solution = Solution()

# for i in range(2, 50):
#     print(solution.collatzSequence(i))

print(solution.longestCollatzSequence())
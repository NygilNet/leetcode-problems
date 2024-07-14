"""
This problem was asked by Microsoft.

You have n fair coins and you flip them all at the same time. Any that come up tails you set aside. The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.


Input: int
Output: int



"""

from random import randint
class Solution:
    def determineCoinRounds(self, numCoins: int) -> int:    
        remaining_coins = numCoins
        self.num_rounds = 1
            
        while remaining_coins > 1:
            save = remaining_coins
            for _ in range(save):
                coin_result = randint(0, 1)
                if coin_result == 0:
                    remaining_coins -= 1
                    if remaining_coins == 1:
                        break
            self.num_rounds += 1

        return self.num_rounds
    
solution = Solution()
print(solution.determineCoinRounds(2))
print(solution.determineCoinRounds(5))
        
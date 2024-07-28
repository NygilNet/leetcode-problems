"""
This problem was asked by Google.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""

class Solution:
    def minNumberOfCoins(self, n: int) -> int:
        
        denominations = [1, 5, 10, 25]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for coin in denominations:
            for amount in range(coin, n + 1):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

        return dp[n] if dp[n] != float('inf') else -1
        
        
        
        # self.c = float('inf')
        # denominations = [1, 5, 10, 25]

        # def _func(coins: int, total: int):
        #     if total > n:
        #         return
        #     if total == n:
        #         self.c = min(self.c, coins)
        #         return
            
        #     for i in range(len(denominations) - 1, -1, -1):
        #         d = denominations[i]
        #         if n - total >= d:
        #             _func(coins + 1, total + d)

        # for i in range(len(denominations) - 1, -1, -1):
        #     _func(1, denominations[i])

        # return self.c
    
solution = Solution()

print(solution.minNumberOfCoins(16)) # -> 3
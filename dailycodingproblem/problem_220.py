"""
This problem was asked by Square.

In front of you is a row of N coins, with values v1, v1, ..., vn.

You are asked to play the following game. You and an opponent take turns choosing either the first or last coin from the row, removing it from the row, and receiving the value of the coin.

Write a program that returns the maximum amount of money you can win with certainty, if you move first, assuming your opponent plays optimally.


Input: row of coins
Output: number (max score if you move first)


double ended queue or two-pointer
"""

class Solution:
    def maxAmountYouCanWin(self, coins: list[int]) -> int:
        turn, left, right = 0, 0, len(coins) - 1
        your_winnings = 0

        while left <= right:
            if coins[left] > coins[right]:
                if turn % 2 == 0:
                    your_winnings += coins[left]
                left += 1
            else:
                if turn % 2 == 0:
                    your_winnings += coins[right]
                right -= 1
            
            turn += 1

        return your_winnings
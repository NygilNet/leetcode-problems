"""
link to leetcode: https://leetcode.com/problems/sum-of-square-numbers/description/?envType=daily-question&envId=2024-06-17

Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

input: number
output: boolean

looks like i've attempted the problem before during September of 2023 without solving it with this code :

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left = 1
        right = c - 1

        while left < right:

            current_square = left ** 2 + right ** 2

            if current_square == c:
                return True
            elif current_square > c:
                right = ((right - left) // 2) + 1
            elif current_square < c:
                left = ((right - left) // 2) - 1

        return False

this is something in the right direction but doesn't make sense

we will iterate from 1 to c - 1
for each number we iterate through, THEN we binary search to check if there is a number that combines to get our solution

"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        L, R = 0, c

        while L <= R:
            MID = L + ((R - L) // 2)

            l, r, save = 0, c, -1

            while l <= r:
                mid = l + ((r - l) // 2)

                current_square = MID ** 2 + mid ** 2
                save = current_square

                if current_square == c:
                    return True
                elif current_square < c:
                    l = mid + 1
                else:
                    r = mid - 1

            if save < c:
                L = MID + 1
            else:
                R = MID - 1.

                math.sq

        return False


 
        # for i in range(1, c):
        #     left, right = 1, c - 1

        #     while left <= right:
        #         mid = left + ((right - left) // 2)

        #         current_square = i ** 2 + mid ** 2

        #         if current_square == c:
        #             return True
        #         elif current_square < c:
        #             left = mid + 1
        #         else:
        #             right = mid - 1

        # return False

    #     class Solution:
    # def judgeSquareSum(self, c: int) -> bool:
    #     left, right = 0, int(math.sqrt(c))
    #     while left <= right:
    #         if left * left + right * right == c:
    #             return True
    #         elif left * left + right * right > c:
    #             right -= 1
    #         else:
    #             left += 1
    #     return False
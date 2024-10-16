"""
This problem was asked by Oracle.

We say a number is sparse if there are no adjacent ones in its binary representation. For example, 21 (10101) is sparse, but 22 (10110) is not. For a given input N, find the smallest sparse number greater than or equal to N.

Do this in faster than O(N log N) time.


Input: number
Output: number


function must be faster than O(N log N)
    binary search

left -> the inputted number
right -> the next binary base (i.e. 1(1), 2(10), 4(100), 8(1000)...)

i. if the input number is sparse, return the input number
"""

class Solution:
    def isSparse(self, n: int) -> bool:
        s = f"{n:b}"
        last_digit_one = False

        for char in s:
            if char == "1" and last_digit_one:
                return False
            last_digit_one = False if char == "0" else True

        return True
    

    def smallestSparseNumberGreaterThanN(self, n: int) -> int:
        if self.isSparse(n):
            return n
        
        left, right = n, 2**(len(f"n:b"))
        smallest_sparse_number = right

        while left <= right:
            mid = left + ((right - left) // 2)
            if self.isSparse(mid):
                smallest_sparse_number = min(mid, smallest_sparse_number)
            right = mid - 1

        return smallest_sparse_number

solution = Solution()
print(solution.isSparse(4))
"""
This problem was asked by Lyft.

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.

Input: list of ints and k
Output: list (where the sum of elements is k)

two-pointer/running sum

"""

class Solution:
    def contiguousList(arr: list[int], k: int) -> list[int]:
        N = len(arr)
        if N == 1:
            if arr[0] == k:
                return arr
            else:
                return []
            
        left, right = 0, 0

        running_sum = arr[0]

        while right < N - 1:
            right += 1

            running_sum += arr[right]
            if running_sum < arr[right] < k:
                running_sum = arr[right]
                left = right
                continue

            while running_sum > k and left < right:
                if arr[left] >= 0:
                    running_sum -= arr[left]
                left += 1
            if running_sum == k:
                return arr[left : right + 1]
        
        return []

print(Solution.contiguousList([1,2,3,4,5], 9))    
print(Solution.contiguousList([-11,2,3,4,5], 9))
"""
This problem was asked by Amazon.

Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.
"""

class Solution:
    def rotateKElements(arr: list, k: int) -> None:
        if not arr or not k:
            return
        
        N = len(arr)
        k %= N

        arr[:] = arr[N - k:] + arr[:N - k]
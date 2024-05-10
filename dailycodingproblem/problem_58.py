"""

This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.


input: an array of integers, a target int
output: integer (the index the target is at in the array) or null (if the target is not in the array)


CAN NOT:
    iterate through the array (O(n) time, needs to be faster)
    sort the array (O(n log n) time)
CAN:
    select index (O(1))
    binary search? (O(log n) time, but the array has been rotated unknown number of times)


possible solution 1 - binary search:
    if the array has been rotated there will be multiple sorted subarrays through out the array

    define a helper function that finds the lowest index and the highest index in a sorted subarray

    define a binary search function that looks for the target element between two indices

    if we find the target element return the index where it was found

    if we didn't find the target element return none

"""

def findIndex(arr: list[int], ele: int) -> int | None:
    
    def _findRange(i: int) -> tuple[int, int]:
        low, high = i, i

        while arr[low - 1] < arr[low]:
            low -= 1
        while arr[high] < arr[high + 1]:
            high += 1

        return (low, high)
    
    def _binarySearch(low: int, high: int) -> int | None:
        left, right = low, high

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == ele:
                return mid
            if arr[mid] < ele:
                left = mid + 1
            else:
                right = mid - 1

        return None
    
    l, r = 0, len(arr) - 1

    while l < r:
        left_low, left_high = _findRange(l)
        right_low, right_high = _findRange(r)

        if left_low <= ele <= left_high:
            target = _binarySearch(left_low, left_high)
            if target is not None:
                return target
        if right_low <= ele <= right_high:
            target = _binarySearch(right_low, right_high)
            if target is not None:
                return target

        l = left_high + 1
        r = right_low - 1
    
    return None


"""

def findIndex(arr: list[int], ele: int) -> int | None:
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == ele:
            return mid
        elif (arr[low] <= ele and ele < arr[mid]) or (arr[mid] < arr[low] and (ele < arr[low] or ele > arr[high])):
            high = mid - 1
        else:
            low = mid + 1

"""
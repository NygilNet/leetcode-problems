"""
link to leetcode: https://leetcode.com/problems/relative-sort-array/description/?envType=daily-question&envId=2024-06-11

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

input: two lists 
output: one list

i. sort the array
ii. find the first key of each element found in arr2, sort from first to last
iii. list interpolation to build the output array

"""

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        remain = []
        def _findFirstIndexAndLength(arr: list[int]) -> tuple[(int, int)]:
            res = {}
            current_ele = arr[0]
            last_index = 0
            current_length = 0

            arr_len = len(arr)
            for i in range(arr_len):
                if arr[i] is current_ele:
                    current_length += 1
                else:
                    res[current_ele] = (last_index, current_length)
                    if current_ele not in arr2:
                        remain.append(current_ele)
                    current_ele = arr[i]
                    last_index = i
                    current_length = 1

            res[current_ele] = (last_index, current_length)
            if current_ele not in arr2:
                remain.append(current_ele)
            return res
        
        a = sorted(arr1)
        first_indices = _findFirstIndexAndLength(a)
        remain.sort()

        res = []
        for ele in arr2:
            idx, length = first_indices[ele]
            res += a[idx: idx + length]
        for ele in remain:
            idx, length = first_indices[ele]
            res += a[idx: idx + length]

        return res


# class Solution:
#     def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
#         def _findFirstIndexAndLength(arr: list[int]) -> tuple[(int, int)]:
#             res = {}
#             current_ele = arr[0]
#             last_index = 0
#             current_length = 0

#             arr_len = len(arr)
#             for i in range(arr_len):
#                 if arr[i] is current_ele:
#                     current_length += 1
#                 else:
#                     res[current_ele] = (last_index, current_length)
#                     current_ele = arr[i]
#                     last_index = i
#                     current_length = 1

#             return res
        
#         a = sorted(arr1)
#         first_indices = _findFirstIndexAndLength(a)

#         res = []
#         for ele in arr2:
#             idx, length = first_indices[ele]
#             res += a[idx: idx + length]

#         return res